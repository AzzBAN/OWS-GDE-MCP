---
title: "Configuring Basic Information About the Data Visualization Screen"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_largescreen_004.html"
depth: 4
---
#### Procedure

1.  Choose **Project Management**.
2.  Select the project on which you want to perform operations.
3.  Access the target module. If there is only one module, it is accessed by default. If there are multiple modules, manually select one.
    
    ![[en-us_image_0000001473745512.png]]
    
4.  Choose **Data Visualization**.
5.  Click ![[en-us_image_0000001373363732.png]], set the data visualization screen name, and create a data visualization screen.
6.  Click the blank area in the canvas and configure global page properties in the property area on the right.
    
    ![[note_3.0-en-us.png]]
    
    -   After you click a blank area in the canvas, the global configuration of the data visualization screen is displayed on the right.
    -   After you click a component, the property configuration of the component is displayed on the right.
    
7.  Configure basic properties of the data visualization screen
    
    **Table 1** Basic properties of the data visualization screen  
    | Property Name | Description |
    | :-- | :-- |
    | Title | Title of the data visualization screen. You can click to configure multiple languages for the title. You can configure internationalization resources by two modes. For details, see 8 and 9. |
    | Label | Configured label. To configure a label for the data visualization screen, choose Data Visualization, click (Data Visualization list), and then click Tag Management. |
    | Display Name | Name displayed in the data visualization screen list. You can set this parameter to a name that is easy to identify. |
    | Open Level | Openness level of the data visualization screen. The options are:
    -   **Module**: The data visualization screen can be used only by a module.
    -   **Project**: When multiple modules exist in a project, the data visualization screen can be called across modules.
    -   **Public**: The data visualization screen is opened and can be called in the system.
    
     |
    | Screen Size | Resolution. The following options can be selected from the drop-down list, which can be adjusted:
    
    -   1366 \* 768
    -   1500 \* 1000
    -   1600 \* 900
    -   1920 \* 1080
    -   3480 \* 2080
    
    The recommended resolution is 1280 x 1024 or higher. |
    | Zoom | Supports auto-fit to the screen size. |
    | Cover | Click Upload to upload an image from the local PC as the cover. Click Capture to make a screenshot for the cover. |
    | Direction | When multiple background colors are set, the gradient effect is provided. You can set the gradient direction.
    
    -   **Horizontal**: Gradient the background color from left to right.
    -   **Vertical**: Gradient the background color from top to bottom.
    
    If only one background color is set, gradient effect is not displayed. |
    | Background Color | Click the text box and select a color from the palette. You can also enter the color code after the pound key (#). |
    | Background Image | Click Upload and select an image as the background image. |
    | Scrollbar Background Color | Background color of the scroll bar when the page content exceeds the page width and the scroll bar needs to be used. |
    | Scrollbar Slider Color | Slider color of the scroll bar when the page content exceeds the page width and the scroll bar needs to be used. |
    | Enable watermarking | After this function is enabled, data visualization screen pages can be protected through a watermark. The watermark can be set using the user name, timestamp, or customized content. |
    | Enabling Copyright Information | After this function is enabled, data visualization screen pages can be protected through a copyright statement. The copyright information can be set through the copyright text or icon. | 8.  Configure internationalization by adding an internationalization resource.
    
    1.  Add a page-specific internationalization resource. ![[en-us_image_0000001392481812.png]] indicates that internationalization can be configured for this field.
        
        ![[en-us_image_0000001458341333.png]]
        
        **Table 2** Parameters for configuring the internationalization information  
        | Name | Description |
        | :-- | :-- |
        | Resource ID | Resource ID. The value can contain letters, digits, underscores (\_), and periods (.). |
        | Save Bundle | Whether to save a created internationalization resource to a bundle
        -   **Yes**: Select the bundle where the created internationalization resource is to be stored. This bundle has been added to the **I18n** tab page. After the created internationalization resource is saved to the bundle, the bundle can be reused on other pages based on the openness level of the bundle.
        -   **No**: The created internationalization resource is saved in **Page Internationalization Resource** and can be used only on the current page.
        
         | 2.  Manage the internationalization resources added to **Page Internationalization Resource** on the **I18n** tab page.
        
        ![[en-us_image_0000001408021610.png]]
        
    3.  Manage and edit page-specific internationalization resources in a unified manner.
        
        ![[en-us_image_0000001407701918.png]]
        
    
9.  Configure internationalization by referencing an internationalization resource. Before the operation, create an internationalization resource bundle on the **I18n** tab page.
    
    1.  On the **I18n** tab page, create an internationalization resource bundle and configure the corresponding properties and multi-language data. For details, see [[Configuring the Internationalization Information|Configuring the Internationalization Information]].
    2.  In the right pane, click the **I18n** tab.
    3.  Click **+** to reference an internationalization resource.
        
        ![[en-us_image_0000001407701966.png]]
        
    4.  In the displayed dialog box, select the configured internationalization resource bundle and establish a reference relationship so that internationalization resources in the bundle can be referenced on the page. If a bundle is added repeatedly, the reference relationship is established only once.
        
        ![[en-us_image_0000001458141849.png]]
        
        Click **Confirm**. The referenced internationalization resource bundles are displayed on the **I18n** tab page.
        
        ![[en-us_image_0000001407862042.png]]
        
    5.  Click ![[en-us_image_0000001442721061.png]] next to the property for which internationalization needs to be configured. On the **Select** tab page, select a property from the existing bundles and click **Save**.
        
        ![[en-us_image_0000001458461669.png]]
        
        ![[note_3.0-en-us.png]]
        
        -   By default, page-specific internationalization resources can be selected on the **Select** tab page.
        -   For a public bundle, you can select it on the **Select** tab page only when the **Quote Internationalization Resource** relationship is configured for the bundle.
        
    
10.  Add a component.
     
     1.  Drag a component from the component bar on the left to the designer.
     2.  Select the component and configure component properties on the right to implement personalized display of the component. The properties that can be configured vary with components.
     
11.  Add a block.
     
     1.  In the **Components** area on the left, click the **Block** tab.
     2.  Select a block and drag it to the designer.
     
12.  Click ![[en-us_image_0000001374827042.png]] to save the page.