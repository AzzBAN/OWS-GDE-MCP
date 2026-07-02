---
title: "Border Layout Panel"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500908.html"
depth: 3
---
# Border Layout Panel

You need to perform the following adaptation rectification methods in the versions using VUE:

Original registration method: Nf.EventBus.register("border-south.afterlayout", function (){})
Current registration method: Spl.EventBus.register(" Border Layout Component ID", "border-south.afterlayout", function(args){})

Original registration mothod: Nf.EventBus.register("border-west.collapseEvent", function (){)}
Current registration method: Spl.EventBus.register(" Border Layout Component ID", "border-west.collapseEvent", function(args){})

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]