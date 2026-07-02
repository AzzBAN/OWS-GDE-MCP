---
title: "Communication Between Pages at the Same Level Through Events"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399060813.html"
depth: 3
---
# Communication Between Pages at the Same Level Through Events

You need to perform the following adaptation rectification in the versions using VUE:

//Child page A sends an event to the parent page.
ParentPage.fireEvent("reloadMember\_colle", "reload", "");
//Parent page registers the event of page B and sends the event to the war\_room\_member\_page child page (that is, child page B).
Spl.EventBus.register("reloadMember\_colle", "reload", function () {
 S("war\_room\_member\_page").downwardEvent("reloadMember","reload","");
 });  
//Child page B registers the event for service logic processing.
Spl.EventBus.register("reloadMember", "reload", function () { 
//do something 
});

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]