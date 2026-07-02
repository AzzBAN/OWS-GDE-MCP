---
title: "Rule: At least One Authentication Policy Must Be Enabled for an Internal API If It Is Called by an External System"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643453.html"
depth: 5
---
# Rule: At least One Authentication Policy Must Be Enabled for an Internal API If It Is Called by an External System

**Description**: APIs that are called by external systems have high risks of unauthorized access. Authentication policies must be used to reduce the risks. Currently, API Fabric supports the following authentication policies: **OAuth2**, **AK SK Signature**, **Username&password**, and **OpenId**.

**Check guide**: Access the **API Governance** page, choose **API Management**, click **Configure**, choose **Server Configuration** > **Policy Configuration**, and check whether at least one authentication mode of the API- or method-level policy is enabled, or whether an authentication policy is developed in the user policy extension mode.

**Positive example**:

![[en-us_image_0000001521994605.png]]

**Tool supported or not**: yes

**Specification name**: Security\_AccessControl\_API\_AuthPolicyConfig

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: API orchestration

**Parent topic:** [[Access Control|Access Control]]