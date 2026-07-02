---
title: "Suggestion: Data Modeling Must Be Driven by Business Requirements and Iteratively Evolved to Gradually Enrich Data Models"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236944713.html"
depth: 6
---
# Suggestion: Data Modeling Must Be Driven by Business Requirements and Iteratively Evolved to Gradually Enrich Data Models

**Specification name**: General\_DataFactory\_Data\_Model\_Business\_Requirement\_Driven\_Principle

**Description**: Data models are used for business analysis in each domain. Data modeling must be driven by business requirements. Data models need to be designed and implemented using the top-down method based on business requirements, and evolved iteratively to enrich and optimize data models gradually. Actual data is required for implementing down-top model verification to ensure that models are reasonable and correct.

**Check guide**: Check that the designed model meets business requirements and does not contain excessive reserved fields or unnecessary fields.

**Negative example**:

A business system defines a logical entity in the baseline version 1.0.0. Only five fields are used in the current version, and 100 fields (**RESERVED\_1** to **RESERVED\_100**) are reserved for business evolution. The following table shows the data model structure.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001236944713__table1223mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:10%"> <col style="width:8%"> <col style="width:8%"> <col style="width:8%"> <col style="width:8%"> <col style="width:12%"> <col style="width:12%"> <col style="width:12%"> <col style="width:10%"> <col style="width:12%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001236944713__row1236mcpsimp"><th class="firstcol" valign="top" width="10%" id="mcps1.3.6.1.11.1.1">TIMECOLUMN</th><td class="cellrowborder" valign="top" width="8%" headers="mcps1.3.6.1.11.1.1 ">APN</td><td class="cellrowborder" valign="top" width="8%" headers="mcps1.3.6.1.11.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="8%" headers="mcps1.3.6.1.11.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="8%" headers="mcps1.3.6.1.11.1.1 ">GGSN</td><td class="cellrowborder" valign="top" width="12%" headers="mcps1.3.6.1.11.1.1 ">RESERVED_1</td><td class="cellrowborder" valign="top" width="12%" headers="mcps1.3.6.1.11.1.1 ">RESERVED_2</td><td class="cellrowborder" valign="top" width="12%" headers="mcps1.3.6.1.11.1.1 ">RESERVED_3</td><td class="cellrowborder" valign="top" width="10%" headers="mcps1.3.6.1.11.1.1 ">...</td><td class="cellrowborder" valign="top" width="12%" headers="mcps1.3.6.1.11.1.1 ">RESERVED_100</td></tr></tbody></table>

**Positive example**:

The iterative evolution mode is used to gradually enrich the data model under the driving force of requirements. The following tables show the evolution.

Version 1.0.0

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001236944713__table1262mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001236944713__row1270mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.10.1.6.1.1">TIMECOLUMN</th><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.10.1.6.1.1 ">APN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.10.1.6.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.10.1.6.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.10.1.6.1.1 ">GGSN</td></tr></tbody></table>

Version 1.0.1: **MSCORPOOLID** is added to meet the new requirement.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001236944713__table1282mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:20%"> <col style="width:16%"> <col style="width:16%"> <col style="width:16%"> <col style="width:16%"> <col style="width:16%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001236944713__row1291mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.12.1.7.1.1">TIMECOLUMN</th><td class="cellrowborder" valign="top" width="16%" headers="mcps1.3.12.1.7.1.1 ">APN</td><td class="cellrowborder" valign="top" width="16%" headers="mcps1.3.12.1.7.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="16%" headers="mcps1.3.12.1.7.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="16%" headers="mcps1.3.12.1.7.1.1 ">GGSN</td><td class="cellrowborder" valign="top" width="16%" headers="mcps1.3.12.1.7.1.1 ">MSCORPOOLID</td></tr></tbody></table>

Version 1.0.2: **FIRCPDATATIME** is added to meet the new requirement.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001236944713__table1305mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:20%"> <col style="width:13.16%"> <col style="width:13.16%"> <col style="width:13.16%"> <col style="width:13.16%"> <col style="width:13.16%"> <col style="width:14.180000000000001%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001236944713__row1315mcpsimp"><th class="firstcol" valign="top" width="20.004000800160036%" id="mcps1.3.14.1.8.1.1">TIMECOLUMN</th><td class="cellrowborder" valign="top" width="13.162632526505302%" headers="mcps1.3.14.1.8.1.1 ">APN</td><td class="cellrowborder" valign="top" width="13.162632526505302%" headers="mcps1.3.14.1.8.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="13.162632526505302%" headers="mcps1.3.14.1.8.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="13.162632526505302%" headers="mcps1.3.14.1.8.1.1 ">GSN</td><td class="cellrowborder" valign="top" width="13.162632526505302%" headers="mcps1.3.14.1.8.1.1 ">MSCORPOOLID</td><td class="cellrowborder" valign="top" width="14.182836567313464%" headers="mcps1.3.14.1.8.1.1 ">FIRCPDATATIME</td></tr></tbody></table>

**Impact**: Over-design may cause uncontrollable costs, long TTM, and difficulty in evolution.

**Parent topic:** [[Data Models|Data Models]]