---
title: "List View"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_007.html"
depth: 4
---
#### Orchestration Procedure

1.  Drag a **List View** component to the component tree and set **Id** to **listview**.
    
    ![[en-us_image_0000001662672905.png]]
    
2.  Set **Interface** to the preconfigured service **components\_person\_get\_list**. Simulation data in the following format is returned:
    
    ![[en-us_image_0000001614273106.png]]
    
    ![[en-us_image_0000001614273190.png]]
    
3.  Set the component properties to the key values of the corresponding fields based on the fields returned by the service. The following figures show the mappings.
    
    ![[en-us_image_0000001662233325.png]]
    
    ![[en-us_image_0000001614113318.png]]
    
4.  Set **Item Url Field** to **url**.
    
    ![[en-us_image_0000001662633193.png]]
    
    -   When a user clicks the data record containing Tom, information at the corresponding URL **/mobile\_test001/components/example\_detail** is displayed.
        
        ![[en-us_image_0000001662440245.png]]
        
    
    ![[note_3.0-en-us.png]]
    
    **URL**, **Location**, and **Item Url Field** are used to configure the redirection path of the list data. Their priorities are different and are as follows in descending order: **Item Url Field** > **Location** > **URL**. When you click the redirection link, the system obtains values from the three configurations in sequence until a required value is obtained.
    
5.  Set **Link Parameter** as shown in the following figure.
    
    ![[en-us_image_0000001614113354.png]]
    
    ![[en-us_image_0000001614273310.png]]
    
    -   After you click a data record, a page is displayed and the value of **name** is sent to the target page.
        
        ![[en-us_image_0000001662633233.png]]
        
        ![[en-us_image_0000001613957926.png]]
        
    
6.  Set **Item Identify Field** to **sid**.
    
    ![[en-us_image_0000001662673253.png]]
    
7.  Set **Searchable** to **Yes**.
    
    ![[en-us_image_0000001662673261.png]]
    
    -   The search box is displayed above the list.
        
        ![[en-us_image_0000001662513425.png]]
        
    
8.  Set **Search Field** to **name**.
    
    ![[en-us_image_0000001614677058.png]]
    
    -   When you click the search button, the content in the text box is sent to the query service as the value of **name**.
        
        ![[en-us_image_0000001662957225.png]]
        
        In the query service, the **name** parameter can be used as the query condition to filter data.
        
        ![[en-us_image_0000001556175894.png]]
        
    
9.  After the configuration is complete, view the information similar to that shown in the following page on the preview page.
    
    ![[en-us_image_0000001623969990.png]]
    
10.  If the **Customized Template** property is configured, configure properties as shown in the following figures.
     
     ![[en-us_image_0000001672329597.png]]
     
     ![[en-us_image_0000001624449738.png]]
     
     -   The list is rendered in the format same as that of the template content.
         
         ![[en-us_image_0000001623970030.png]]