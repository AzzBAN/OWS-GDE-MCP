---
title: "Rule: The Number of Properties of a Single Model Cannot Exceed 200"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162640372.html"
depth: 6
---
# Rule: The Number of Properties of a Single Model Cannot Exceed 200

**Description**: Various databases have restrictions on the row length of data. Therefore, you are advised not to define too many properties in a model. It is recommended that the number of properties of a single model be less than or equal to 200. Therefore, the necessity of each model property must be considered during model design.

**Check guide**: Open the property list of the model on the develop-state page and check whether the number of model properties is within the recommended range and whether each model property is necessary.

**Negative example**: After properties are added to multiple versions, the number of properties of some models increases gradually. As a result, the number of properties exceeds the database threshold, and the asset package fails to be deployed or upgraded.

**Exception scenario**: Some models have a large number of properties, but they are fully verified to run properly in each database. In addition, the impact of residual fields and reserved fields in earlier versions on the live network is fully evaluated and verified (for example, properties are deleted after O&M).

**Tool supported or not**: yes

**Specification name**: General\_Model\_The\_Number\_of\_Model\_Attributes\_Should\_Not\_Be\_Too\_Large

**Severity**: minor

**Parent topic:** [[Model|Model]]