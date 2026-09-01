---
layout: page
title: Human Activity Recognition
description: Participant-aware classification with random forests, support vector machines, and LOSO validation.
importance: 2
category: machine-learning
---

## Overview

This project developed classifiers for human activity recognition from sensor-derived features. The central evaluation question was whether a trained model could generalize to a person not represented in the training data.

## Approach

- Compared random forest and support vector machine classifiers.
- Used five-fold cross-validation for model selection and hyperparameter search.
- Used leave-one-subject-out (LOSO) cross-validation to estimate participant-level generalization.
- Examined accuracy, precision, recall, F1 score, confusion matrices, and ROC behavior.

## Validation rationale

Observations from the same participant are correlated. A random observation-level split can therefore place highly similar records in both training and validation data. LOSO validation keeps each participant entirely within one fold and provides a more realistic estimate for deployment to new users.

## Limitations

Performance may still depend on sensor placement, device characteristics, activity definitions, and population diversity. A production system would require calibration and external validation on independently collected data.

**Tools:** Python, scikit-learn, random forest, SVM, GridSearchCV, group-aware validation
