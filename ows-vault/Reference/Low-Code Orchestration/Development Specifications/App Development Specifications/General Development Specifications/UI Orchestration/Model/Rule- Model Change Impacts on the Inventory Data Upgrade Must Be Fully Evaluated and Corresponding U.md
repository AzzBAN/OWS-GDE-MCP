---
title: "Rule: Model Change Impacts on the Inventory Data Upgrade Must Be Fully Evaluated and Corresponding Upgrade Plan Must Be Formulated"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123588.html"
depth: 6
---
# Rule: Model Change Impacts on the Inventory Data Upgrade Must Be Fully Evaluated and Corresponding Upgrade Plan Must Be Formulated

**Description**: When properties are modified or added for a model with a large amount of inventory data (for example, million-level records), the entire table needs to be rebuilt in some databases. The time required increases with the data volume. Therefore, you need to formulate an upgrade plan to prevent the asset package import from taking a long time or even timeout.

**Check guide**: For modified models, you can export the asset package and compare the JSON files of the models before and after the modification to determine the modifications.

**Negative example**: No upgrade solution is formulated for the model with a large amount of inventory data. The asset package upgrade mode is used. As a result, importing an asset package may take a long time or even time out, affecting the import of other assets in the same asset package.

**Tool supported or not**: no

**Specification name**: General\_Model\_Fully\_Evaluated\_The\_Impact\_Of\_Model\_Changes

**Severity**: major

**Parent topic:** [[Model|Model]]