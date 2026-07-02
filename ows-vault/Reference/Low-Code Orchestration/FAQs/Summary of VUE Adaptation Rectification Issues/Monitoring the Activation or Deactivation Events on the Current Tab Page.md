---
title: "Monitoring the Activation or Deactivation Events on the Current Tab Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399060785.html"
depth: 3
---
# Monitoring the Activation or Deactivation Events on the Current Tab Page

You need to perform the following adaptation rectification in the versions using VUE:

top.Portal.getCurrentTab().on("activate", () => {
    // do something
})
top.Portal.getCurrentTab().on("deactivate", () => {
    // do something
})

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]