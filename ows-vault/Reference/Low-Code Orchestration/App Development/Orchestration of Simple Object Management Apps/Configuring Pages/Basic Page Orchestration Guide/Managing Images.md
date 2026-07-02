---
title: "Managing Images"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_studio_adv_general_0054.html"
depth: 5
---
#### Procedure

1.  Access a created project and module.
2.  Choose **Page** > **Orchestration Resource** > **Image Management**.
3.  (Optional) Click ![[en-us_image_0000001762325457.png]] under **Picture Catalog** on the left to create an image catalog.
    
    ![[en-us_image_0000001716254962.png]]
    
4.  Click **Add** to upload an image.
    
    **Figure 1** Image configuration  
    ![[en-us_image_0000001716255134.png]]
    
    **Table 1** Parameters  
    | Parameter | Description |
    | :-- | :-- |
    | Directory | Catalog for storing archived images |
    | Pictures | Image file you selected. Only the following formats are supported: JPG, GIF, PNG, and SVG. |
    | File Name | File name automatically generated based on the image file. Additionally, the system automatically generates the image path based on the image name. |
    | Description | Brief description |
    | Terminal Usage | Whether an image is used on a terminal |
    | Open Level | Image open level
    -   **Module**: The image can be used within a module.
    -   **Project**: When multiple modules exist in a project, the image can be called across modules.
    -   **Public**: The image is opened and can be called in the system.
    
     | 5.  Click **Submit**. You can view the image URL in the list, for example, **/adc-static/imagemgt/images/$**_{tenant\_id}_**/test\_wc/test\_wc/wc/ image 6.png**. This address is used when an image is referenced.