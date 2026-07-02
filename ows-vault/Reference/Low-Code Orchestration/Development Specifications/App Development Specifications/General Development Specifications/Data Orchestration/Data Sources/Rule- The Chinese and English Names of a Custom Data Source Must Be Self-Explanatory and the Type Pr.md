---
title: "Rule: The Chinese and English Names of a Custom Data Source Must Be Self-Explanatory and the Type Prefix Is Contained in the Custom Data Source Name"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662126317.html"
depth: 6
---
# Rule: The Chinese and English Names of a Custom Data Source Must Be Self-Explanatory and the Type Prefix Is Contained in the Custom Data Source Name

**Specification name**: General\_DataFactory\_Datasource\_Naming\_Specifications

**Description**:

1.  When creating a custom data source, specify the scenario and storage medium in the Chinese and English names of the data source.
2.  When creating a custom data source, add the type prefix of the custom data source for easy identification.

**Check guide**:

1.  Check whether the Chinese and English names of the custom data source are self-explanatory.
2.  Check whether the custom data source name contains a type prefix.

**Positive example**: **Gauss100\_UserInfo\_**_xxx_

**Negative example**: **Custom\_TableA\_**_xxx_

**Impact**: Non-standard names result in poor maintainability of data sources and failure to identify data source types.

**Parent topic:** [[Data Sources|Data Sources]]