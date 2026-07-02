---
title: "Developing a Playback Plugin for the Customized Recorder"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001215643322.html"
depth: 5
---
#### Context

After a customized recorder is developed, the corresponding customized playback plugin must be available. Otherwise, the script recorded by the customized recorder may fail to be played back. The customized playback plugin must contain the commands listed in the following table.

**Table 1** Command list (Recording)  
| Command | Description |
| :-- | :-- |
| click | Left-click the mouse. |
| doubleClick | Double-click the left mouse button. |
| rightClick | Right-click the mouse. |
| moveToElement | Move the cursor to a specified element and perform the recording using floating menus. |
| type | Enter the content in the element. |
| getText | Obtain the element text and record it using floating menus. | **Table 2** Command list (Pickup)  
| Command | Description |
| :-- | :-- |
| Custom | Customize the pickup command based on service requirements. In the help.json file corresponding to the command, inspector of a parameter must be set to true, indicating that the parameter can be picked up. |