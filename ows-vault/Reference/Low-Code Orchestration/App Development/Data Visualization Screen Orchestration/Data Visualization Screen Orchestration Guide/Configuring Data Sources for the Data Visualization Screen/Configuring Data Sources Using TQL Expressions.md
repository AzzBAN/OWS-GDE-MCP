---
title: "Configuring Data Sources Using TQL Expressions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_largescreen_010.html"
depth: 5
---
#### Context

You can use TQL expressions to directly query model data and use the model data as data sources of the data visualization screen.

To query model data using TQL expressions and use the model data as data sources of the data visualization screen, **Data can be accessed by the frontend** must be enabled for the model.

For example, you need to use TQL expressions to query device information model data. This model contains the **status** field, which is used to identify device states. The number of assets in different states can be displayed in a pie chart on a data visualization screen.

To use the model for TQL query, you need to enable the frontend data access function.

![[en-us_image_0000001761599308.png]]

Assume that you need to collect statistics on assets in different device states and display the statistical results in a pie chart. The corresponding TQL statement is as follows:

select status,count(1) as num from "/office\_equipment/office\_equipment/office\_equ\_equipment\_mgt" as office\_equ\_equipment\_mgt group by status