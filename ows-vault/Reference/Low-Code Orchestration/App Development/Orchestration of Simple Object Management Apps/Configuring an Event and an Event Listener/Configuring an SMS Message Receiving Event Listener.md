---
title: "Configuring an SMS Message Receiving Event Listener"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_event_006.html"
depth: 4
---
#### Context

SMS message receiving event is preset in the system and used together with the Notice service provided by GDE. After receiving an SMS message, the Notice service triggers an orchestration event. Based on the listener configuration of this orchestration event, ADC triggers the corresponding service.

[Table 1](#EN-US_TOPIC_0000002025165833__table10922121602911) describes the parameters of the SMS message receiving event (/System/sms/sms\_received).

**Table 1** Event parameters  
| Parameter | Description |
| :-- | :-- |
| receive\_log\_id | ID of the received log, which is of the text type |
| sms\_gateway\_id | ID of the SMS gateway, which is of the text format |
| receive\_time | Receiving time, which is of the integer format |
| dest\_address | Target number, which is of the text format |
| src\_address | Source number, which is of the text format |
| sms\_content | SMS message content, which is of the text format | For example, if SMS message receiving logs need to be recorded in a service, perform listening on the SMS message receiving event. When this event is triggered, the service for creating logs is triggered to record logs.