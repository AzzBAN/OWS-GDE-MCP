---
title: "Developing and Packaging Customized Plugins"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001178682086.html"
depth: 6
---
#### Context

During customized plugin development, pay attention to the following associated modifications:

-   When you modify or add a command, modify the following information:
    -   Method name in the **action\_ext.py** file
    -   Commands in the **ExtDemon** list of the **register.json** file
    -   Commands in the **commands** list in the **help.json** file
-   When you change the name or version number of a customized plugin package, modify the following content:
    -   Name of the folder in the level-1 directory where the customized plugin project file is located
        
        The folder name is in the **ext\_** _Plugin package name_ **\_** _Version_ format. The value of _Version_ must be in the format of _XX\_XX\_XX_.
        
    -   **name** and **version** in the **actionx.rapx** file
-   When you modify the class name, modify the following information:
    -   Name of the class on which the command in the **action\_ext.py** file depends
    -   Class name in the **register.json** file