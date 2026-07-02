---
title: "Rule: Cards Must Run Independently and Cannot Depend on Each Other"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523397.html"
depth: 6
---
# Rule: Cards Must Run Independently and Cannot Depend on Each Other

**Description**:

1\. A card can run independently on a page and cannot depend on other cards.

2\. If cards need to communicate with each other, the card events need to be configured for the current online orchestration. Cards can be used to release and subscribe to events.

**Check guide**: Use card events to implement communications between cards. Other methods are forbidden.

**Positive example**:

![[en-us_image_0000002354295621.png]]

**Tool supported or not**: no

**Specification name**: General\_Card\_Must\_Support\_Independent\_Operation

**Severity**: major

**Parent topic:** [[Card|Card]]