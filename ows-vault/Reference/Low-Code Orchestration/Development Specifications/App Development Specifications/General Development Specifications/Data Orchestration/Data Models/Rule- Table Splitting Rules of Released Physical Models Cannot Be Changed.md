---
title: "Rule: Table Splitting Rules of Released Physical Models Cannot Be Changed"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001237224689.html"
depth: 6
---
# Rule: Table Splitting Rules of Released Physical Models Cannot Be Changed

**Specification name**: General\_DataFactory\_Data\_Model\_No\_Storage\_Rule\_Modification\_After\_Release

**Description**: Generally, physical data tables are split for storage. They can be split by UTC time or by natural time if time-based splitting is used. To be compatible with historical data, table splitting rules of released physical models cannot be changed.

**Check guide**: Check whether the table splitting rules are changed for released models.

**Negative example**:

The table splitting rule of a physical model released for commercial use in the business experience domain is changed in different model versions.

   
| Version | Physical Model | Time-based Table Splitting Mode | Physical Model Instance |
| :-- | :-- | :-- | :-- |
| 1.0.0 | SDR\_IOT\_CP\_NB\_GTPV2\_15MIN | UTC time–based table splitting | SDR\_IOT\_CP\_NB\_GTPV2\_15MIN\_16978 |
| 1.0.1 | SDR\_IOT\_CP\_NB\_GTPV2\_15MIN | Natural time–based table splitting | SDR\_IOT\_CP\_NB\_GTPV2\_15MIN\_20200825 | **Impact**: If the table splitting rules of released physical models are changed, issues, such as historical data loss and execution errors of online apps, may occur.

**Parent topic:** [[Data Models|Data Models]]