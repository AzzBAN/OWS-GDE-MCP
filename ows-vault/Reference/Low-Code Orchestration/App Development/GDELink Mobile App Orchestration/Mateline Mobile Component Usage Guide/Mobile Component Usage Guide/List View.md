---
title: "List View"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778803385.html"
depth: 5
---
# List View

**Properties**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000001778803385__table4328mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:20%"> <col style="width:80%"></colgroup><tbody><tr id="EN-US_TOPIC_0000001778803385__row4333mcpsimp"><td class="cellrowborder" valign="top" width="20%">Property Name</td><td class="cellrowborder" valign="top" width="80%">Description</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4338mcpsimp"><td class="cellrowborder" valign="top" width="20%">Aggregation Title</td><td class="cellrowborder" valign="top" width="80%">List View can classify data of the same type into one category and display the data together. It allows users to configure the title of this type of data, that is, the aggregation title. The format is "#Row[xx]".</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4343mcpsimp"><td class="cellrowborder" valign="top" width="20%">Aside Field</td><td class="cellrowborder" valign="top" width="80%">Side title field</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4348mcpsimp"><td class="cellrowborder" valign="top" width="20%">Can Use When Offline</td><td class="cellrowborder" valign="top" width="80%">Whether the component is available in offline mode</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4353mcpsimp"><td class="cellrowborder" valign="top" width="20%">Config Aggregation</td><td class="cellrowborder" valign="top" width="80%">Fields by which data is aggregated. For example, if this property is set to task_id, task_type, all data with the same task_id and task_type is aggregated into a category.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4358mcpsimp"><td class="cellrowborder" valign="top" width="20%">Custom Row Template</td><td class="cellrowborder" valign="top" width="80%">Custom list display content. Use {{row.xx}} to obtain service data. After a custom template is configured, content is displayed firstly based on the template, and the header field and other configuration items become invalid.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4363mcpsimp"><td class="cellrowborder" valign="top" width="20%">Empty Message</td><td class="cellrowborder" valign="top" width="80%">Default content to be displayed when there is no data.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4368mcpsimp"><td class="cellrowborder" valign="top" width="20%">Header Field</td><td class="cellrowborder" valign="top" width="80%">Field of a service that is used as the title</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4373mcpsimp"><td class="cellrowborder" valign="top" width="20%">Id</td><td class="cellrowborder" valign="top" width="80%">Component ID</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4378mcpsimp"><td class="cellrowborder" valign="top" width="20%">Ignore Item Page History</td><td class="cellrowborder" valign="top" width="80%">Whether to record the history when a user clicks a list item</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4383mcpsimp"><td class="cellrowborder" valign="top" width="20%">Image Field</td><td class="cellrowborder" valign="top" width="80%">Field returned by the service, which is used as the image path.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4388mcpsimp"><td class="cellrowborder" valign="top" width="20%">Item Identify Field</td><td class="cellrowborder" valign="top" width="80%">Field returned by the service, which is used as the unique identifier of the data record.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4393mcpsimp"><td class="cellrowborder" valign="top" width="20%">Item Url Field</td><td class="cellrowborder" valign="top" width="80%">Redirection link</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4398mcpsimp"><td class="cellrowborder" valign="top" width="20%">Link Parameters</td><td class="cellrowborder" valign="top" width="80%">Parameter transferred during redirection</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4403mcpsimp"><td class="cellrowborder" valign="top" width="20%">Location</td><td class="cellrowborder" valign="top" width="80%">Page to be redirected to. This property has a higher priority than url.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4408mcpsimp"><td class="cellrowborder" valign="top" width="20%">Page Size</td><td class="cellrowborder" valign="top" width="80%">Page size, that is, number of data records to be loaded each time.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4413mcpsimp"><td class="cellrowborder" valign="top" width="20%">Searchable</td><td class="cellrowborder" valign="top" width="80%">Whether the list is searchable. If the property is set to true, the search box is displayed above the list. You are advised to configure the filter item, which is more powerful than the search function.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4418mcpsimp"><td class="cellrowborder" valign="top" width="20%">Search Field</td><td class="cellrowborder" valign="top" width="80%">Field to be used for searching. This property can be used together with Searchable.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4423mcpsimp"><td class="cellrowborder" valign="top" width="20%">Search PlaceHolder</td><td class="cellrowborder" valign="top" width="80%">Placeholder in the search box</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4428mcpsimp"><td class="cellrowborder" valign="top" width="20%">Service Id</td><td class="cellrowborder" valign="top" width="80%">List data source</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4433mcpsimp"><td class="cellrowborder" valign="top" width="20%">Service Parameters</td><td class="cellrowborder" valign="top" width="80%">Parameters required for obtaining list data</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4438mcpsimp"><td class="cellrowborder" valign="top" width="20%">Summary Field</td><td class="cellrowborder" valign="top" width="80%">List content field, which is displayed under the title.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row4443mcpsimp"><td class="cellrowborder" valign="top" width="20%">Support Multiple Select</td><td class="cellrowborder" valign="top" width="80%">Whether multiple options can be selected in the list. If this property is set to true, multiple options can be selected but this function is available only when the current page contains only the List View component.</td></tr><tr id="EN-US_TOPIC_0000001778803385__row14091233133410"><td class="cellrowborder" valign="top" width="20%">url</td><td class="cellrowborder" valign="top" width="80%">Redirection URL. After a URL is configured, redirection is executed when a list item is clicked.</td></tr></tbody></table>

