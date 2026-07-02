---
title: "Initializing a Customized Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_004.html"
depth: 6
---
#### Procedure

1.  In a local file directory, hold down **Shift**, right-click in the blank area, and choose **Open PowerShell Here** or **Open PowerShell window here (S)** from the shortcut menu.
2.  Run **adc init** to initialize the project. Confirm and enter information as prompted.
    
    ![[en-us_image_0000001121787508.png]]
    
    **Table 1** Project initialization information  
    | Information | Description |
    | :-- | :-- |
    | Select a project type | Retain the default value Customized Page, and press Enter.
    -   Customized Page
    -   Third JS Library
    -   Customized Page Components
    -   Customized Mobile Components
    
     |
    | Select a frame type | Retain the default value vue + adc ui, and press Enter.
    
    -   vue + adc ui
    -   vue + element ui
    -   vue + mobile ui
    -   empty project
    
     |
    | Name of Customized Page | Retain the default value procodedemo, and press Enter. |
    | Description | Page description. |
    | Would you like to include "vuex" in your project | Enter n and press Enter. |
    | Which "CSS extension language" would you like to use? | Retain the default value CSS, and press Enter. | 3.  After the project is initialized, verify that the message "Construction completed!" is displayed.
4.  Access the local project directory, use the VSCode-huawei tool to open the folder, and view the initialization code file.