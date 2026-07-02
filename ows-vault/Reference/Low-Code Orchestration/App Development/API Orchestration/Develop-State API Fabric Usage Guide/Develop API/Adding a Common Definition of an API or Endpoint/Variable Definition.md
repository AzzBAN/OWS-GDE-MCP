---
title: "Variable Definition"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_148.html"
depth: 6
---
#### Usage Scenarios

1.  When adding a southbound service, you can use **${**_Variable name_**}** to reference a variable, as shown in [Figure 1](#EN-US_TOPIC_0000001568986681__en-us_topic_0122468779_fig744812414467).
    
    The defined variable is **cbs.server**.
    
    **Figure 1** Referencing a variable when adding an endpoint  
    ![[en-us_image_0313137848.png]]
    
2.  Use **apigw.getProperty('**_{Variable name}_**')** in the JavaScript of **Process orchestration** to obtain the variable value.
    
    [Figure 2](#EN-US_TOPIC_0000001568986681__en-us_topic_0122468779_fig1493762314524) shows an example. The tool supports association. Enter the first letter of the variable in the JavaScript, as shown in [Figure 3](#EN-US_TOPIC_0000001568986681__en-us_topic_0122468779_fig13923151145615).
    
    **Figure 2** Referencing the variable in the JavaScript  
    ![[en-us_image_0122468825.png]]
    
    **Figure 3** Associating the variable name in the JavaScript  
    ![[en-us_image_0122468880.png]]