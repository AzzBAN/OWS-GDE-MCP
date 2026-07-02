---
title: "Rule: Names and Aliases of Logical Models Must Be Self-Explanatory"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236784715.html"
depth: 6
---
# Rule: Names and Aliases of Logical Models Must Be Self-Explanatory

**Specification name**: General\_DataFactory\_Model\_Names\_Self\_Annotated\_Names

**Description**: During data modeling, metadata, such as the names and aliases of logical entities, must be properly defined because it is displayed on the business system WebUI. The business side needs to formulate a set of business scenario–based naming rules. The names and aliases must be self-explanatory and can indicate the business meaning or the business application scenario.

The logical model naming must comply with _GTS Unified Data Standard V2020.0_.

**Check guide**: Check whether names and aliases of logical models are self-explanatory.

**Negative example**

 
| Logical Model Name | Alias |
| :-- | :-- |
| OC\_YYS | Carrier configuration table | **Positive example**

 
| Logical Model Name | Alias |
| :-- | :-- |
| DETAIL\_UFDR\_STREAMING\_CHRMR | User-plane streaming service and RAN CHR/MR association xDR |
| CFG\_CWR\_USER\_INFO | CWR Add a user tag configuration table | **Impact**: Non-standard naming results in poor model maintainability and repeated construction.

**Parent topic:** [[Data Models|Data Models]]