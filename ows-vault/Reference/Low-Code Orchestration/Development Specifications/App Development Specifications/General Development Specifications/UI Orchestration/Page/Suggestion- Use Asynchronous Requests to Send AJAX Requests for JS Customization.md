---
title: "Suggestion: Use Asynchronous Requests to Send AJAX Requests for JS Customization"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162800398.html"
depth: 6
---
# Suggestion: Use Asynchronous Requests to Send AJAX Requests for JS Customization

**Description**: Synchronization is not recommended for sending AJAX requests in JS. If synchronization is used, frame freezing will occur on the page.

**Check guide**: Check the value of the **async** property when MessageProcessor.process is used. **async:true** indicates asynchronization, and **async:false** indicates synchronization.

**Positive example**:

![[en-us_image_0000001149866375.png]]

**Negative example**:

![[en-us_image_0000001103186560.png]]

**Tool supported or not**: no

**Specification name**: General\_Page\_Send\_Asynchronous\_Ajax\_Request

**Severity**: suggestion

**Parent topic:** [[Page|Page]]