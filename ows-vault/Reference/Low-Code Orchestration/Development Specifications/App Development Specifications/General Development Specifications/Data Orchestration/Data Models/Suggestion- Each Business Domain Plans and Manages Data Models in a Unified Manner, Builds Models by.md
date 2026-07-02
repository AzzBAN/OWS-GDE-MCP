---
title: "Suggestion: Each Business Domain Plans and Manages Data Models in a Unified Manner, Builds Models by Echelon, and Accumulates Common Basic Packages"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192144744.html"
depth: 6
---
# Suggestion: Each Business Domain Plans and Manages Data Models in a Unified Manner, Builds Models by Echelon, and Accumulates Common Basic Packages

**Specification name**: General\_DataFactory\_Data\_Model\_Hierarchical\_Principle

**Description**: Each business domain has its own model set. Multiple business teams in a business domain may develop and deliver businesses concurrently. It is recommended that each business domain plan and manage data models in a unified manner and accumulate common basic packages. When there is a new requirement, the basic package model is preferentially reused. If the requirement cannot be met, a data model is created. In this way, repeated construction and redundant models can be avoided.

**Check guide**: Check whether the data model development meets the requirement.

**Negative example**: The basic package is not imported and a new data model is created each time.

**Positive example**: The basic packages are developed as the first- or second-echelon apps and are accumulated as assets.

After continuous business delivery and model sorting, the common dimension model app SEQ.COMMON\_DIMENSION is accumulated for the product in the business experience domain. This model app contains more than 600 general dimension models of the business experience domain and is used as a basic package used by the upper-layer apps, avoiding repeated dimension creation and redundant models.

**Impact**: Apps without layered design may have disordered dependencies and are difficult to be managed.

**Parent topic:** [[Data Models|Data Models]]