---
layout: page
title: ECG Heart-rate Estimation
description: Signal-processing pipeline for robust heart-rate estimation from short ECG segments.
importance: 1
category: data-science
---

## Overview

This project analyzed 200 ECG segments, each 30 seconds long and sampled at 200 Hz, to estimate heart rate under signal-quality and peak-detection variability.

## Approach

- Established a baseline estimator with an MAE of **12.38 beats per minute**.
- Investigated peak-detection, autocorrelation, and spectral estimates.
- Used physiological plausibility constraints and signal-quality checks.
- Compared errors across records rather than relying only on an overall average.

## Technical considerations

Peak detection can fail because of noise, baseline wander, ectopic beats, or incorrect thresholds. Autocorrelation and spectral estimates provide complementary evidence, but each can also select harmonics. A robust estimator therefore needs agreement checks and explicit handling of low-confidence segments.

## Limitations

The project dataset and short-window design constrain generalization. Clinical use would require validated acquisition protocols, uncertainty reporting, external cohorts, and medical-device quality controls.

**Tools:** Python, NumPy, SciPy, digital signal processing, peak detection, spectral analysis
