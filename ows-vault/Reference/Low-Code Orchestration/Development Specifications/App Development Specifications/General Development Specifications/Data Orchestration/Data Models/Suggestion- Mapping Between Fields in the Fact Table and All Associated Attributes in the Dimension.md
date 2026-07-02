---
title: "Suggestion: Mapping Between Fields in the Fact Table and All Associated Attributes in the Dimension Level Needs to Be Clearly Defined"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001237224691.html"
depth: 6
---
# Suggestion: Mapping Between Fields in the Fact Table and All Associated Attributes in the Dimension Level Needs to Be Clearly Defined

**Specification name**: General\_DataFactory\_Data\_Model\_Clarify\_Relationship\_Between\_Dimension\_Model\_and\_Fact\_Table

**Description**: In the multidimensional aggregation model, the rollup and drilldown of the multidimensional aggregation and query can be performed only when the association between the dimension and fact table is complete. Therefore, the mapping between fields in the fact table and all associated attributes in the dimension level need to be clearly defined.

**Positive example**: The following tables describe the association between the fact table **CDR\_AIU\_MOC\_CHRMR** and the dimension **Last BSC/RNC**. The dimension **Last BSC/RNC** contains three associated attributes, and the fields in the fact table are mapped to the three associated attributes in the dimension level.

   
| Fact Table | Dimension Level | Dimension Attribute | Mapping |
| :-- | :-- | :-- | :-- |
| CDR\_AIU\_MOC\_CHRMR | Last BSC/RNC | MSC or POOL\_ID of LASTBSC\_SPC | \[POOLID\] |
| Network ID of Last BSC/RNC | \[NI\] |
| Signaling point of LASTBSC\_SPC | \[LASTBSCRNC\] | 
| Dimension Table | Dimension Level | Aggregation Level | Dimension Attribute | Field Mapping |
| :-- | :-- | :-- | :-- | :-- |
| DIM\_TERMINAL | Terminal TAC | 1 | Terminal TAC | \[TAC\] |
| Terminal Brand | 2 | Terminal Brand | \[TER\_BRAND\_NAME\] |
| Terminal OS | 2 | Terminal OS | \[TER\_OSTYPE\] |
| Terminal Type | 2 | Terminal Type | \[TER\_TYPE\_ID\] |
| Terminal Model | 2 | Terminal Model | \[TER\_MODEL\_NAME\] | **Negative example**: The attributes are not associated or only some attributes are associated.

**Impact**: If the association is incomplete, analysis cannot be performed in the dimension that is not associated.

**Parent topic:** [[Data Models|Data Models]]