---
title: "Rule: Asset Matching Resources Cannot Contain Source Code or Sensitive Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370571428.html"
depth: 5
---
# Rule: Asset Matching Resources Cannot Contain Source Code or Sensitive Data

**Description**: Resources released with assets, including documents, icons, images, and tables, cannot contain source code or sensitive data of any format to prevent improper data disclosure.

**Check guide**: Check the matching resources in the asset package to ensure that the asset package does not contain source code or sensitive data.

**Positive example**:

The matching resources in the asset package contain only necessary resource files.

![[en-us_image_0000001688870648.png]]

**Negative example**:

The source code file is embedded in the app help document.

![[en-us_image_0000001817712789.png]]

**Tool supported or not**: no

**Specification name**: Security\_SensitiveData\_Resource\_Not\_Include\_SourceCode\_And\_SensitiveData

**Category**: non-bottom-line check item

**Severity**: critical

**Orchestration scenario**: all

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]