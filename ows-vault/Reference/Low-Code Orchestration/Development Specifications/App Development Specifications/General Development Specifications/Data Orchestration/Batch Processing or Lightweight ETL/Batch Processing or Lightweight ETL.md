---
title: "Batch Processing or Lightweight ETL"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001191984780.html"
depth: 5
children: ["Rule: External Stored Procedures Called by the Stored Procedure Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Trustworthy", "Rule: Loop of the Startloop Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Terminable", "Rule: The Dependency Operator in a Batch Processing or Lightweight ETL Control Flow Must Avoid Cyclic Dependency", "Rule: Data Cleanup Must Be Considered During Data Orchestration to Avoid Duplicate Data in the Same Batch Due to Repeated Execution", "Rule - Batch Processing and Lightweight ETL Tasks Should Not Run in the Same Queue as BFS-Spark Aggregation and Computing Tasks", "Suggestion: To Save Costs, Use Lightweight ETL Operators to Process Less than 10 Million Records in Batches", "Suggestion: The Load Spark Sql Operator Preferentially Uses the Static Partition Loading Mode When the Partition Field Value Is Fixed", "Suggestion: Ensure that Group and Connection Keys of Group and Connection Operators for Batch Processing Are Evenly Distributed When Configuring Upstream Data Processing Logic of Businesses, Preventing Task Running Failures Caused by Data Skew", "Suggestion: When Data Skew Occurs During Aggregation and Sum Calculations Using the Group Operator for Batch Processing, Discretize Group Keys for Pre-grouping to Reduce the Impact of Data Skew", "Suggestion: Inject SQL Statements with the Same Logic in the Control Flow to Reduce the Impact of Data Skew When Group Keys of the Group Operator for Batch Processing Are Not Evenly Distributed During the Aggregation and Computing", "Suggestion: When Data Skew Occurs and Multiple Connection Operators Are Used to Associate and Combine Multiple Tables to Generate a Big Table, Use Union and Group Operators to Orchestrate Data to Reduce the Impact of Data Skew", "Suggestion: Set the Output Field on the Columns Tab Page When Extracting Some Fields from Data", "Suggestion: Enable Small File Combination When the Load Spark Sql Operator Is Used", "Suggestion: Do Not Use Multiple Transform Operators of Batch Processing or Lightweight ETL in Series to Process Fields", "Suggestion: Use Proper Flow Variables to Prevent Repeated Calculations of Large Datasets", "Suggestion: Plan an Independent YARN Resource Pool When Hadoop Is Shared by Data Cube and Other Systems (GTS Product Convergence Solution)", "Suggestion: When the Route Operator Has More Than Three Filter Criteria (Output Branches), Move the Filter Criteria of the Route Operator Forward to Filter Criteria of the Extract Operator", "Suggestion: Enable the Batch Interface for the Load JDBC Operator of the Batch Processing or Lightweight ETL Flow to Improve Data Loading Performance"]
---
# Batch Processing or Lightweight ETL

This section describes the rules and suggestions that should be followed during orchestration of batch processing and lightweight ETL flows. You can refer to the specifications and configure flows based on site requirements.

-   **[[Rule- External Stored Procedures Called by the Stored Procedure Operator in a Batch Processing or Li|Rule: External Stored Procedures Called by the Stored Procedure Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Trustworthy]]**  
    
-   **[[Rule- Loop of the Startloop Operator in a Batch Processing or Lightweight ETL Control Flow Must Be T|Rule: Loop of the Startloop Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Terminable]]**  
    
-   **[[Rule- The Dependency Operator in a Batch Processing or Lightweight ETL Control Flow Must Avoid Cycli|Rule: The Dependency Operator in a Batch Processing or Lightweight ETL Control Flow Must Avoid Cyclic Dependency]]**  
    
-   **[[Rule- Data Cleanup Must Be Considered During Data Orchestration to Avoid Duplicate Data in the Same |Rule: Data Cleanup Must Be Considered During Data Orchestration to Avoid Duplicate Data in the Same Batch Due to Repeated Execution]]**  
    
-   **[[Rule - Batch Processing and Lightweight ETL Tasks Should Not Run in the Same Queue as BFS-Spark Aggr|Rule - Batch Processing and Lightweight ETL Tasks Should Not Run in the Same Queue as BFS-Spark Aggregation and Computing Tasks]]**  
    
-   **[[Suggestion- To Save Costs, Use Lightweight ETL Operators to Process Less than 10 Million Records in |Suggestion: To Save Costs, Use Lightweight ETL Operators to Process Less than 10 Million Records in Batches]]**  
    
-   **[[Suggestion- The Load Spark Sql Operator Preferentially Uses the Static Partition Loading Mode When t|Suggestion: The Load Spark Sql Operator Preferentially Uses the Static Partition Loading Mode When the Partition Field Value Is Fixed]]**  
    
-   **[[Suggestion- Ensure that Group and Connection Keys of Group and Connection Operators for Batch Proces|Suggestion: Ensure that Group and Connection Keys of Group and Connection Operators for Batch Processing Are Evenly Distributed When Configuring Upstream Data Processing Logic of Businesses, Preventing Task Running Failures Caused by Data Skew]]**  
    
