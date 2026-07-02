---
title: "Process Form"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365343136.html"
depth: 3
---
# Process Form

For process form pages, the platform JavaScript needs to provide ticket-related functions. After customizing a process form page, check whether the following JavaScript files have been replaced. If not, manually replace them.

**Table 1** JavaScript replacement description of the process form   
| Path of the Ext Version File /bpmruntime/pages/ticket/... | Path of the New Vue Version File /adc-web/bpm/static/pages/legacy/ticket\_vue/... | Description |
| :-- | :-- | :-- |
| getBasicInfo.js | getBasicInfo.js | Obtains ticket information and notify others of handling the ticket through EventUtils. |
| ticket\_create\_base.js | ticket\_create\_base\_new.js | Provides the basic functions of creating a draft, template, and ticket. This script is used in the ticket creation phase. |
| ticket\_create\_base\_new.js |
| ticket\_currentinfo.js | ticket\_currentinfo\_new.js | Displays the ticket ID, title, current phase, current handler, and SLA on the ticket\_currentInfo panel. |
| ticket\_currentinfo\_new.js |
| ticket\_process\_base.js | ticket\_process\_base\_new.js | Provides basic functions for handling tickets and loading more ticket information. This script is used in the ticket creation phase. |
| ticket\_process\_base\_new.js |
| ticket\_basicinfo\_base.js | ticket\_basicinfo\_base\_new.js | Provides basic functions of viewing tickets. This script is used by users without permission or used to view completed tickets on the page containing \_basicinfoPage. |
| ticket\_basicinfo\_base\_new.js |
| follow\_ticket\_script.js | follow\_ticket\_script.js | Provides the function of following tickets. This function has been canceled in the new version and is only compatible. |
| ticket\_info\_base.js | ticket\_info\_base.js | Only displays tickets queried in details mode. |
| EventUtils.js | EventUtils.js | Provides event support for the preceding functions. | If the preceding JavaScript files are copied from the platform JavaScript files and customized, you need to obtain the new JavaScript files, add the custom content, and replace the JavaScript files on the customization page. After the replacement is complete, verify the function and check whether a JavaScript error is reported in the browser console. If so, rectify the fault based on other VUE adaptations.

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]