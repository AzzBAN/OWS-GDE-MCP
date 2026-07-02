---
title: "Configuring a Custom Theme"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/page_008.html"
depth: 5
---
#### Context

ADC allows you to develop applications for various industries and meets your specific theme color requirements. On ADC, developers can customize application theme colors that meet preferences of target users and industries.

When the theme switching function is enabled, the four themes that can be switched are **Default**, **Black**, **Deep Sea Blue**, and **Moon Shadow Grey**. The theme colors have been preset and can be used directly. No color is preset for the **Deep Sea Blue** theme. You need to define the theme color of the corresponding style.

Therefore, when customizing a theme, you can set the theme name to **Deep Sea Blue** and define the theme style for theme switching on the GUI. If the custom theme name is set to a name other than **Deep Sea Blue**, you need to use scripts to load the theme on the page.

**Table 1** Theme application scope   
| Category of GUI Elements | Preset Theme Style | Custom Theme Style |
| :-- | :-- | :-- |
| Platform pages (such as the Portal Common Configuration and system configuration pages) | Styles of the Default, Black, and Moon Shadow Grey themes are supported. | The theme style cannot be customized. |
| Elements at the framework layer (colors of top title bar and menu theme) | Styles of the Default, Black, and Moon Shadow Grey themes are supported. | The style of the Deep Sea Blue theme can be customized. You can select Deep Sea Blue from the Switch Theme drop-down list. |
| App orchestration pages (pages generated after orchestration in a project) | Styles of the Default, Black, and Moon Shadow Grey themes are supported. | The style of any theme can be customized.
-   To customize the style of the **Deep Sea Blue** theme, you can select **Deep Sea Blue** from the **Switch Theme** drop-down list.
-   To customize the style of a theme other than **Deep Sea Blue**, you can use the following scripts to load the theme on the page:
    
    U.ready(function(){
        U.loadCurrentTheme("newtheme")
    });
    

 | When the theme switching function is enabled for runtime-state deployment, you can switch the themes.

**Figure 1** Switch Theme  
![[en-us_image_0000002346846562.png]]