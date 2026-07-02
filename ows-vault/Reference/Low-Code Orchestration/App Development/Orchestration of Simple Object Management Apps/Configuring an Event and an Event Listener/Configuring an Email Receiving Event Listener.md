---
title: "Configuring an Email Receiving Event Listener"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_event_005.html"
depth: 4
---
#### Context

Email receiving event is preset in the system and used together with the Notice service provided by GDE. After receiving an email, the Notice service triggers an orchestration event. Based on the listener configuration of this orchestration event, ADC triggers the corresponding service.

[Table 1](#EN-US_TOPIC_0000001155077308__table10922121602911) describes the parameters of the email receiving event (/System/mail/email\_received).

**Table 1** Event parameters  
| Parameter | Description |
| :-- | :-- |
| attachment | Email attachment. It is of the file list type. |
| title | Email title, which is of the text type |
| content | Email content, which is of the text type |
| email\_from | Email sender, which is of the text type |
| email\_to | Email recipient, which is of the text type |
| email\_cc | CC recipient of an email, which is of the text type |
| email\_bcc | BCC recipient of an email, which is of the text type |
| read\_status | Email receiving status, which can be an integer
-   **0**: Unread
-   **1**: Read

 |
| send\_time | Email sending time |
| msg\_id | Email message ID |
| server\_id | Email server ID | For example, if email receiving logs need to be recorded in a service, perform listening on the email receiving event. When this event is triggered, the service for creating logs is triggered to record logs.