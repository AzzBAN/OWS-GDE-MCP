---
title: "Obtaining the start and limit Parameters by Grid"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500904.html"
depth: 3
---
# Obtaining the start and limit Parameters by Grid

You need to perform the following adaptation rectification in the versions using VUE:

S('missionGrid').grid.toolbars\[0\].cursor || 0  
//It is changed to the following:
S('missionGrid').getPagingParams().start;   

$('#missionGrid .x-grid3-row').length 
//It is changed to the following:
S('missionGrid').getPagingParams().limit

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]