---
title: "Rule: Fields Can Only Be Appended to Physical Tables and Cannot Be Inserted to the Middle"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001191984778.html"
depth: 6
---
# Rule: Fields Can Only Be Appended to Physical Tables and Cannot Be Inserted to the Middle

**Specification name**: General\_DataFactory\_Data\_Model\_Only\_Add\_Fields\_at\_End\_of\_the\_Table

**Description**: For the good performance of modifying the table field sequence on the data engine, fields can only be appended to the table instead of inserting to the middle during the modeling of the physical model.

**Check guide**:

For example, check the field adding mode in the physical model SDR\_CWR\_SMS\_ANALYSIS.

Version 1.0.0

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001191984778__table977mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:25%"> <col style="width:18.75%"> <col style="width:18.75%"> <col style="width:18.75%"> <col style="width:18.75%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001191984778__row985mcpsimp"><th class="firstcol" valign="top" width="25%" id="mcps1.3.6.1.6.1.1">TIMECOLUMN</th><td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.3.6.1.6.1.1 ">APN</td><td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.3.6.1.6.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.3.6.1.6.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.3.6.1.6.1.1 ">GGSN</td></tr></tbody></table>

**Positive example**: In version 1.0.1, the **MSCORPOOLID** attribute field is added to the end of the table.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001191984778__table998mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:25%"> <col style="width:15%"> <col style="width:15%"> <col style="width:15%"> <col style="width:15%"> <col style="width:15%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001191984778__row1007mcpsimp"><th class="firstcol" valign="top" width="25%" id="mcps1.3.8.1.7.1.1">TIMECOLUMN</th><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.8.1.7.1.1 ">APN</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.8.1.7.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.8.1.7.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.8.1.7.1.1 ">GGSN</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.8.1.7.1.1 ">MSCORPOOLID</td></tr></tbody></table>

**Negative example**: In version 1.0.1, the **MSCORPOOLID** attribute field is added to the middle of the table.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001191984778__table1022mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:25%"> <col style="width:15%"> <col style="width:15%"> <col style="width:15%"> <col style="width:15%"> <col style="width:15%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001191984778__row1031mcpsimp"><th class="firstcol" valign="top" width="25%" id="mcps1.3.10.1.7.1.1">TIMECOLUMN</th><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.10.1.7.1.1 ">APN</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.10.1.7.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.10.1.7.1.1 ">MSCORPOOLID</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.10.1.7.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="15%" headers="mcps1.3.10.1.7.1.1 ">GGSN</td></tr></tbody></table>

**Impact**: If a field is inserted to the middle of a released physical model, issues, such as incompatibility, and execution errors of online apps, may occur.

**Parent topic:** [[Data Models|Data Models]]