-   **[[Suggestion- When Data Skew Occurs During Aggregation and Sum Calculations Using the Group Operator f|Suggestion: When Data Skew Occurs During Aggregation and Sum Calculations Using the Group Operator for Batch Processing, Discretize Group Keys for Pre-grouping to Reduce the Impact of Data Skew]]**  
    
-   **[[Suggestion- Inject SQL Statements with the Same Logic in the Control Flow to Reduce the Impact of Da|Suggestion: Inject SQL Statements with the Same Logic in the Control Flow to Reduce the Impact of Data Skew When Group Keys of the Group Operator for Batch Processing Are Not Evenly Distributed During the Aggregation and Computing]]**  
    
-   **[[Suggestion- When Data Skew Occurs and Multiple Connection Operators Are Used to Associate and Combin|Suggestion: When Data Skew Occurs and Multiple Connection Operators Are Used to Associate and Combine Multiple Tables to Generate a Big Table, Use Union and Group Operators to Orchestrate Data to Reduce the Impact of Data Skew]]**  
    
-   **[[Suggestion- Set the Output Field on the Columns Tab Page When Extracting Some Fields from Data|Suggestion: Set the Output Field on the Columns Tab Page When Extracting Some Fields from Data]]**  
    
-   **[[Suggestion- Enable Small File Combination When the Load Spark Sql Operator Is Used|Suggestion: Enable Small File Combination When the Load Spark Sql Operator Is Used]]**  
    
-   **[[Suggestion- Do Not Use Multiple Transform Operators of Batch Processing or Lightweight ETL in Series|Suggestion: Do Not Use Multiple Transform Operators of Batch Processing or Lightweight ETL in Series to Process Fields]]**  
    
-   **[[Suggestion- Use Proper Flow Variables to Prevent Repeated Calculations of Large Datasets|Suggestion: Use Proper Flow Variables to Prevent Repeated Calculations of Large Datasets]]**  
    
-   **[[Suggestion- Plan an Independent YARN Resource Pool When Hadoop Is Shared by Data Cube and Other Syst|Suggestion: Plan an Independent YARN Resource Pool When Hadoop Is Shared by Data Cube and Other Systems (GTS Product Convergence Solution)]]**  
    
-   **[[Suggestion- When the Route Operator Has More Than Three Filter Criteria (Output Branches), Move the |Suggestion: When the Route Operator Has More Than Three Filter Criteria (Output Branches), Move the Filter Criteria of the Route Operator Forward to Filter Criteria of the Extract Operator]]**  
    
-   **[[Suggestion- Enable the Batch Interface for the Load JDBC Operator of the Batch Processing or Lightwe|Suggestion: Enable the Batch Interface for the Load JDBC Operator of the Batch Processing or Lightweight ETL Flow to Improve Data Loading Performance]]**  
    

**Parent topic:** [[Data Orchestration|Data Orchestration]]

## Sub-topics

- [[Rule- External Stored Procedures Called by the Stored Procedure Operator in a Batch Processing or Li]]
- [[Rule- Loop of the Startloop Operator in a Batch Processing or Lightweight ETL Control Flow Must Be T]]
- [[Rule- The Dependency Operator in a Batch Processing or Lightweight ETL Control Flow Must Avoid Cycli]]
- [[Rule- Data Cleanup Must Be Considered During Data Orchestration to Avoid Duplicate Data in the Same ]]
- [[Rule - Batch Processing and Lightweight ETL Tasks Should Not Run in the Same Queue as BFS-Spark Aggr]]
- [[Suggestion- To Save Costs, Use Lightweight ETL Operators to Process Less than 10 Million Records in ]]
- [[Suggestion- The Load Spark Sql Operator Preferentially Uses the Static Partition Loading Mode When t]]
- [[Suggestion- Ensure that Group and Connection Keys of Group and Connection Operators for Batch Proces]]
- [[Suggestion- When Data Skew Occurs During Aggregation and Sum Calculations Using the Group Operator f]]
- [[Suggestion- Inject SQL Statements with the Same Logic in the Control Flow to Reduce the Impact of Da]]
- [[Suggestion- When Data Skew Occurs and Multiple Connection Operators Are Used to Associate and Combin]]
- [[Suggestion- Set the Output Field on the Columns Tab Page When Extracting Some Fields from Data]]
- [[Suggestion- Enable Small File Combination When the Load Spark Sql Operator Is Used]]
- [[Suggestion- Do Not Use Multiple Transform Operators of Batch Processing or Lightweight ETL in Series]]
- [[Suggestion- Use Proper Flow Variables to Prevent Repeated Calculations of Large Datasets]]
- [[Suggestion- Plan an Independent YARN Resource Pool When Hadoop Is Shared by Data Cube and Other Syst]]
- [[Suggestion- When the Route Operator Has More Than Three Filter Criteria (Output Branches), Move the ]]
- [[Suggestion- Enable the Batch Interface for the Load JDBC Operator of the Batch Processing or Lightwe]]
