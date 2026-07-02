---
title: "Values in the SingleSelect Component Are Occasionally Left Empty During Initialization Because the event Component Assigns a Value to the SingleSelect Component in a Form"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500876.html"
depth: 3
---
# Values in the SingleSelect Component Are Occasionally Left Empty During Initialization Because the event Component Assigns a Value to the SingleSelect Component in a Form

The following uses the SingleSelect component (**id** and **name** uses the same attribute: **motype\_id**) as an example. The reason is that, in the versions using VUE, the actions to assign a value to **motype\_id** (of the SingleSelect Component) are asynchronous. Assigning values to the attribute in the form after loadformdata is loaded and assigning values to the attribute by the event component, which is component to perform the value setting action (that is, assigning an empty value), are asynchronous. The rectification method is to re-assign a value to the SingleSelect component in the callback function of the LoadDataFinished event in the table data loading component.

In the VUE versions, the following code needs to be added to the JS component:

Spl.EventBus.register("xxloadDataid',"LoadDataFinished",function(param){
   S("motype\_id").setValue(param.data\["motype\_id"\])
 })
 //Note: motype\_id in S("motype\_id") is the ID of the SingleSelect component.
 // motype\_id in param.data\["motype\_id"\] is the name attribute of the SingleSelect component.
 //Note: If the value of another component is used in the parameter attribute of the SingleSelect component, for example, domain\_id:"#Page\[domain\_id\]", the load method is required. Otherwise, the value of domain\_id may not be obtained due to asynchronization.
 Spl.EventBus.register("xxloadDataid',"LoadDataFinished",function(param){
  S("motype\_id").load({domain\_id:"#Page\[domain\_id\]"},param.data.result\["motype\_id"\])
 })

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]