---
title: "Rule: Use the Validation Operator to Perform Security Verification on External Input Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370571424.html"
depth: 5
---
# Rule: Use the Validation Operator to Perform Security Verification on External Input Data

**Description**: You are advised to use the Validation operator to perform security verification on external parameter information in the app to prevent security risks caused by uncertain external input.

**Check guide**: Check whether there is external input information in the app.

**Positive example**: The request parameter information received by the HttpListener(S) operator comes from external systems, and the content is risky. The Validation operator is used to verify parameter validity.

**Impact**: If the Validation operator is not used for verification, app running may be affected.

**Specification name**: Security\_DataCheck\_DataFactory\_AIP\_Perform\_External\_Parameter\_Verification

**Severity**: minor

**Orchestration scenario**: data orchestration

**Parent topic:** [[Data Verification|Data Verification]]