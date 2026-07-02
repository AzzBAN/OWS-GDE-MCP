---
title: "General Restrictions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001710244669.html"
depth: 5
---
#### Common Process

Pay attention to the following restrictions when common processes are used in API orchestration:

-   If input or output parameters of the common process to be called by an API are changed, the API Fabric does not automatically update process variables of the API. You need to manually update the process variables.
-   A common process can be called by an API only once.
    
    To call common processes for multiple times, you are advised to define different common processes. If a common process must be called multiple times, service personnel need to modify sub-process data cached when an API calls the common process upon recall of the common process.