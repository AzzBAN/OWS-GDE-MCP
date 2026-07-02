---
title: "Suggestion: The Load Spark Sql Operator Preferentially Uses the Static Partition Loading Mode When the Partition Field Value Is Fixed"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001276469148.html"
depth: 6
---
# Suggestion: The Load Spark Sql Operator Preferentially Uses the Static Partition Loading Mode When the Partition Field Value Is Fixed

**Specification name**: General\_DataFactory\_Batch\_Preferentially\_Use\_Static\_Partitions

**Description**: The loading performance will be improved if the Load Spark Sql operator preferentially uses the static partition loading mode, when the value of the partition field is fixed before the current batch of data is loaded to the database after being calculated.

**Check guide**: Check the extraction criteria and calculation logic before data is imported to the database to check whether the value of the partition field is fixed. If it is, use the static partition loading mode.

**Positive example**:

1.  Select the static partition loading mode for the Load Spark Sql operator when the value of the partition field (scheduling batch time) of the Extract Spark Sql operator is a constant, as shown in the following figure.
    
    ![[en-us_image_0000001970810093.png]]
    
2.  Check that the value of the **stat\_date** field (scheduling batch) is fixed according to the configuration information for **Edit Filter Criteria** for the Extract Spark Sql operator.
    
    ![[en-us_image_0000001971145821.png]]
    
3.  Select the static partition loading mode when the value of the **STAT\_DATE** field (scheduling batch) in the uploaded target table is fixed.
    
    ![[en-us_image_0000001944108450.png]]
    

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]