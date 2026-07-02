---
title: "Configuring Existence Verification"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_013.html"
depth: 5
---
#### Context

For input parameter of the string type, the existence of the parameters can be verified.

Data existence verification: If the value of the **text1** field to be created is **aaa**, the value of the corresponding field configurations queried in the corresponding model or service must contain **aaa**. Otherwise, the creation fails.

For example, when creating the member information, the system needs to check whether the member type exists.

-   If the value of **member\_type** is **vip** and **vip** exists in **member\_type** during the verification, the verification is successfully.
-   If the value of **member\_type** is **vvip** and **vvip** does not exist in **member\_type** during the verification, the verification fails.

**Figure 1** Existence verification using a model  
![[en-us_image_0000001194210399.png]]

**Figure 2** Existence verification using a service  
![[en-us_image_0000001194210417.png]]

If the data existence verification fails, the service returns a failure message.

Both the model and service can be used for verification in the preceding scenario. In the actual development, there are more complex scenarios. You can select a proper method based on site requirements.