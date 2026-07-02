---
title: "Suggestion: Set the Output Field on the Columns Tab Page When Extracting Some Fields from Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001327188813.html"
depth: 6
---
# Suggestion: Set the Output Field on the Columns Tab Page When Extracting Some Fields from Data

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Filtering\_Some\_Fields

**Description**: The Extract operator can extract some fields. To filter some fields, you can set the **Output** field on the **Columns** tab page of the Extract operator. This method helps to save computing resources. Do not use the Extract and Transform operators to filter all fields.

**Check guide**: Check for redundant Transform operators.

**Positive example**: The Transform operator in the red box shown in the following figure can filter some fields. You can move the filter criteria for outputting some fields of the Transform operator forward to the filter criteria of the Extract operator.

**Figure 1** Flow before optimization  
![[en-us_image_0000001276629876.png]]

**Figure 2** Flow after optimization  
![[en-us_image_0000001645223254.png]]

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]