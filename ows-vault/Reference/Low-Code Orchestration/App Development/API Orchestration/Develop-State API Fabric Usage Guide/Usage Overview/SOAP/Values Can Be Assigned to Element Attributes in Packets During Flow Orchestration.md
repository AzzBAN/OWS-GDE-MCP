---
title: "Values Can Be Assigned to Element Attributes in Packets During Flow Orchestration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662324776.html"
depth: 6
---
#### Example

The WSDL definition file of an API contains a **findCustomerOverviewByAddressResponse** element that defines the **OpType** attribute. The following figure shows the segment.

![[en-us_image_0000001621334296.png]]

During flow orchestration, you can assign a value to the **OpType** attribute during data mapping for northbound responses, as shown in the following figure.

![[en-us_image_0000001669628317.png]]

![[note_3.0-en-us.png]]

If direct mapping and value assignment do not meet requirements, you can compile a JavaScript script in the JavaScript editing box.

After the value is assigned, ensure that the value of the **OpType** attribute can be returned in the response, as shown in the following figure.

![[en-us_image_0000001621269832.png]]