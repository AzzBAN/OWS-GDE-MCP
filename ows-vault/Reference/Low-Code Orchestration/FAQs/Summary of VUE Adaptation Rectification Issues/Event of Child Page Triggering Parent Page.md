---
title: "Event of Child Page Triggering Parent Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399180693.html"
depth: 3
---
# Event of Child Page Triggering Parent Page

You need to perform the following adaptation rectification in the versions using VUE:

//A child page triggers an event.
ParentPage.fireEvent("xxid","xxEvent",params) 
//The event is registered on the parent page.
Spl.EventBus.register("xxid","xxEvent",function(){})

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]