---
title: "Suggestion: Use Simulated Keyboard Instead of Simulated Mouse to Perform Operations as Many as Possible"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001768145200.html"
depth: 6
---
# Suggestion: Use Simulated Keyboard Instead of Simulated Mouse to Perform Operations as Many as Possible

**Description**: Preferentially use simulated keyboard instead of simulated mouse to perform operations because the position of the button needs to be collected for mouse operations, which may vary with the computer environment. Use the mouse to perform operations, such as click and image click operations, that cannot be performed using the keyboard.

**Check guide**: Check whether the process script uses the click control and whether **Simulate Manual Click** is set to **True**

**Positive example**: When a file is uploaded, the cursor is in the text box by default, and the **Select Folder** button is selected by default. You can use the simulated keyboard to paste the absolute path of the file and press **Enter**. No click operations are needed.

![[en-us_image_0000001746851542.png]]

**Tool supported or not**: no

**Specification name**: General\_RPA\_Use\_Simulated\_Keyboard\_Prefer

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]