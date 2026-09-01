#!/usr/bin/env python3
"""Check WCAG contrast ratios for one or more named color pairs."""

from __future__ import annotations

import argparse
import re
import sys


HEX_COLOR = re.compile(r"^#(?P<value>[0-9a-fA-F]{6})$")


def parse_color(value: str) -> tuple[int, int, int]:
    match = HEX_COLOR.fullmatch(value)
    if not match:
        raise argparse.ArgumentTypeError(f"Expected a six-digit hex color, got {value!r}")
    raw = match.group("value")
    return tuple(int(raw[index : index + 2], 16) for index in (0, 2, 4))


def channel_luminance(channel: int) -> float:
    value = channel / 255
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4


def relative_luminance(color: tuple[int, int, int]) -> float:
    red, green, blue = (channel_luminance(channel) for channel in color)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(foreground: tuple[int, int, int], background: tuple[int, int, int]) -> float:
    lighter, darker = sorted(
        (relative_luminance(foreground), relative_luminance(background)), reverse=True
    )
    return (lighter + 0.05) / (darker + 0.05)


def parse_pair(value: str) -> tuple[str, str, str, float]:
    try:
        name, foreground, background, minimum = value.split(":", maxsplit=3)
        parse_color(foreground)
        parse_color(background)
        threshold = float(minimum)
    except (ValueError, argparse.ArgumentTypeError) as error:
        raise argparse.ArgumentTypeError(
            "Pair must be NAME:#RRGGBB:#RRGGBB:MINIMUM, for example body:#172033:#f7f9fc:4.5"
        ) from error
    if not name.strip() or threshold <= 0:
        raise argparse.ArgumentTypeError("Pair name must be non-empty and minimum must be positive")
    return name.strip(), foreground, background, threshold


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pair", action="append", required=True, type=parse_pair)
    args = parser.parse_args()

    failed = False
    for name, foreground, background, minimum in args.pair:
        ratio = contrast_ratio(parse_color(foreground), parse_color(background))
        passed = ratio >= minimum
        failed |= not passed
        status = "PASS" if passed else "FAIL"
        print(f"{status} {name}: {ratio:.2f}:1 (minimum {minimum:.1f}:1)")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
