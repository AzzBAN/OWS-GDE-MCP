---
title: "listeners"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_echart_005.html"
depth: 5
---
#### listeners

**listeners** contains the **clickMenu** property, which is used for configuring report display menus.

**clickMenu** provides three modes for configuring display menus. You can right-click **clickMenu** to select one mode.

**Figure 1** listeners  
![[en-us_image_0000001166930658.png]]

The parameters are as follows.

  
| Name | Description | Configuration |
| :-- | :-- | :-- |
| RemoteMenuButtons | Dynamically displayed button | A service returns text, url, target, handler, and items. { text: "", handler: "", url: "", target: "", items: \[\] } In the values, handler is a user-defined processing method name that is registered in advance and items are sub menus. |
| MenuButtonGroup | Menu button group | Used for configuring a group of buttons. |
| RedirectMenuButton | Redirection menu button | Used for configuring menu parameters. type: redirect id: text: parameters: url: | Examples of the following three configuration modes:

-   RemoteMenuButtons
    
    The **serviceId** and **demo\_testremotemunu\_getList** parameters return results in the following format:
    
    { text: "", handler: "", url: "", target: "", items: \[\]}
    
    **Figure 2** RemoteMenuButtons  
    ![[en-us_image_0000001166452356.jpg]]
    
    **Figure 3** Display effect  
    ![[en-us_image_0000001212172215.jpg]]
    
-   MenuButtonGroup
    
    **Figure 4** MenuButtonGroup  
    ![[en-us_image_0000001212330793.jpg]]
    
    **Figure 5** Display effect  
    ![[en-us_image_0000001212092259.jpg]]
    
-   RedirectMenuButton
    
    **Figure 6** RedirectMenuButton  
    ![[en-us_image_0000001166930828.jpg]]
    
    **Figure 7** Display effect  
    ![[en-us_image_0000001212450783.jpg]]
    
-   Display buttons added using scripts
    
    ![[note_3.0-en-us.png]]
    
    In addition to configuring display buttons in the **listeners** configuration tree, you can use a script to add display buttons.
    

In scripts, you can listen to the **Click** events and trigger the generation of new buttons.

//Script format

this.on("click", function(e/\* {data:{}, menu:{}}\*/) {
   if (e.data.x == ?) {
      e.menu.addItem({"type": "redirect", "text":"Drill Down Time", "url":"#", "parameters":""});
   }
});

Example report: multi-Axis-Chart>Three Yaxis Chart

To set displayed buttons only on column charts but not line charts, compile a customized script as follows:

this.on("click", function(e) {
   console.log(e)
   if (e.data.componentSubType == "bar") {
      e.menu.addItem({"type": "redirect", "text":"Drill Down Time", "url":"#", "parameters":""});
   }
});

**Figure 8** Display effect  
![[en-us_image_0000001166770888.jpg]]