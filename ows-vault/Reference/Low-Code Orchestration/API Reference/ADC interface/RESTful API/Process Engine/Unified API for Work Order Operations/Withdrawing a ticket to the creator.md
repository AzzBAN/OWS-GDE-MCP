---
title: "Withdrawing a ticket to the creator"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002502272104.html"
depth: 6
---
#### Function Description

Start with GDE 26.3, Interface script invoked by the instance:

var request = {

"order\_id": "d": "test-20251220-00000001",

"reason": "test",}

var url = "/adc-bpm/rest/v1/unified/order/test\_app/test\_module/test\_process/recall";var response = ServiceInvoker.post(url, request);