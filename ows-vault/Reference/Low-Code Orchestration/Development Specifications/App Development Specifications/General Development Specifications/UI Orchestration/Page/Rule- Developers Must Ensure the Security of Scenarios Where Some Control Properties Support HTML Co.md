---
title: "Rule: Developers Must Ensure the Security of Scenarios Where Some Control Properties Support HTML Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403845.html"
depth: 6
---
# Rule: Developers Must Ensure the Security of Scenarios Where Some Control Properties Support HTML Configuration

**Description**: Some properties of some standard controls provided by the current system support HTML configuration. The system provides only some foolproof measures, which cannot ensure security fundamentally. Developers need to ensure security, configurable HTML components in the current system include the HTML template attributes of the card and table components, HTML template attributes of the table column component, HTML panel code attributes, and title template and row template attributes of the list view component.

**Check guide**: A message similar to the following is displayed when you configure properties in the page designer:

![[en-us_image_0000001263857590.png]]

**Positive example**:

![[en-us_image_0000001682029309.png]]

**Negative example**:

![[en-us_image_0000001633471146.png]]

**Tool supported or not**: no

**Specification name**: General\_Page\_Use\_Html\_Template

**Severity**: minor

**Parent topic:** [[Page|Page]]