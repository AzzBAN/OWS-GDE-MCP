---
title: "Assistant Panel"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001913146041.html"
depth: 5
---
#### Properties

![[en-us_image_0000001867267588.png]]

**Table 1** Basic properties  
| Name | Description |
| :-- | :-- |
| Id | Unique ID of a component, which is used to bind events and call APIs. |
| Size | Width and height of the component |
| Position | Position of the component in the canvas |
| Rotate | Rotation angle of the component |
| Position of the floating button | Position of a floating button in the canvas. After the component is collapsed, the floating button is displayed. | ![[en-us_image_0000001867267792.png]]

**Table 2** Common properties  
| Name | Description |
| :-- | :-- |
| Name | (Mandatory) Component name, which is the unique index in some scenarios. |
| Theme | Component theme. The skin can be changes in one-click mode. |
| Title | Component title |
| Font Style | Text style of the title |
| Request Config | Method of sending a request to the server after a dialog is sent. The configuration is the same as that of Request Config on the Body tab page. If the parameter is not configured, the request configuration under the common properties is used. | ![[en-us_image_0000001913714389.png]]

![[en-us_image_0000001867954986.png]]

**Table 3** Request Config  
| Name | Description |
| :-- | :-- |
| Custom Function | After the custom function is enabled, you need to compile the function for handling requests. |
| Request Function | JavaScript script, which is used to send requests to the foundation model and obtain replies. |
| Type | SSE and BASIC are supported. BASIC indicates ajax requests, and SSE indicates streaming requests. |
| URL | Request URL |
| Stream Type | Whether a streaming request is fully or partially returned when Type is set to SSE. |
| Pre Request Function | Callback function used before a request is sent. In most cases, this function is used to set parameters. |
| Success Function | Handling function after the request succeeds. However, if a service logic is taken over by a custom function, the system does not handle the returned logic any longer. |
| Error Function | Handling function after the request fails | ![[en-us_image_0000001913347225.png]]

**Table 4** Header  
| Name | Description |
| :-- | :-- |
| Height | Height of the header area |
| Background | Background of the header area Picture: allows users to set the background image for the element. Repeat: allows users to define the repetition mode of the background image. The background image may be repeated along the horizontal axis and/or the vertical axis, or not be repeated at all. Color: allows users to set the background color of the element. Size: allows users to set the background image size. You can retain its original image size, stretch to a new size, or scale to the size of the available space of the element while retaining its original scale. Position: allows users to set the initial position of the background image. |
| Actions Config | Definitions on the operation buttons in the upper right corner History Record: Displays chat records, and allows users to edit, delete, and resend the records. System Settings: indicates a system configuration button, which is used to configure whether to display the profile and the command display mode. HTML Panel: indicates a common component, which is used to customize content. For details about the configuration items, see the HTML panel component of the system. Button: indicates a common component, which is used to configure common buttons with click events. Dropdown Select: indicates a common component that supports custom drop-down options. Copilot Select: has similar functions as the drop-down list. Images can be configured. | ![[en-us_image_0000001867427900.png]]

**Table 5** History Record  
| Name | Description |
| :-- | :-- |
| Visible Condition | Whether the button is visible and the visibility conditions by returning true or false in the function. |
| List Query Function | Request function for querying historical records. If this parameter is not set, the default handling logic is used. |
| Update Function | Function for updating historical records. If this parameter is not set, the default handling logic is used. |
| Delete Function | Function for deleting historical records. If this parameter is not set, the default handling logic is used. |
| Save Function | Function for saving historical records. If this parameter is not set, the default handling logic is used. |
| Query Detail Function | Function for querying a single historical record. If this parameter is not set, the default handling logic is used. | ![[en-us_image_0000001867268152.png]]

**Table 6** Buttons  
| Name | Description |
| :-- | :-- |
| Click Handler | Handling logic after a button is clicked |
| Visible Condition | Whether the button is visible and the visibility conditions by returning true or false in the function | ![[en-us_image_0000001913467745.png]]

**Table 7** Body  
| Name | Description |
| :-- | :-- |
| Tabs Config | Content on the tab. Multiple tabs need to be configured. When there is only one tab, the tab is not displayed on the top. |
| Tabs Style | Display style of the tab in the normal or activated state | ![[en-us_image_0000001867268196.png]]

**Table 8** Tab configuration  
| Name | Description |
| :-- | :-- |
| Name | (Mandatory) Tab name |
| Title | Tab title |
| Activate | Whether the current tab is activated. Only one activated tab is allowed in the multi-tab scenario. |
| Guide Configuration | Content in the wizard area which is displayed when there is no dialog in the dialog box. |
| Message Header Config | Custom function. The returned content is displayed as the message title. |
| Message Content Config | Prefix and suffix of the message |
| User Meta Config | User profile information |
| Assistant Meta Config | Assistant profile information |
| Actions Config | Shortcut buttons after a dialog is returned |
| Input Config | Placeholder, operation button, and input prompt information of the input box |
| Request Config | Method of sending a request to the server after a dialog is sent. The configuration is the same as that of Request Config on the tab page. If the parameter is not configured, the request configuration under the common properties is used. |