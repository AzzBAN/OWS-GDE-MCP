---
title: "Tool Management"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734768746.html"
depth: 7
---
#### Procedure

1.  Log in to the home page of the agent, click ![[en-us_image_0000002299256000.png]] in the upper right corner, and choose **Settings** > **Tools**.
2.  (Optional) If a browser other than Google Chrome is used, install the WeAutomate Web plugin for the browser to ensure that the related web scripts can be executed.
    
    1.  In the **Extensions** area, click the browser plugin card based on the used browser type.
        
        **Figure 1** Browser plugin cards
        
        ![[en-us_image_0000001623258501.png]]
        
    2.  In the displayed dialog box, perform subsequent operations as prompted and click **OK**.
    
3.  After the plugin of the browser is installed, enable the **WeAutomate Web** plugin in the browser to ensure that the related web scripts can be executed by WeAutomate Assistant.
    
    The following uses the Google Chrome browser as an example to describe how to enable the plugin. For details about how to enable other browsers, see the related browser documents.
    
    1.  Open Google Chrome, click ![[en-us_image_0000001623098061.png]] in the upper right corner, and select **Settings**.
    2.  In the navigation pane, choose **Extension Management**.
    3.  On the **Extension Management** page, toggle on **WeAutomate Web** and restart the browser for the new plugin to take effect.
        
        **Figure 2** Enabling the browser plugin
        
        ![[en-us_image_0000001573218310.png]]
        
    
4.  (Optional) To use Assistant to execute Java desktop app scripts, install the corresponding Java app plugin.
    
    Return to the tool page of the agent and select a plugin installation mode from the Java card based on the installation path of the used Java app.
    
    -   In the default mode, install plugins for Java apps that are installed in the **Program Files** or **Program Files(x86)** directory and for which the _%JRE\_HOME%_ environment variable is set. In this case, click **Default Installation** and wait until the installation is complete.
    -   In the manual mode, install plugins for Java apps that are not installed in the **Program Files** and **Program Files(x86)** directories. In this case, click **Manual Installation**. In the displayed **Install Java Plugin in Custom Directory** dialog box, enter or select the Java app installation directory and click **Install**.
    
    ![[en-us_image_0000001623378397.png]]
    
5.  (Optional) Install the web driver tool of the Assistant.
    
    1.  Download the web driver tool.
        
        In the **Web Driver** area on the **Tools** page of the agent, click ![[en-us_image_0000002300139920.png]] on the right of **Current Browser Version** on the card based on the browser type, and then go to the directory based on the browser version to download the web driver file containing **Driver**.
        
    2.  After the download is completed, click ![[en-us_image_0000002299972382.png]] on the right of **Current Driver Version** to import the downloaded web driver file.
        
        **Figure 3** Importing the web driver
        
        ![[en-us_image_0000002299972390.png]]