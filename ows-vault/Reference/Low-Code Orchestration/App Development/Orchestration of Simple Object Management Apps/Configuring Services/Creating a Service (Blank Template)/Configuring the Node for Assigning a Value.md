---
title: "Configuring the Node for Assigning a Value"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_036.html"
depth: 5
---
#### Context

The assign node is used to define global variables and assign values to the variables in complex services involving multiple nodes. After a global variable is defined, it is stored in the context and can be used on other nodes.

For example, in a service, you need to define global variables g\_a and g\_b using the assign node and assign the values of **name** and **score** of the previous node to the global variables.

In addition, after other node operations are performed, the values of the global variables g\_a and g\_b are used as the input of the model parameters **m\_name** and **m\_value** on the create node.

**Figure 1** Configuration example  
![[en-us_image_0000001234074917.png]]

The following describes how to configure the start, assign, and create nodes.