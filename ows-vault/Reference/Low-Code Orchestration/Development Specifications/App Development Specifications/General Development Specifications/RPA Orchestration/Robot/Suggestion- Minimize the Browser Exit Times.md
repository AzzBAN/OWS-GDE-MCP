---
title: "Suggestion: Minimize the Browser Exit Times"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001768145180.html"
depth: 6
---
# Suggestion: Minimize the Browser Exit Times

**Description**: When you exit the browser and then open it, the robot needs to re-establish a connection with the browser. The connection may fail to be established, causing robot execution failures. Therefore, do not frequently exit the browser or kill the browser processes in the same script. If you want to close a web page, close the tab.

**Check guide**: Check whether the quit or killProcess control is used in the process script to exit the browser.

**Tool supported or not**: no

**Specification name**: General\_RPA\_Forbidden\_Use\_Subprocess

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]