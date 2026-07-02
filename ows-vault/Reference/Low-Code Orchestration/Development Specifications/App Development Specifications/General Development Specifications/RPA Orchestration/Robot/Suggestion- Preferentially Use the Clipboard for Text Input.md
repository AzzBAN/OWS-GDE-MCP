---
title: "Suggestion: Preferentially Use the Clipboard for Text Input"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001814865245.html"
depth: 6
---
# Suggestion: Preferentially Use the Clipboard for Text Input

**Description**: The clipboard is preferred for text input. Before pasting a text, clear the text box to ensure that no other texts exist.

**Check guide**: Check whether the type control is used in the process script.

**Positive example**:

-   Check whether a control for the data clearance operation is performed before entering and pasting information. For example, press **Ctrl+A** or **Delete** and then paste the information, or press **Ctrl+A** and then **Ctrl+V** to overwrite the information.
    
    ![[en-us_image_0000001746850510.png]]
    
-   Do not use the input text control. If the character string is too long, the input may be disordered. If you need to use the control, clear the text box before entering the character string.
    
    ![[en-us_image_0000001793809701.png]]
    

**Tool supported or not**: no

**Specification name**: General\_RPA\_Use\_Clipboard\_Prefer

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]