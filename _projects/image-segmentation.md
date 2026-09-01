---
layout: page
title: RGB and NIR Image Segmentation
description: Controlled comparison of RGB and multimodal inputs for semantic segmentation.
importance: 3
category: machine-learning
---

## Overview

This computer-vision project compared image-segmentation models trained with RGB information and combined RGB/near-infrared inputs.

## Result

| Input configuration | Test score |
| ------------------- | ---------: |
| RGB                 |     87.01% |
| RGB + NIR           |     86.45% |

The RGB-only configuration performed slightly better in the final comparison. The result is a useful reminder that adding a sensor modality does not automatically improve generalization; alignment, noise, architecture, normalization, and sample size all affect whether the additional signal is useful.

## Evaluation considerations

- Training, validation, and test images were kept separate.
- Model selection was based on validation performance rather than the final test set.
- Input pipelines were compared under a consistent evaluation protocol.

## Limitations

The difference between configurations should be interpreted with uncertainty and repeated-run variability in mind. A stronger conclusion would require repeated training seeds and confidence intervals or a paired comparison across test images.

**Tools:** Python, deep learning, image preprocessing, RGB/NIR data, semantic segmentation
