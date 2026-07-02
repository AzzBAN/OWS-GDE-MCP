---
title: "Basic Form Orchestration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mobile_component_019.html"
depth: 4
---
#### Orchestration Procedure

1.  Create the components\_form model corresponding to a form. The model fields must contain most data types, as shown in the following figure.
    
    ![[en-us_image_0000001662515425.png]]
    
2.  Generate services and pages based on this model.
    
    ![[en-us_image_0000001613795570.png]]
    
3.  Drag a **Form Panel** component to the component tree and set **Id** to **formpanel**.
    
    ![[en-us_image_0000001614275422.png]]
    
4.  Drag a **Hidden** component under **Data Fields**.
    
    ![[en-us_image_0000001662515457.png]]
    
5.  Set **Id** of the **Hidden** component to **sid**.
    
    ![[en-us_image_0000001614275462.png]]
    
6.  Set **Name** of the **Hidden** component to **sid**.
    
    ![[en-us_image_0000001613795662.png]]
    
7.  Set **Value** of the **Hidden** component to **1**.
    
    ![[en-us_image_0000001614275486.png]]
    
    ![[note_3.0-en-us.png]]
    
    **sid** matches the primary key **sid** in the model. Therefore, you can configure **Value** to locate the specific data in the model. For example, if **sid** is set to **1**, subsequent operations on the current form are performed based on the data record whose primary key is **1** in the model.
    
8.  Set **Require Submission** to **Yes** for the **Hidden** component.
    
    ![[en-us_image_0000001613955518.png]]
    
    ![[note_3.0-en-us.png]]
    
    The value of the **Hidden** component is involved in form data submission only when the property value is **Yes**.
    
9.  Drag a **Service Button** component under **Button**.
    
    ![[en-us_image_0000001662235569.png]]
    
10.  Set **Interface** of the **Service Button** component to **components\_form\_update**.
     
     ![[en-us_image_0000001614838638.png]]
     
11.  Set **Success Message** of the **Service Button** component to **Data updated successfully!**
     
     ![[en-us_image_0000001614358898.png]]
     
12.  Set **Text** of the **Service Button** component to **Update**.
     
     ![[en-us_image_0000001662958805.png]]
     
13.  Drag a **Data Loader** component under **Form Panel**.
     
     ![[en-us_image_0000001663079069.png]]
     
     ![[note_3.0-en-us.png]]
     
     After the form data is updated, preview the form. The **Data Loader** component calls the interface in [14](#EN-US_TOPIC_0000001450878353__en-us_topic_0000001450482301_li14870173085012) to query the returned data.
     
14.  Set **Interface** of the **Data Loader** component to **components\_form\_get**.
     
     ![[en-us_image_0000001662635501.png]]
     
15.  Set the parameters of the **Data Loader** component in the following figures.
     
     ![[en-us_image_0000001662235645.png]]
     
     ![[en-us_image_0000001614115622.png]]
     
     ![[note_3.0-en-us.png]]
     
     **#Form\[formpanel.sid\]** indicates the value of **sid** in the formpanel form. The value of **sid** for the **Hidden** component in the form can be transferred to the GET service as a parameter.
     
16.  After the preceding steps are performed, a basic form is created.
     
     ![[en-us_image_0000001613795758.png]]
     
17.  To view the functions of a form element component, for example, **Text Input**, drag a **Text Input** component under **Data Fields**.
     
     ![[en-us_image_0000001662635673.png]]
     
18.  Set **Name** of the **Text Input** component to **name**, which corresponds to the value of **name** for the **Text** component in the model.
     
     ![[en-us_image_0000001662515789.png]]
     
     ![[en-us_image_0000001613955762.png]]
     
19.  Set **sid** of the **Hidden** component to a data record in the model. In this example, set **sid** to **1**.
     
     ![[en-us_image_0000001613955798.png]]
     
20.  Preview the page.
     
     ![[en-us_image_0000001614519366.png]]
     
21.  Enter a value in the text box and click **Update**. The form data has been updated to the data record whose **sid** is **1** in the model by the service.
     
22.  Cancel the preview and preview the page again. Click **Data Loader**. The form data is displayed.