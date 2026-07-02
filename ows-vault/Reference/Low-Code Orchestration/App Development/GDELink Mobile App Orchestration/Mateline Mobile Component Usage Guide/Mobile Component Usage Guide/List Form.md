---
title: "List Form"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001781247997.html"
depth: 5
---
# List Form

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Allow Row Delete | If this parameter is set to true, the Delete button is available for deleting fields. |
| Initial Row Count | Number of rows to be rendered initially |
| Max Row Count | Maximum number of rows that can be rendered | **APIs**

**removeAt**

Input parameter: **index**

Output parameters: none

Description: Delete the field in the specified position in List Form. The form view template is used as a basic unit.

Example:

C("listform").removeAt(0)// Delete the first form view template.

**clear**

Input parameters: none

Output parameters: none

Description: Clear all fields in List Form.

Example:

C("listform").clear()

**addRow**

Input parameters: an array, JSON string, or blank

Output parameters: none

Description: Add a line to List Form and set a value.

Example:

C("listform").addRow({la:"A",lb:"B"})

// Add a line and set the value.

C("listform").addRow(\[{la:"A",lb:"B"},{la:"C",lb:"D"}\])

// Add two lines and set the value.

C("listform").addRow()

// Add a blank line.

**setValue**

Input parameters: JSON

Output parameters: none

Description: Set the value of List Form.

Example:

C("listform").setValue({la:"A",lb:"B"})

// Clear the line, add a new line, and set a value.

**getValue**

Input parameters: none

Output parameters: JSON

Description: Obtain the value.

Example:

C("listform").getValue()

**hide**

Description: Hide a component.

**show**

Description: Show a component.

**Events**

**dataLoaded**

Description: The event is triggered after data loading is complete.

Example:

C("id").on("dataLoaded",function(json){

//do something

})

**RowAdded**

Description: The event is triggered after a row is added.

Example:

C("id").on("RowAdded",function(index,row){

//do something

})

**FAQs**

Scenarios

1\. Dynamically obtain form data through services.

2\. Reload form data.

3\. Listen to the loading completion event of the form data and execute the custom method after the form loading is complete.

**Precautions**

This component is used with the form view template. Data fields can be configured in the form view template. A form template occupies a line.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]