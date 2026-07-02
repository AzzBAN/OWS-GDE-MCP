---
title: "Rule: The safeHtml Translator Must Be Configured for Rich Text Input Parameters"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162640572.html"
depth: 5
---
# Rule: The safeHtml Translator Must Be Configured for Rich Text Input Parameters

**Description**: The rich text box provides rich page effects and requires page rendering after configuration. If malicious code exists, injection problems, such as XSS injection, may occur. GDE provides the safeHtml() translator for security filtering.

**Check guide**: Log in to the develop-state environment, select a desired asset, and check the pages one by one. If the page contains a rich text box, check whether **Common functions** is selected in the **Translator** column of the corresponding input parameter configuration row for the service that stores the rich text box and whether the safeHtml() translator is added.

![[en-us_image_0000001524254585.png]]

**Positive example**:

1\. Click the input parameter of the rich text type and click the add icon in the **Translator** column to add a translator.

![[en-us_image_0000001472812446.png]]

2\. Set **Translation Mode** to **General Configuration**, **Mapping Type** to **Common functions**, and **Name** to **safeHtml()**.

![[en-us_image_0000001472493218.png]]

**Tool supported or not**: yes

**Specification name**: Security\_DataCheck\_Page\_RichHtml\_NoXssTranslate

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: all

**Parent topic:** [[Data Verification|Data Verification]]