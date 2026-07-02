---
title: "Suggestion: When the Route Operator Has More Than Three Filter Criteria (Output Branches), Move the Filter Criteria of the Route Operator Forward to Filter Criteria of the Extract Operator"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001327229017.html"
depth: 6
---
# Suggestion: When the Route Operator Has More Than Three Filter Criteria (Output Branches), Move the Filter Criteria of the Route Operator Forward to Filter Criteria of the Extract Operator

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Presetting\_Routing\_Conditions

**Description**: When multiple outputs (more than three) are generated for one input from the Extract operator after processing using a Route operator, and aggregation and computing are performed on each output, computing performance deteriorates significantly. In this case, you need to move filter criteria of the Route operator forward to filter criteria of the Extract operator to improve computing performance.

**Check guide**: Check whether a Route operator has multiple outputs during flow orchestration. If yes, you are advised to optimize the flow, that is, multiple outputs are generated for Extract operators.

**Positive example**:

When there is one input from an Extract Spark Sql operator, three outputs are generated after processing using a Route operator, and aggregation and computing are performed on each output, leading to poor overall computing performance. You can optimize the flow, that is, move the filter criteria of the Route operator forward to the filter criteria of the Extract Spark Sql operator to generate three inputs.

-   The following figure shows the orchestration flow before the optimization.
    
    ![[en-us_image_0000001276949812.png]]
    
-   The following figure shows the orchestration flow after the optimization.
    
    ![[en-us_image_0000001276629900.png]]
    

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]