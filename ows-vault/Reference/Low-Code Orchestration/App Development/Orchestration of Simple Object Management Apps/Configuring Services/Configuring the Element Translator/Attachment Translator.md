---
title: "Attachment Translator"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_059.html"
depth: 5
---
#### Context

For parameters of Object type, you can use the attachment translator to translate and convert parameters.

For example, the attachment field **attachment** exists in the model. When querying the model data, you need to extract the attachment name, content, and size from the **attachment** field. If you need to add the **attachment** field to the output parameter in the corresponding query service or query list service, set the type to **Object**, add the required output parameters **name**, **data**, and **size**, and configure them in the attachment translator.