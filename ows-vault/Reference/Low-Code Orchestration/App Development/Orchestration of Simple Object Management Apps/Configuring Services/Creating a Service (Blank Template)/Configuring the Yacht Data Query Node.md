---
title: "Configuring the Yacht Data Query Node"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_054.html"
depth: 5
---
#### Context

The application scenario of **DataService Query** under **Platform Services** is different from that of **Get**, **GetList**, and **TQLQuery** under **Model Operations**.

![[en-us_image_0000001456372185.png]]

![[note_3.0-en-us.png]]

This node is not displayed by default. To display this node, set **integration\_yacht** to **true** at the master level.

This node is used for data exchanges between ADC and Data Cube. The following query modes are supported:

-   TQL mode: Data can be queried using TQL syntax or TQL scripts. For details about the syntax and examples, see [[TQL Syntax Reference|TQL Syntax Reference]].
    
    An example is as follows.
    
    select \* from #table where name = $name and age > $age limit #start,#limit order by #orders #asc\_desc
    
-   Yacht SQL mode: The SQL editor for Yacht service is provided to edit SQL statements for accessing Data Cube data through Yacht, implementing flexible development of data access functions. For details about the SQL syntax supported by Yacht, see [[SQL Syntax of the Yacht Service|SQL Syntax of the Yacht Service]].
    
    Before configuring this item, you are advised to prepare a runtime-state environment where Yacht has been installed and understand the data source to be queried under **Products and Services** > **Data Cube** > **Data Opening** > **SQL Editor**.
    
    ![[en-us_image_0000001456252497.png]]
    
    An example of Yacht SQL statements is as follows:
    
    yacht\_sql: select \* from #table where name = ? and age > ? order by #orders #asc\_desc limit #start,#limit
    

Take the preceding statement as an example. You need to set the input parameters listed in the following table in the service.

**Table 1** Input parameters for DataService Query  
| Parameter | Description |
| :-- | :-- |
| table | Table name. If the table name has been specified in the SQL statement, for example, select \* from cfg.BAT\_IMP\_RELATION\_D, you do not need to set the table name again. If no table name is specified in the SQL statement, you need to transfer the table name using a parameter. For example, if select \* from #table is used, you need to transfer the specified table name using a parameter. |
| start | Start row number of the query |
| limit | Number of query records |
| orders | Field to be sorted. Multiple fields are supported. Use commas (,) to separate them. |
| asc\_desc | Sorting mode of the field to be sorted. The options are true (ascending order) and false (descending order). |
| yacht\_database | Yacht data source for the specified query. By default, if this parameter is not transferred, the query data source is physical-MetaOne. That is, you do not need to specify this parameter when querying physical-MetaOne. To query other data sources, such as data in physical-MONITOR\_PT, transfer this parameter and specify the data source. |
| Other parameters | Parameter used as the query input, for example, a field in a data table | The following uses the Yacht SQL mode as an example to describe how to configure the DataService Query service.