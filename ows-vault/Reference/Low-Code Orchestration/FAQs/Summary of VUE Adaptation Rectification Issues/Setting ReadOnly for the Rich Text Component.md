---
title: "Setting ReadOnly for the Rich Text Component"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365340972.html"
depth: 3
---
# Setting ReadOnly for the Rich Text Component

You need to perform the following adaptation rectification in the versions using VUE:

Spl.EventBus.register("text1", "after-init", function() {
         // text1 indicates the component ID. The rich text component is loaded asynchronously and can be operated only after initialization is complete.
    S("text1").setReadOnly(true);
});

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]