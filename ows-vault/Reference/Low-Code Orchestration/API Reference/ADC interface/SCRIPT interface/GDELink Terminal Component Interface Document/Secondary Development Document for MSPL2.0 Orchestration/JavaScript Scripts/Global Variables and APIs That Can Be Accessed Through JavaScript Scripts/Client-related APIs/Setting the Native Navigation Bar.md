---
title: "Setting the Native Navigation Bar"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457117585.html"
depth: 9
---
#### U.setNavigationBar(obj)

Used to allow users to display native navigation pane on the top of light apps and configure related information.

![[notice_3.0-en-us.png]]

The Harmony version is not supported.

 
| Parameter | Type |
| :-- | :-- |
| obj | Object | Example:

  let obj = {
leftType: "text", //none: hidden; icon: icon; text: text; icon\_text: icon and text
centerType: "search", //none: hidden; text: title; search: search box
rightType: "icon", //none: hidden; icon: icon; icon\_menu: icon and directory list
barVisibility: true, //true: visible; false: invisible
    center: {
text: "Title",
        languageKey: "title",
        textSize: "18",
searchTextHint: "Prompt text",
        searchLanguageKey: "search"
    },
    left: {
        text:"Back",
        languageKey: "back",
        textSize: "14",
icon: "", //Icon address. https://... If this parameter is left empty for the icon and icon\_text types, the default icon is displayed.
        iconSize: "30"
    },
    right: {
icon: "", //Icon address, https://...
        iconSize: "30",
menus: \["Function 1", "Function 2"\]
    },
    callBack: function(result){
       // result: '{"callBackType": "clickLeft", "menuItem": -1, "searchText": ""}'
       //callbackType: clickLeft: Click the left event. clickTitle: Click the title event. clickRight: Click the right event. clickRightMenu: Click the directory list event. search: Enter the text event in the search box.
       //menuItem: Subscript of the current directory position
       //searchText: Search for content based on the entered text.
    }
  }
  U.setNavigationBar(obj)