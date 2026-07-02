---
title: "Rule: Do Not Directly Introduce External URLs and Pages to Assets"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123760.html"
depth: 5
---
# Rule: Do Not Directly Introduce External URLs and Pages to Assets

**Description**: 1. External URLs may have security risks and may cause users' doubts if an alarm is displayed. Therefore, you are not allowed to directly reference external URLs unless they are trusted.

2\. External pages may have security risks. You are not allowed to directly embed external pages into assets unless these page URLs are trusted.

**Check guide**: 1. Check whether external URLs are directly referenced or information is sent to external URLs in source codes.

2\. Check that no external pages are embedded into assets using iframe. You are advised to use Page Panel instead of Frame Panel in an asset. If Frame Panel is used, do not reference external URLs in **Src**.

3\. Check whether the URL configured during page configuration of the menu in the asset cannot reference external URLs.

**Negative example**:

window.open("http://www.hacker.com");

window.location.href="http://www.hacker.com";

window.navigate("http://www.hacker.com ");

window.location.replace("http://www.hacker.com ");

location.href="http://www.hacker.com";

self.location="http://www.hacker.com";

top.location="http://www.hacker.com";

![[en-us_image_0000002417340161.png]]

**Tool supported or not**: yes

**Rectification guide**: Check whether the external URL is trusted. If yes, apply for shielding the alarm. If no, delete the external URL.

**Specification name**: Security\_PhishingAttack\_ExternalUrl

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Anti-phishing|Anti-phishing]]