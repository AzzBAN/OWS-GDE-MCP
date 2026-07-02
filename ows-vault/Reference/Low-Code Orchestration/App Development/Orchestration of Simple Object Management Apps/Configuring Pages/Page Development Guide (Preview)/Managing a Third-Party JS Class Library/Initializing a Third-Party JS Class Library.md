---
title: "Initializing a Third-Party JS Class Library"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_008.html"
depth: 6
---
#### Procedure

1.  In a local file directory, hold down **Shift**, right-click in the blank area, and choose **Open PowerShell Here** or **Open PowerShell window here (S)** from the shortcut menu.
2.  Run **adc init** to initialize the project. Confirm and enter information as prompted.
    
    PS F:\\tempfile\\procode\\procodedemo\\thirdJS> adc init
    ? Select a project type Third JS Library
    ? Name of javascript library: thirdJS
    ? Projec Name of javascript library: demo
    ? Module Name of javascript library: demo
    ? Description: test
    name:  thirdJS
    moduleName:  demo
    projectName:  demo
    description:  test
       create thirdJS\\adcui.json
    Construction completed!
     $  cd thirdJS
    
    **Table 1** Project initialization  
    | Initialization Information | Description |
    | :-- | :-- |
    | Select a project type | Use arrows on the keyboard to select Third JS Library. |
    | Name of javascript library | Customized name of a third-party class library. |
    | Projec Name of javascript library | Project name in Studio. |
    | Module Name of javascript library | Module name in Studio. |
    | Description | Customized description. | 3.  After the project is initialized, verify that the message "Construction completed!" is displayed.
4.  Access the local project directory, use the VSCode-huawei tool to open the folder, and view the initialization code file.