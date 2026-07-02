---
title: "Rule: Sensitive Data Cannot Be Exported and Personal Data Export Must Be Protected"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363613.html"
depth: 5
---
# Rule: Sensitive Data Cannot Be Exported and Personal Data Export Must Be Protected

**Description**:

Exporting sensitive data or personal data may cause improper data disclosure and trust crisis.

1\. The export function is not provided for sensitive data. For details about the sensitive data classification, see [[Appendix 1- Sensitive Data|Appendix 1: Sensitive Data]].

2\. The export function is provided for personal data only in business scenarios. For details about the personal data classification, see [[Appendix 2- Examples of Personal Data|Appendix 2: Examples of Personal Data]].

3\. If the export function is required in business scenarios, the following protection mechanisms must be provided:

(1) Minimum permission: The export function can be assigned only to users required for business processing.

(2) Traceability: Operation logs must be recorded when personal data is exported.

(3) Encryption protection: The personal data needs to be exported in encryption mode.

**Check guide**:

Check whether the exported service data contains sensitive data or personal data.

**Positive example**:

1\. Customized assets do not provide the capability for exporting personal data in batches.

2\. The exported data does not contain sensitive personal data, or personal data is encrypted in specific scenarios.

![[en-us_image_0000002412480609.png]]

**Negative example**:

1.  The assets developed in customized mode provide the capability of exporting all user data.
2.  The exported data contains personal or sensitive data.

![[en-us_image_0000002412360801.png]]

**Exception scenarios**:

If the plaintext export is required in a scenario, the security expert of the business domain needs to review whether the scenario is proper and notify related personnel of the risks.

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_DonotSupportExport

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]