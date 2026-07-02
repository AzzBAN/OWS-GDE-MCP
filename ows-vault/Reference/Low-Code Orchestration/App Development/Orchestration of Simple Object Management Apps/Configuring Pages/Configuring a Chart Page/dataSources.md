---
title: "dataSources"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_echart_002.html"
depth: 5
---
#### dataSources

You can use the dataSources node to orchestrate data sources of report templates. dataSources determines the data to be displayed in a report.

Right-click **dataSources** and choose **Add Child** > **ServiceDataSource** (or **BlankDataSource**) from the shortcut menu to create a service data source. Two types of data sources are supported: ServiceDataSource and BlankDataSource.

**Figure 1** dataSources  
![[en-us_image_0000001212450497.png]]

**Table 1** Description of ServiceDataSource   
| Name | Description |
| :-- | :-- |
| type | ServiceDataSource |
| name | Data source name |
| serviceId | Double-click the cell to make it editable. The options are as follows: 1. Select a service from the drop-down list box. 2. Click the search icon and select a value from the displayed dialog box. |
| parameters | Input parameters required by a service. |
| columns | Select the fields that will be displayed in a chart from the values returned by the service (used when the series data is obtained from options in iteration mode). |
| name | Key value returned by the service (The returned field of the service must be the same as name configured here). |
| type | Data type. Possible values:
-   DateTime
-   Text
-   Number

 |
| label | Label name that will be displayed in a chart | **Table 2** Description of BlankDataSource   
| Name | Description |
| :-- | :-- |
| type | BlankDataSource |
| name | Data source name |
| columns | name | Key returned by the service |
| type | Data type |
| label | Label name that will be displayed in a chart |