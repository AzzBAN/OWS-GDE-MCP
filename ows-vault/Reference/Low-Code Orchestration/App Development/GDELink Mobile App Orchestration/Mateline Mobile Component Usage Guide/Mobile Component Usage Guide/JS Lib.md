---
title: "JS Lib"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001735440564.html"
depth: 5
---
# JS Lib

This component provides custom page scripts, which can be used for multiple pages.

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Script | Script name | Example:

Create a JS library file named **jslibtest**. The method defined in the script is as follows:

define(function() {

console.log ("Find define");

return {"equipmentPageReadyCallback":equipmentPageReadyCallback};

});

function equipmentPageReadyCallback() {

console.log ("Find equipmentPageReadyCallback");

Nf.showPopupWindow({message: ''});

$("\[spl-id='testbutton'\]").click(function(){

C("primarykey").setValue('wwww')});

console.log ("End of equipmentPageReadyCallback");

}

The method defined by the library file in the JS component is as follows:

require(\["js!jslibtest"\],

function(detailPage) {

console.log("begin execute js.");

detailPage.equipmentPageReadyCallback();

});

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]