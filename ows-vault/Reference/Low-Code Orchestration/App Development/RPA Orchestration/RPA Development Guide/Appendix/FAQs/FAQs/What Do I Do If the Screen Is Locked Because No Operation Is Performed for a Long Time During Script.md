---
title: "What Do I Do If the Screen Is Locked Because No Operation Is Performed for a Long Time During Script Execution?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001222554889.html"
depth: 7
---
#### Procedure

1.  Start Studio.
2.  In the navigation pane, click ![[en-us_image_0000001508041793.png]].
3.  In the **Recently Edited Items** area, click the project name to go to the project design page.
4.  Configure the screen lock prevention function.
    
    1.  Drag the **Run python Expression** control to the canvas, and click ![[en-us_image_0000001222438989.png]] on the right of **Expression**.
    2.  In the displayed **Expression** dialog box, enter the following expression to prevent the screen locking:
        
        **from ctypes import windll**
        
        **windll.kernel32.SetThreadExecutionState(0x80000002)**
        
        ![[en-us_image_0000001176719554.png]]
        
    3.  Click **OK**.
    
5.  Disable the screen lock prevention function.
    
    1.  Drag the **Run python Expression** control to the canvas, and click ![[en-us_image_0000001176719946.png]] on the right of **Expression**.
    2.  In the displayed **Expression** dialog box, enter the following expression to disable the screen lock prevention:
        
        **from ctypes import windll**
        
        **windll.kernel32.SetThreadExecutionState(0x80000000)**
        
    3.  Click **OK**.