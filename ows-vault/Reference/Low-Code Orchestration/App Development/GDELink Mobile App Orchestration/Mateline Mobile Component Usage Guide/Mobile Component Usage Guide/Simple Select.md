---
title: "Simple Select"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001780727221.html"
depth: 5
---
# Simple Select

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| ID | Component ID |
| Label | Component label |
| Output | Used to convert loaded data in the query service to display values in a drop-down list. Each option in a drop-down list has two field values: display value and hidden value. For example, {"text": "Label", "value": "Name", "parse\_expr": "results"} indicates that the label field returned by a service is converted to the display value in a drop-down list, and that the value of the name field is converted to the value in the drop-down list. parse\_expr indicates that the data in the results node of the service will be converted. If output is not configured, the default display value is the value of the text field; the hidden value is the value of the value field; and the default value of parse\_expr is results. |
| Parameters | Service request parameter, in JSON format |
| ParentSelectName | Name of the parent drop-down list of the child filter drop-down list |
| PlaceHolder | Default display value |
| Read Only | Whether the component is read-only. The value can be true or false. |
| Service ID | OWS service, which is generally the GetList service. |
| Value | Default |
| Visible | Whether the control is visible. A TQL expression is supported. You can determine whether to display the control based on the values of other controls. |
| Width | Component width |
| Required | Whether the component is mandatory | APIs

**isRequired**

Input parameters: none

Output parameter: **true** or **false**

Description: whether the control is mandatory

Example: C("simpleSelect").isRequired(); // **simpleSelect** indicates the component ID.

**addOptions**

Input parameter (options): a single object or array

Output parameters: none

Description: Options in the drop-down list are added.

Example:

// Add a single option.

C("simpleSelect").addOptions({"value":"test1","text":"Text Display Value1"});

// Add multiple options.

C("simpleSelect").addOptions(\[{"value":"test1","text":"Text Display Value1"},

{"value":"test2","text":"Text Display Value2"}\])

**clearOptions**

Input parameters: Boolean. The value can be **true** or **false** and these parameters are optional.

Output parameters: none

Description: whether a specified option in the drop-down list is cleared. A Boolean value is transferred and the default value is **false**.

Example:

C("simpleSelect").clearOptions();

**reload**

Input parameter: **params**, in JSON or Object format

Output parameters: none

Description: drop-down list for reloading service IDs applicable to a drop-down list. It does not apply to static data drop-down lists.

Example:

C("simpleSelect").reload({"testKey":"testValue"});

**setValue**

Input parameters: String

Output parameters: none

Description: A value is re-assigned to the drop-down list.

Example:

C("simpleSelect").setValue("test");

**setReadOnly**

Input parameters: Boolean. The value can be **true** or **false**.

Output parameters: none

Description: The drop-down list is set to read-only.

Example:

// Set the drop-down list to read-only.

C("simpleSelect").setReadOnly(true);

// Set the drop-down list to a selective drop-down list.

C("simpleSelect").setReadOnly(false);

Events

**valueChanged**

Description: event triggered when the value changes

Example:

C("id").on("valueChanged",function(){

console.log('aaa')

})

**change**

Description: event triggered when the value changes

Example:

C("id").on("change",function(json){

console.log(json.value)

})

Precautions

When both static options and services are configured, all the configured data is displayed in the drop-down list.

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]