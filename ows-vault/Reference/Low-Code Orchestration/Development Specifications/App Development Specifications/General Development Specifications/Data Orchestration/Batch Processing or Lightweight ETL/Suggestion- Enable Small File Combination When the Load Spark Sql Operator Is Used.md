---
title: "Suggestion: Enable Small File Combination When the Load Spark Sql Operator Is Used"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001276629036.html"
depth: 6
---
# Suggestion: Enable Small File Combination When the Load Spark Sql Operator Is Used

**Specification name**: General\_DataFactory\_Batch\_Merging\_Small\_File\_Merge

**Description**: When the Load Spark Sql operator for batch processing is used in orchestration, you need to enable the small file combination function. You can use the file combination function of either the Carbon database or the Load Spark Sql operator for batch processing. Combining small files prevents a large number of files from being imported to the database. If a large number of small files are imported to the database, the HDFS performance, or extraction performance of downstream data may deteriorate.

**Check guide**: Check whether the Load Spark Sql operator is used. If yes, check the number of files to be imported to the database and enable the small file combination function. For details, see the related product documentation.

**Positive examples**:

-   In the develop-state environment, you can click ![[en-us_image_0000002043237237.png]] on the canvas toolbar, and set the flow parameter **hdi\_perpartition\_filenumber** by flow level to specify the number of files to be imported to the database.
    
    For example, when the default value of **hdi\_perpartition\_filenumber** is **500** and the Load Spark Sql operator is used, small files will be combined and 500 files in total will be generated.
    
    ![[en-us_image_0000002043122281.png]]
    
-   In the runtime state, you can choose **Products and Services** > **Data Cube** > **Data Processing** > **Big Data Integration** > **Flow Configuration**, right-click the target flow, choose **Edit Parameter** from the shortcut menu, and modify the target file number for file merging.
    
    ![[en-us_image_0000002006955292.png]]
    

**Version**: The small file combination function is supported in 23.0 or later.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]