---
title: "This interface is used to query the detailed information about the associated TT of a specified TT according to the TT ID and whether the TT is archived."
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001972666689.html"
depth: 6
---
#### Function

Starting from GDE 24.2, Interface script invoked by the instance:

var request =

{

"order\_id":"INC-20221111-00000003"};

var url = "/adc-bpm/rest/v1/order/associate-order/query";

var response = ServiceInvoker.post(url, request);