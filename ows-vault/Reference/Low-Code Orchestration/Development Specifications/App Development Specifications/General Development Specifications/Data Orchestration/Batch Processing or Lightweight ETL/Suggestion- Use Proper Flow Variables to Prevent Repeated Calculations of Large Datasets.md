---
title: "Suggestion: Use Proper Flow Variables to Prevent Repeated Calculations of Large Datasets"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001276469152.html"
depth: 6
---
# Suggestion: Use Proper Flow Variables to Prevent Repeated Calculations of Large Datasets

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Prevent\_Double\_Counting

**Description**: If an orchestrated app contains expressions, flow-level broadcast variables need to be calculated using the Calculate operator for the control flow business in advance and then transferred to the data flow. In this way, the Transform operator does not perform the same expression logic calculation on each field, facilitating subsequent expression logic maintenance and saving computing resources during running.

**Check guide**: Check whether the operator for the data flow business contains redundant expressions.

**Positive example**:

1.  Move the complex logic (with the calculation result being a fixed value) of the Calculate operator for the data flow business forward to the logic of the Calculate operator for the control flow business. The output result can be directly referenced by the Transform operator for the data flow business. Do not use an expression whose calculation result is a fixed value when configuring the field of the Transform operator for the data flow business. The following figure shows an expression definition example that requires logic moving.
    
    ![[en-us_image_0000002043096097.png]]
    
2.  The Transform operator for the data flow business can reference the upstream expression calculation result.
    
    ![[en-us_image_0000002007056326.png]]
    

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]