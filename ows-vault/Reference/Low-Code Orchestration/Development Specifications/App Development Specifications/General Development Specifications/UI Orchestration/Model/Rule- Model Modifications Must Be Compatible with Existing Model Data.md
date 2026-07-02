---
title: "Rule: Model Modifications Must Be Compatible with Existing Model Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963692.html"
depth: 6
---
# Rule: Model Modifications Must Be Compatible with Existing Model Data

**Description**: When an existing model is modified, if the model has been used at some sites, the new model must be backward compatible with the model before the modification to ensure that the model can be successfully upgraded to the new model at these sites. At least the following requirements must be met:

-   Do not add mandatory properties. If a mandatory property is added, the inventory data in the model before the upgrade does not meet the mandatory requirements of the new property.
-   The property cannot be deleted. Deleted properties cannot be rolled back.
-   When the length of a text property is changed, it can be prolonged but not shortened. If the text property is shortened, the inventory data in the model before the upgrade does not meet the property length requirements.

The preceding requirements are only the basic compatibility requirements. There may be some differences between versions.

**Check guide**: When a model is modified on the develop-state page, a message is displayed if an operation that may be incompatible with the model data before the modification is performed (for example, the length of a text property is shortened). For modified models, you can export the asset package and compare the JSON files of the models before and after the modification to determine the modifications.

**Positive example**: Fully evaluate the model differences between versions to ensure that the changes are compatible with the inventory data on the live network.

**Exception scenario**: If the data of the inventory model that is not backward compatible with must be modified, the model must be upgraded through O&M methods such as manual operations on the database.

**Tool supported or not**: no

**Specification name**: General\_Model\_Backward\_Compatible\_With\_The\_Model\_Data\_Before\_The\_Change.

**Severity**: minor

**Parent topic:** [[Model|Model]]