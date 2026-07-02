---
title: "Suggestion: Enable the Batch Interface for the Load JDBC Operator of the Batch Processing or Lightweight ETL Flow to Improve Data Loading Performance"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001838180545.html"
depth: 6
---
# Suggestion: Enable the Batch Interface for the Load JDBC Operator of the Batch Processing or Lightweight ETL Flow to Improve Data Loading Performance

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Preferentially\_Use\_Batch\_Interface

**Description**: If a flow contains a Load JDBC operator, you are advised to enable the batch interface to improve the performance of loading data to the database.

**Check guide**: Check whether the flow contains a Load JDBC operator. If yes, check whether the batch interface is enabled for the operator. If it is not, enable it.

**Positive example**:

-   Flows and the Load JDBC operator before optimization
    
    Flow description: In the control flow, the Calculate operator calculates data to obtain multiple time ranges. In the data flow, the Extract JDBC operator searches for data that meets the conditions based on the obtained time ranges, and the Load JDBC operator loads the data to another table. **Data Loading Mode** of Load JDBC is set to **Update Or Insert**. The settings of all data flows are the same except that the extraction conditions are different.
    
    **Figure 1** Control flow (before optimization)  
    ![[en-us_image_0000001838195121.png]]
    
    **Figure 2** Data flow (before optimization)  
    ![[en-us_image_0000001838390413.png]]
    
    **Figure 3** Load JDBC (before optimization)  
    ![[en-us_image_0000001838356605.png]]
    
-   Flows and the Load JDBC operator after optimization
    
    Flow description:
    
    -   Multiple Data Flow operators that are executed in serial mode in the control flow are integrated into one Data Flow operator.
    -   In the data flow, multiple Extract JDBC operators concurrently extract data, the Union operator integrates all data, and the Deduplicate operator deduplicates the data to be loaded to the database based on the primary key.
    -   For the Load JDBC operator, **Data Loading Mode** is set to **Replace** and **Use Batch Interface** is set to **Enable** during batch data loading, improving flow execution performance.
    
    **Figure 4** Control flow (after optimization)  
    ![[en-us_image_0000001838357909.png]]
    
    **Figure 5** Data flow (after optimization)  
    ![[en-us_image_0000001791439428.png]]
    
    **Figure 6** Load JDBC (after optimization)  
    ![[en-us_image_0000001791440004.png]]
    

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]