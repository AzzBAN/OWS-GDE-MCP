---
title: "Rule: For Inheritance Purposes, Entity Names and Entity Field Names Cannot Be Modified or Deleted in the Evolution of Released Baseline Models"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236944711.html"
depth: 6
---
# Rule: For Inheritance Purposes, Entity Names and Entity Field Names Cannot Be Modified or Deleted in the Evolution of Released Baseline Models

**Specification name**: General\_DataFactory\_Data\_Model\_Inheritance\_Principle

**Description**: For the compatibility with historical data and good database performance, for released data models, their entity field names cannot be deleted or changed, and their entity names cannot be changed unless there are design defects. In addition, new fields cannot change the meaning of the original entities.

**Check guide**: Check whether entity names are changed or entity field names are deleted or changed for released models.

**Negative examples**:

-   Example 1: A business team released the physical model FBB\_HSI\_OLT\_HTTP\_MAP for HTTP data records of access devices in the baseline version 1.0.0. The team changed the physical model name to FBB\_HSI\_OLT\_HTTP\_MAP\_NEW in version 1.0.1, which is not allowed.
-   Example 2: A business team released the physical model DETAIL\_UFDR\_THROUGHPUT in the baseline version 1.0.0, and the model contains the physical field **DW\_PEAK\_THROUGHPUT\_1** that indicates the downlink throughput (bit/s) at the peak hour in the first period. The team changed the field name in the physical model to **DW\_PEAK\_TP\_1** in version 1.0.1, which is not allowed.

**Impact**: If the entity names are changed or entity field names are deleted or changed for released models, compatibility issues may occur, causing errors during program execution.

**Parent topic:** [[Data Models|Data Models]]