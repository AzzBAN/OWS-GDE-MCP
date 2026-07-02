---
title: "Suggestion: When Data Skew Occurs During Aggregation and Sum Calculations Using the Group Operator for Batch Processing, Discretize Group Keys for Pre-grouping to Reduce the Impact of Data Skew"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001327229009.html"
depth: 6
---
# Suggestion: When Data Skew Occurs During Aggregation and Sum Calculations Using the Group Operator for Batch Processing, Discretize Group Keys for Pre-grouping to Reduce the Impact of Data Skew

**Specification name**: General\_DataFactory\_Batch\_LightETL\_GroupBy\_Data\_Skew.

**Description**: When configuring business orchestration logic, you need to ensure that group fields are evenly distributed during aggregation and sum calculations using the Group operator. For example, a large number of empty values or same constants are not allowed. If such a problem occurs, you can discretize group keys for pre-grouping and perform aggregation and sum calculations.

**Check guide**: Check the logic of upstream and downstream businesses for uneven distribution of group keys.

**Positive example**:

1.  If group keys are skewed, the Group operator is split into two Group operators. The first one is used to discretize group keys and perform pre-aggregation, and the second one is used for final aggregation.
    
    ![[en-us_image_0000002042866225.png]]
    
2.  Define the discrete value of the group key for the Transform operator.
    
    ![[en-us_image_0000002006957952.png]]
    
3.  Configure the group key of the first Group operator used for pre-aggregation, as shown in the following figure.
    
    ![[en-us_image_0000002008980466.png]]
    

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]