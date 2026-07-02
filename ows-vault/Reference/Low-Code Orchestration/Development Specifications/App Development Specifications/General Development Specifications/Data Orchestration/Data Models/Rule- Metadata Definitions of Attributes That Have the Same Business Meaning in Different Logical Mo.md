---
title: "Rule: Metadata Definitions of Attributes That Have the Same Business Meaning in Different Logical Models Must Be the Same, Including the Field Name, Description, Type, Length, and Value Range"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192144742.html"
depth: 6
---
# Rule: Metadata Definitions of Attributes That Have the Same Business Meaning in Different Logical Models Must Be the Same, Including the Field Name, Description, Type, Length, and Value Range

**Specification name**: General\_DataFactory\_Data\_Model\_Same\_Business\_Meaning\_Same\_Definition

**Description**: The metadata definitions of attributes with the same business meaning must be the same. Otherwise, the attribute definitions in different logical models may be confusing, resulting in conflicts during operations, such as data access and association analysis.

**Negative example**:

The **IMSI** attribute (commonly used in the OSS domain) contains 63 characters after being encrypted. Multiple logical models contain this attribute, and its definitions are listed in the following table.

     
| Logical Model | Attribute Name | Description | Data Type | Data Length | Standard or Not |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Logical model 1 | IMSI | International mobile subscriber identity | VARCHAR | 63 | YES |
| Logical model 2 | IMSI | International mobile subscriber identity | VARCHAR | 63 | YES |
| Logical model 3 | USR\_ID | User ID, that is, IMSI | VARCHAR | 63 | NO |
| Logical model 4 | IMSI | International mobile subscriber identity | VARCHAR | 255 | NO | **Impact**: Inconsistent metadata definitions may cause poor maintainability or even program logic errors.

**Parent topic:** [[Data Models|Data Models]]