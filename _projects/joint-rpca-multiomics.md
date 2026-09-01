---
layout: page
title: Joint-RPCA for Multi-omics Integration
description: Cross-language validation of R/Bioconductor and Python workflows for microbiome data.
importance: 1
category: research
---

## Overview

This active research and software-development project investigates **Joint Robust Principal Component Analysis (Joint-RPCA)** for integrating microbiome multi-omics data. The practical goal is to make results from R/Bioconductor and Python/Gemelli workflows comparable by controlling preprocessing, configuration, randomness, and output alignment.

## Methodological focus

- Apply equivalent abundance, prevalence, and frequency filtering before ordination.
- Preserve a shared sample set across multiple assays.
- Run both implementations with fixed configuration and random seeds.
- Compare sample scores, feature loadings, explained variation, and cross-validation outputs.
- Account for sign and rotational indeterminacy when comparing latent representations.

## Validation evidence

The working IBD multi-omics dataset contains 60 shared samples. Before frequency filtering, the current workflow retains 459 metagenomic features and 800 metatranscriptomic features. A 10% frequency threshold retains 334 and 785 features, respectively. These counts are treated as reproducibility checks rather than biological conclusions.

## Engineering contribution

The work includes test coverage for input filtering, reproducible Quarto documentation, structured configuration files, and interoperable R/Python outputs. Negative or missing values are rejected before transformation, and threshold semantics are tested explicitly.

## Limitations

- Equivalent software settings do not guarantee identical numerical optimization paths.
- Latent components may require sign or orthogonal alignment before comparison.
- Biological interpretation requires domain validation beyond computational agreement.

## Repositories

- [`Joint_RPCA_in_R`](https://github.com/sabujcb/Joint_RPCA_in_R)
- [`mia_JRPCA`](https://github.com/sabujcb/mia_JRPCA)
- [`OMAWorkflows`](https://github.com/sabujcb/OMAWorkflows)

**Tools:** R, Python, Bioconductor, `mia`, `MultiAssayExperiment`, Gemelli, Quarto, GitHub Actions