**APIs**

**deleteRow**

Input parameters: Number

Output parameters: none

Description: Delete the _N_th line of the list, and the value of _N_ starts from 0.

Example:

C("ComId").deleteRow(1); // **ComId** indicates the component ID.

**hide**

Input parameters: none

Output parameters: none

Description: Hide the list.

Example:

C("ComId").hide(); // **ComId** indicates the component ID.

**show**

Input parameters: none

Output parameters: none

Description: Show the list.

Example:

C("ComId").show(); // **ComId** indicates the component ID.

**refresh**

Input parameters: none

Output parameters: none

Description: Refresh the list.

Example:

C("ComId").refresh(); // **ComId** indicates the component ID.

**reloadFromCache**

Input parameters: Array

Output parameters: none

Description: Refresh the list based on the data transferred from the input parameters.

Example:

C("ComId").reloadFromCache(\[{task\_id:"0001",task\_type:"CM"},{..}, ...\]); // **ComId** indicates the component ID.

**destroy**

Input parameters: none

Output parameters: none

Description: Destroy a component.

Example:

C("ComId").destroy(); // **ComId** indicates the component ID.

**stick**

Input parameters: String:ItemIdField

Output parameters: none

Description: Perform the pinning operation based on the transferred flag bit.

Example:

C("ComId").stick("0001"); // **ComId** indicates the component ID.

**unStick**

Input parameters: String:ItemIdField

Output parameters: none

Description: Perform the unpinning operation based on the transferred flag bit.

Example:

C("ComId").unStick("0001"); // **ComId** indicates the component ID.

**openMultiSelectMode**

Input parameters: none

Output parameters: none

Description: Enter the multi-selection mode.

Example:

C("ComId").openMultiSelectMode(); // **ComId** indicates the component ID.

**closeMultiSelectMode**

Input parameters: none

Output parameters: none

Description: Exit the multi-selection mode.

Example:

C("ComId").closeMultiSelectMode(); // **ComId** indicates the component ID.

**getSelectedItems**

Input parameters: none

Output parameters: Array

Description: In multi-selection mode, obtain the selected data.

Example:

C("ComId").getSelectedItems(); // **ComId** indicates the component ID.

**Events**

**dataLoaded**

Description: The event is triggered after data loading is complete.

Example:

C("id").on("dataLoaded",function(json){

//do something

})

**itemClick**

Description: This event is triggered when a row is clicked.

Example:

C("id").on("itemClick",function(row){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]