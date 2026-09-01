---
layout: page
title: Protein–Drug Affinity Prediction
description: Validation study showing how evaluation design changes apparent model generalization.
importance: 2
category: research
---

## Overview

This project examined predictive modeling for protein–drug affinity, with particular attention to whether performance persists when the model encounters unseen proteins or unseen drugs.

## Evaluation design

Three validation strategies were compared:

| Strategy                  | Generalization question                        | Concordance index |
| ------------------------- | ---------------------------------------------- | ----------------: |
| Leave-one-observation-out | Can the model predict another observed pair?   |            ≈0.829 |
| Leave-one-protein-out     | Can the model generalize to an unseen protein? |            ≈0.512 |
| Leave-one-drug-out        | Can the model generalize to an unseen drug?    |            ≈0.829 |

## Main finding

The sharp performance decrease under leave-one-protein-out validation shows that strong random or observation-level validation can hide a major generalization weakness. The result illustrates why the cross-validation unit must match the intended deployment scenario.

## Reproducibility principles

- Group-aware splits were defined before model fitting.
- Preprocessing and feature selection were restricted to training data.
- The evaluation reports the validation estimand represented by each split, not only a single aggregate score.

## Limitations

The results are specific to the available proteins, drugs, representations, and sample size. Additional external datasets and uncertainty estimates would be required before drawing deployment-level conclusions.

**Tools:** Python, scikit-learn, group-aware cross-validation, concordance-index evaluation
