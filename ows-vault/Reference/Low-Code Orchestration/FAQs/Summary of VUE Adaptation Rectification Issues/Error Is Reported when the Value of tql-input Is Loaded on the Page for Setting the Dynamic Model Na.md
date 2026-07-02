---
title: "Error Is Reported when the Value of tql-input Is Loaded on the Page for Setting the Dynamic Model Name in the TQLInput Component"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500884.html"
depth: 3
---
# Error Is Reported when the Value of tql-input Is Loaded on the Page for Setting the Dynamic Model Name in the TQLInput Component

You need to perform the following adaptation rectification in the versions using VUE:

//Register the LoadDataFinished event in the new framework and reset the value of tql-input.
Spl.EventBus.register('LoadFormData1', "LoadDataFinished", function (data) {
     let oldValue \= data.data.result\["monitored\_model\_condition"\];
     S('monitored\_model\_condition').setValue(oldValue);
});

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]