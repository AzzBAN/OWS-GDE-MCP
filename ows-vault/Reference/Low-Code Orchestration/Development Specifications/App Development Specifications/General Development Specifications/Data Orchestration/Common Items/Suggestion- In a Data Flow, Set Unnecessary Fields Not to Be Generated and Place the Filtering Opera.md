---
title: "Suggestion: In a Data Flow, Set Unnecessary Fields Not to Be Generated and Place the Filtering Operator as Early as Possible to Reduce the Amount of Data to Be Processed and Improve Efficiency"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236784713.html"
depth: 6
---
# Suggestion: In a Data Flow, Set Unnecessary Fields Not to Be Generated and Place the Filtering Operator as Early as Possible to Reduce the Amount of Data to Be Processed and Improve Efficiency

**Specification name**: General\_DataFactory\_Common\_Orchestration\_Efficient

**Description**: During data processing, a larger volume of data consumes more time and more computing resources. During orchestration, you can filter unnecessary fields or data in the early stage of data processing to improve efficiency. For example, when configuring attributes of a data reading operator, set the fields that are not required in subsequent business processing not to be generated to reduce the data volume. If data needs to be filtered, place the filtering operator close to the start position to reduce the amount of data to be processed.

**Check guide**:

Based on business requirements, check whether any field is not processed or generated during data processing. If such a field exists, set the field not to be generated during data reading or in the early stage. In addition, check whether the filtering operator is placed close to the start position of the data flow. If not, move the operator close to the start position.

**Positive example**

![[en-us_image_0000002006633604.png]]

**Impact**: If unnecessary data is involved in the calculation, more computing resources are consumed and the calculation time is prolonged.

**Parent topic:** [[Common Items|Common Items]]