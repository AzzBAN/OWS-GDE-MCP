---
title: "Searching for Related Models"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_027.html"
depth: 5
---
#### Context

During the data query, multiple data models need to be queried to obtain corresponding data.

For example, in a member information system, there are two tables storing the member information, one is a basic information table **baseinfo** that is used to store names, and the other is a contact information table **contact** that is used to store phone numbers and email addresses.

When a query service needs to be provided and all information needs to be queried, you can search for the related model. When the information in **baseinfo** is matched, **contact\_code** is returned based on **baseinfo**. In this case, the contact information can be obtained from the **contact** table.

**Figure 1** Example of searching for related models  
![[en-us_image_0000001150010942.png]]

In the actual scenario, such information is encrypted. This is only an example and does not involve encryption and decryption conversion.