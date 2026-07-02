---
title: "Carousel Table"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/component/carouselTable.html"
depth: 5
---
#### Properties

![[en-us_image_0000001557200862.png]]

**Table 1** Border Settings  
| Name | Description |
| :-- | :-- |
| Vertical Border | Whether to display the vertical border of a table. |
| Border Style | Border type, width, and color. | ![[en-us_image_0000001556921582.png]]

**Table 2** Row settings  
| Name | Description |
| :-- | :-- |
| Rows | Number of rows in the carousel list. |
| Alignment Mode | Alignment mode of the cell content. The options are Left, Center, and Right. |
| Text Style | Font, width, color, and size of the cell content. |
| Row Background Color | Background color of a row in the list. |
| Zebra Stripe | Whether to display zebra patterns, that is, the colors of odd and even lines are different. |
| Zebra Stripe Color | Background color of even rows in the list. | ![[en-us_image_0000001556922194.png]]

**Table 3** Highlight Settings  
| Name | Description |
| :-- | :-- |
| Enable Highlight Effect | Whether to enable the highlight effect during rotation display. |
| Text Style | Text style of the highlighted row cell content. |
| Background Color | Background color of the highlighted row. | ![[en-us_image_0000001556763034.png]]

**Table 4** Animation Settings  
| Name | Description |
| :-- | :-- |
| Rotate Display | Specifies whether to enable the rotation display effect. |
| Animation Duration | Scrolling duration of each row of data during rotation display. |
| Autoplay | Specifies whether to perform automatic rotation after rendering is complete. |
| Step | Number of data records to be rotated at a time. When the step exceeds the number of rows on a page, the number of rows on a page is used. |
| Overflow Scrolling | If the function is enabled, the overflow text on the preview or release page can be automatically scrolled. |
| Overflow Duration | Scrolling duration of overflow text. | ![[en-us_image_0000001607322393.png]]

**Table 5** Pagination  
| Name | Description |
| :-- | :-- |
| Alignment | Alignment mode of the pagination bar. The options are Left, Center, and Right. |
| Margin | Outer margin of the pagination bar. | ![[en-us_image_0000001557202106.png]]

**Table 6** Column Settings  
| Name | Description |
| :-- | :-- |
| Column Type | The value can be Index, Custom, or Normal. |
| Field Name | Field mapped to a table column in the data source |
| Table Header | Content displayed in the table header |
| Column Width | Column width |
| Table Header Template | You can directly configure the template or upload an HTML file. |
| Content Template | Columns customized in the HTML file are used. This parameter is valid only for common columns. |
| Sortable. | Whether a column supports sorting. This parameter does not take effect for index columns. |
| Cell Style | The cell style can be customized when Column Type is set to Normal or Index. |
| Progress | This parameter is displayed only when Column Type is set to Custom. The progress bar style can be configured. | ![[en-us_image_0000001606962565.png]]

**Table 7** Special Row  
| Name | Description |
| :-- | :-- |
| Rule | The rows that meet the rule are displayed in the rule background color. |
| Background Color | Background color of the special row. | **Table 8** Data export configuration  
| Name | Description |
| :-- | :-- |
| excelExportServiceIds | Export service identifier. |
| exportOption | Options to be exported. exportAll can be selected. |
| parameters | Parameters of the data export service, such as limit (used to limit the number of records to be exported) and start (used to specify the start position of record export). |
| success | Callback function after the export is successful. |
| error | Callback function after the export fails. | ![[en-us_image_0000001814203129.png]]