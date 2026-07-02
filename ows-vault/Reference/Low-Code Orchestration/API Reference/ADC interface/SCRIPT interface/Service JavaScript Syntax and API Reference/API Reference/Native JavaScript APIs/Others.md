---
title: "Others"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_014.html"
depth: 7
---
# Others

Do not use the **eval()** function. If this function is used to process character strings directly or indirectly entered by users, malicious attacks may occur.

**Table 1** Differences between the native JavaScript engine and ADC JavaScript engine   
| Type | Native JavaScript Engine | ADC JavaScript Engine |
| :-- | :-- | :-- |
| Date object | new Date("2021-09-08 08:01:02") | new Date("2021-09-08T08:01:02Z") | **Parent topic:** [[Native JavaScript APIs|Native JavaScript APIs]]