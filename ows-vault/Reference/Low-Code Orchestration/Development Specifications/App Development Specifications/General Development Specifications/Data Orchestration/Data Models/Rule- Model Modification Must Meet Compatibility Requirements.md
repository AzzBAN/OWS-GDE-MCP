---
title: "Rule: Model Modification Must Meet Compatibility Requirements"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192304722.html"
depth: 6
---
# Rule: Model Modification Must Meet Compatibility Requirements

**Specification name**: General\_DataFactory\_Data\_Model\_Compatibility\_Must\_Be\_Considered

**Description**: During app version iteration, compatibility requirements must be met in any modification, including modification of model fields.

**Check guide**: Check whether the modification meets the following requirements: the data lengths of physical table fields of Spark table models and Hive table models can only be increased; for other models, the data types of physical table fields cannot be changed, and fields cannot be deleted from the physical tables.

The following uses the physical model SDR\_CWR\_VOICE\_ANALYSIS as an example.

Version 1.0.0

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001192304722__table1057mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001192304722__row1065mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.6.1.6.1.1">Physical Column</th><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.1.1 ">TIMECOLUMN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.1.1 ">ASCCNT_ID</td></tr><tr id="EN-US_TOPIC_0000001192304722__row1076mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.6.1.6.2.1">Data Type</th><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.2.1 ">NUMERIC(18)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.2.1 ">VARCHAR(26)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.2.1 ">VARCHAR(63)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.6.1.6.2.1 ">NUMERIC(10)</td></tr></tbody></table>

**Negative example**:

Version 1.0.1: A data type is modified.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001192304722__table1088mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001192304722__row1096mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.9.1.6.1.1">Physical Column</th><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.1.1 ">TIMECOLUMN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.1.1 ">ASCCNT_ID</td></tr><tr id="EN-US_TOPIC_0000001192304722__row1107mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.9.1.6.2.1">Data Type</th><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.2.1 ">NUMERIC(18)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.2.1 ">NUMERIC(26)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.2.1 ">VARCHAR(63)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.9.1.6.2.1 ">NUMERIC(10)</td></tr></tbody></table>

**Positive example**:

Version 1.0.1: A data length is increased.

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001192304722__table1121mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"> <col style="width:20%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001192304722__row1129mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.12.1.6.1.1">Physical Column</th><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.1.1 ">TIMECOLUMN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.1.1 ">CGISAI</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.1.1 ">MSISDN</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.1.1 ">ASCCNT_ID</td></tr><tr id="EN-US_TOPIC_0000001192304722__row1140mcpsimp"><th class="firstcol" valign="top" width="20%" id="mcps1.3.12.1.6.2.1">Data Type</th><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.2.1 ">NUMERIC(18)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.2.1 ">VARCHAR(128)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.2.1 ">VARCHAR(63)</td><td class="cellrowborder" valign="top" width="20%" headers="mcps1.3.12.1.6.2.1 ">NUMERIC(10)</td></tr></tbody></table>

**Impact**: If the model modification does not meet the compatibility requirements, issues, such as execution errors of online apps, may occur.

**Parent topic:** [[Data Models|Data Models]]