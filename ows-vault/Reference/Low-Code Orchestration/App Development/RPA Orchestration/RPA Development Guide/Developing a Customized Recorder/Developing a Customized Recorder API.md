---
title: "Developing a Customized Recorder API"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001260723121.html"
depth: 5
---
#### Procedure

1.  Develop the following public APIs based on service requirements:
    
    -   API for obtaining the area where an element is located based on the mouse position
        -   Request: {"command":"getRect","_screenX_":100,"_screenY_":200}
            
            **Table 1** Request parameters  
            | Name | Description |
            | :-- | :-- |
            | screenX | Position of the cursor on the X axis relative to the upper left corner of the screen |
            | screenY | Position of the cursor on the Y axis relative to the upper left corner of the screen | -   Response: {"command":"getRect","x":100,"y":10,"width":100,"height":200}
    -   API for obtaining the element information based on the mouse position
        -   Request: {"command":"getElementInfo","_screenX_":100,"_screenY_":200}
            
            **Table 2** Request parameters  
            | Name | Description |
            | :-- | :-- |
            | screenX | Position of the cursor on the X axis relative to the upper left corner of the screen |
            | screenY | Position of the cursor on the Y axis relative to the upper left corner of the screen | -   Response: {"command":"getElementInfo","_target_":"{}","_editable_":true,"_selectTag_":true,"_selectItem_":\["1","2","3"\]}
            
            **Table 3** Response parameters  
            | Name | Description |
            | :-- | :-- |
            | target | Information about the obtained element. It is recommended that the information be returned in a JSON string. Command example: { "appName": "chrome.exe", "title": "Baidu, you know", "target": \[\] } |
            | editable | Whether the obtained element is a text box Currently, the text box is displayed in Studio and is left blank on the app page.
            -   **true**: Yes
            -   **false**: No
            
             |
            | selectTag | Whether the obtained element is a single-choice drop-down list box
            
            -   **true**: Yes
            -   **false**: No
            
             |
            | selectItem | Options in the drop-down list box of the obtained element This parameter is valid only when selectTag is set to true. | 2.  Develop the following APIs related to the recording function based on service requirements:
    
    -   API for starting recording
        -   Request: {"command":"START\_RECORD"}
        -   Response: none
    -   API for stopping recording
        -   Request: {"command":"STOP\_RECORD"}
        -   Response: none
    -   Enter the value API in the element.
        -   Request: {"command":"type","_screenX_":100,"_screenY_":200,"_value_":"Entered value","_clear_":true/false}
            
            **Table 4** Request parameters  
            | Name | Description |
            | :-- | :-- |
            | screenX | Position of the cursor on the X axis relative to the upper left corner of the screen |
            | screenY | Position of the cursor on the Y axis relative to the upper left corner of the screen |
            | value | Value to be entered in the element |
            | clear | Whether to clear the original value before entering a new value
            -   **true**: Yes
            -   **false**: No
            
             | -   Response: none
    -   (Optional) API for selecting options from the drop-down list box
        -   Request {"command":"select","_screenX_":100,"_screenY_":200,"_index_":1}
            
            **Table 5** Request parameters  
            | Name | Description |
            | :-- | :-- |
            | screenX | Position of the cursor on the X axis relative to the upper left corner of the screen |
            | screenY | Position of the cursor on the Y axis relative to the upper left corner of the screen |
            | index | Index of an option in the drop-down list box | -   Response: none
    
3.  Develop the following APIs related to the pickup function based on service requirements:
    
    -   API for starting pickup
        -   Request: {"command":"startInspect","_itemName_":"Parameter name","_actionName_":"Command name","_driver\_type_":"extension"}
            
            **Table 6** Request parameters  
            | Name | Description |
            | :-- | :-- |
            | itemName | Parameter name of a command For example, the parameter name of the click command is target. |
            | actionName | Command name, for example, click, rightclick, and doubleclick |
            | driver\_type | driver\_type property of a command The default value of driver\_type is extension. | -   Response: none
    -   API for stopping pickup
        
        ![[notice_3.0-en-us.png]]
        
        You can use the cleanup function in the API for stopping pickup based on service requirements.
        
        -   Request: {"command":"stopInspect"}
        -   Response: none
    
4.  After the development is complete, use the customized recorder to record scripts in Studio and verify that the recording function is available.