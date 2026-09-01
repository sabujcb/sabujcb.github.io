---
layout: page
title: Solar Energy Forecasting
description: Statistical and machine learning models for short-term photovoltaic production forecasting.
importance: 1
featured_order: 3
category: machine-learning
project_type: Time-series forecasting
status: Completed study
metric_value: "≈0.1618"
metric_label: best non-differenced XGBoost MAE in the project target scale
card_highlights:
  - Benchmarks statistical and machine learning models on identical forecast windows.
  - Preserves temporal ordering to prevent future-to-past leakage.
tools: [Python, R, XGBoost, ARIMA/ETS, time-series CV]
resources:
  - label: TimeSeriesSplit
    url: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
  - label: XGBoost
    url: https://xgboost.readthedocs.io/en/stable/
---

## Overview

This applied forecasting project used hourly photovoltaic production and weather data to compare classical time-series models with supervised machine learning methods.

## Approach

- Integrated measured solar production with external weather data.
- Compared ARIMA/ARMA, exponential smoothing, linear regression, random forest, support vector regression, and XGBoost.
- Evaluated non-differenced and differenced target formulations.
- Used chronological validation to preserve the temporal ordering of observations.

## Result

The strongest non-differenced XGBoost configuration achieved an MAE of approximately **0.1618** in the project’s target scale. Differencing improved selected ARIMA/ARMA configurations, illustrating that target representation can materially change model behavior.

## Engineering and statistical considerations

- Weather predictors must be aligned to the correct forecast timestamp.
- Random train/test splitting would leak future temporal information.
- Forecast accuracy depends on season, weather regime, and forecast horizon.
- Model comparisons are meaningful only when evaluated on the same time windows and scale.

## Limitations

The data were collected from a specific photovoltaic installation and period, so performance should not be generalized to other sites without recalibration and external validation.

**Tools:** Python, R, pandas, scikit-learn, XGBoost, ARIMA/ETS, weather APIs, time-series validation
