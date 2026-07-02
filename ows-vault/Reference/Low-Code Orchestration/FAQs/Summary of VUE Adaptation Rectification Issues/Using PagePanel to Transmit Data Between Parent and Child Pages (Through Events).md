---
title: "Using PagePanel to Transmit Data Between Parent and Child Pages (Through Events)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365340980.html"
depth: 3
---
# Using PagePanel to Transmit Data Between Parent and Child Pages (Through Events)

You need to perform the following adaptation rectification in the versions using VUE:

//The parent page sends an event to the child page. (The parameter of the following method is similar to that of Spl.EventBus.fireEvent.)
 S("pagepanelId").downwardEvent(...args)
//The child page sends an event to the parent page.
 ParentPage.fireEvent(...args)

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]