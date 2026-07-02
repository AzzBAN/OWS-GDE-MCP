---
title: "Aggregate Dataframe By Group"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002552560705.html"
depth: 7
---
# Aggregate Dataframe By Group

**pandas.groupBy**

**Description:**

Aggregate dataframe by group according to one or more fields, Similar to the group by operation of the database table.List of user-defined parameters:

1\. axis: The value is 0,1, select grouping row data (0) or column data (1).

2\. level: grouped by a specific level, the by and level parameters cannot be specified at the same time.

3\. as\_index: Whether to return the object indexed by the group label, the default is True.

4\. sort: Whether to sort according to the grouping field, the default is True.

5\. observed: Whether to display the observed value, the default is False.

6\. dropna: Whether to delete the row or column data where the NA value in the grouping field is located.

**Input:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560705__table130395mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:3300%"> <col style="width:3300%"> <col style="width:3300%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560705__row130401mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">name</td><td class="cellrowborder" valign="top" width="33.33333333333333%">type</td><td class="cellrowborder" valign="top" width="33.33333333333333%">help</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130411mcpsimp"><td class="cellrowborder" valign="top" width="33.33333333333333%">reference</td><td class="cellrowborder" valign="top" width="33.33333333333333%">TableObject</td><td class="cellrowborder" valign="top" width="33.33333333333333%">DataFrame to be grouped</td></tr></tbody></table>

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560705__table130421mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560705__row130430mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130449mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">by</td><td class="cellrowborder" valign="top" width="16.666666666666664%">string</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Fields of grouping by.Use array form for multiple fields</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130463mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">aggregation</td><td class="cellrowborder" valign="top" width="16.666666666666664%">list</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">sum|mean|max|min|count</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Select the method of group aggregation</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130477mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">user-defined</td><td class="cellrowborder" valign="top" width="16.666666666666664%">flexibleTable</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">User-defined parameters are used to configure additional parameters of the interface pandas.groupBy. For details, see the official Pandas documentation https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130491mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560705__table130507mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"> <col style="width:2000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560705__row130515mcpsimp"><td class="cellrowborder" valign="top" width="20%">name</td><td class="cellrowborder" valign="top" width="20%">type</td><td class="cellrowborder" valign="top" width="20%">default</td><td class="cellrowborder" valign="top" width="20%">range</td><td class="cellrowborder" valign="top" width="20%">help</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130531mcpsimp"><td class="cellrowborder" valign="top" width="20%">return</td><td class="cellrowborder" valign="top" width="20%">TableObject</td><td class="cellrowborder" valign="top" width="20%">groupby_fd</td><td class="cellrowborder" valign="top" width="20%">-</td><td class="cellrowborder" valign="top" width="20%">DataFrame generated by group aggregation</td></tr></tbody></table>

**samples**

Group and aggregate the data table by the name field to calculate the average value

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002552560705__table130546mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002552560705__row130551mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130558mcpsimp"><td class="cellrowborder" valign="top" width="50%">by</td><td class="cellrowborder" valign="top" width="50%">name</td></tr><tr id="EN-US_TOPIC_0000002552560705__row130564mcpsimp"><td class="cellrowborder" valign="top" width="50%">aggregation</td><td class="cellrowborder" valign="top" width="50%">mean</td></tr></tbody></table>

**Parent topic:** [[Table Data Processing|Table Data Processing]]