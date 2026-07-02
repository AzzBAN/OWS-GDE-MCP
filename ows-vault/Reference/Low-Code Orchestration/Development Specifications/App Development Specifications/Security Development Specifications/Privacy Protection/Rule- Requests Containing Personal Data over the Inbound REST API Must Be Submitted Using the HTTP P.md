---
title: "Rule: Requests Containing Personal Data over the Inbound REST API Must Be Submitted Using the HTTP POST Method"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363629.html"
depth: 5
---
# Rule: Requests Containing Personal Data over the Inbound REST API Must Be Submitted Using the HTTP POST Method

**Description**: You are disallowed to use the HTTP GET method to submit requests containing personal data. If the HTTP POST method is used to submit requests containing personal data, cross-site request forgery attacks can be effectively prevented and improper information disclosure does not exist because URLs with personal data cannot be recorded in server logs, proxy logs, and browser history.

**Check guide**: Log in to the develop-state environment, and choose **Inbound REST**. On the displayed service list page, check services one by one.

**Positive example**:

![[en-us_image_0000001521033221.png]]

**Tool supported or not**: yes

**Specification name**: Security\_PrivacyProtection\_InboundInterface\_UsePostMethod

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: API orchestration - API integration and orchestration

**Parent topic:** [[Privacy Protection|Privacy Protection]]