---
title: "Arrays in Different Dimensions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_089.html"
depth: 6
---
#### Processing Rules

The rules for JS script processing are as follows for the arrays in different dimensions and in different mapping scenarios:

1.  Root element Y is mapped to Z, as shown in [Figure 1](#EN-US_TOPIC_0000001538778433__en-us_topic_0129536987_fig21355191290). The tool generates the following code:
    
    Z = X\[0\].Y
    
    **Figure 1** Mapping root element Y to Z  
    ![[en-us_image_0240797223.png]]
    
2.  Sub-element Y is mapped to sub-element Z, as shown in [Figure 2](#EN-US_TOPIC_0000001538778433__en-us_topic_0129536987_fig584674812146). The tool generates the following code:
    
    Z\[0\].e = X\[0\].Y\[0\].a 
    Z\[0\].f =  X\[0\].Y\[0\].b
    
    **Figure 2** Mapping sub-element Y to sub-element Z  
    ![[en-us_image_0240797773.png]]
    
3.  Assign values on the root element and sub-element, as shown in [Figure 3](#EN-US_TOPIC_0000001538778433__en-us_topic_0129536987_fig4347146111713). The tool assigns values on the array objects.
    
    For(int i=0;i<Y.length;i++){
         Z\[i\].e = X\[0\].Y\[i\].a;
         Z\[i\].f = X\[0\].Y\[i\].b;
    }
    
    **Figure 3** Assigning values on both the root element and sub-element in different dimensions  
    ![[en-us_image_0240798830.png]]
    
    The priorities of the value in the **Js Editor** window and of the intermediate code generated in data mapping are the same as those in [[Array in the Same Dimension|Array in the Same Dimension]].