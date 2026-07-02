---
title: "Steps"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001781156217.html"
depth: 5
---
# Steps

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| Parameters | Service input parameter |
| Service Id | Return data required for dynamically generating nodes |
| Show Number | Whether to display the sequence number |
| width | Component width. Enter a number ranging from 1 to 10000. | **APIs**

**setStatusByIndex**

Input parameter: **index status**

Output parameters: none

Description: Set the node status based on the node index.

Example:

C("step1").setStatusByIndex(4,"succeed");

**setStatusByLabel**

Input parameter: **label status**

Output parameters: none

Description: Set the node status based on the node label.

Example:

C("step1").setStatusByLabel("label1","succeed");

**loadData**

Input parameters: **serviceId** and **parameters**

Output parameters: none

Description: Reload the data rendering node.

Example:

C("step1").setStatusByLabel("renderSteps",{});

**Events**

**click**

Description: click event. The input parameters are the configuration of the clicked node.

Example:

Spl.EventBus.register("id","click",function(params){

//do something

})

**FAQs**

Scenarios

1\. Use this component with its sub component stepsNode to configure a flowchart.

**Precautions**

N/A

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]