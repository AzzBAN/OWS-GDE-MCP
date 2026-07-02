---
title: "$(document).Ready()"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500880.html"
depth: 3
---
# $(document).Ready()

**Issue:** The current framework is SPA. However, $(document).Ready is implemented using jQuery.

$(document).Ready(function(){ console.log("xxx")})

**Solution:** Use a new method for adaptation.

Nf.ready(function(){console.log("xxx")});

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]