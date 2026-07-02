---
title: "Suggestion: Select a Proper Mouse Click Mode"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001814745341.html"
depth: 6
---
# Suggestion: Select a Proper Mouse Click Mode

**Description**: There are three simulated manual click modes: hardware event, JavaScript simulation, and Chromium API. You need to select a proper click mode as required.

-   If the selected mode is a hardware event, the click event is triggered by simulating manual operations. However, if the control is hidden under a pop-up window, the control may fail to be located.
-   If the selected mode is Chromium API, the Chrome DevTools Protocol API is used to simulate a click event.
-   If the selected mode is JavaScript simulation or empty, the click is triggered based on the automation API of the target element. In some cases, the click triggered by the automation API may be blocked by the browser. You can select **Always allow** on the right of the address bar of the browser web page or select another item.
-   The recommended priority is as follows: Chromium API > JavaScript simulation > hardware event
-   Use the hardware event mode for the file selection box.

**Check guide**: Check whether a click control is used in the process script.

**Tool supported or not**: no

**Specification name**: General\_RPA\_Use\_Click\_Mode\_Properly

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]