---
title: "Rule: Use the Validation Operator to Perform Security Verification on External Input Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001604632972.html"
depth: 6
---
# Rule: Use the Validation Operator to Perform Security Verification on External Input Data

**Specification name**: General\_DataFactory\_AIP\_Perform\_External\_Parameter\_Verification

**Description**: You are advised to use the Validation operator to perform security verification on external parameter information in the app to avoid security risks caused by uncertain external input.

**Check guide**: Check whether external input information exists in the app.

**Positive example**: The request parameter information received by the HttpListener(S) operator comes from external systems and the content is risky. The Validation operator is used to verify parameter validity.

**Impact**: If the Validation operator is not used for verification, app running may be affected.

**Parent topic:** [[Data Integration|Data Integration]]