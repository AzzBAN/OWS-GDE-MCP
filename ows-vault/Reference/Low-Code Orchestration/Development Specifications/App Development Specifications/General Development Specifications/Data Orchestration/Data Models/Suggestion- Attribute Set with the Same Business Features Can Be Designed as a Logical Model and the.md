---
title: "Suggestion: Attribute Set with the Same Business Features Can Be Designed as a Logical Model and the Attribute Set Splitting Is Defined in the Physical Model"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001237104691.html"
depth: 6
---
# Suggestion: Attribute Set with the Same Business Features Can Be Designed as a Logical Model and the Attribute Set Splitting Is Defined in the Physical Model

**Specification name**: General\_DataFactory\_Data\_Model\_Attribute\_Sets\_with\_the\_Same\_Characteristics\_Designed\_as\_a\_Logical\_Entity

**Description**: The mapping between logical models and physical models is 1:_N_, that is, one logical model can map to multiple physical models on data sources. When registering the metadata information, the business side does not need to consider the splitting on the logical model. The splitting is performed on the physical model.

**Positive example**:

As shown in the following table, the business side defines the service model TDR\_PS\__XXX_ that maps to three physical models. The logical model contains all field attributes required by the business and maps to the physical models. Each physical model split all required fields on their physical data source.

    
| Logical Model | Field Description | Physical Model (HDFS) | Physical Model (Carbon) | Physical Model (Hive) |
| :-- | :-- | :-- | :-- | :-- |
| TDR\_PS\_XXX | \- | TDR\_PS\_XXX\_HDFS | TDR\_PS\_XXX\_CB | TDR\_PS\_HIVE |
| MSISDN | User's mobile phone number | MSISDN | MSISDN | MSISDN |
| ... | ... | ... | ... | ... |
| UE\_SRVCC\_CAPABILITY | Whether UE supports SRVCC | \- | UE\_SRVCC\_CAPABILITY | \- |
| UE\_VOICE\_PREFERENCE | Whether UE supports voice services | \- | UE\_VOICE\_PREFERENCE | \- |
| VOLTE\_INDICATOR | Whether UE supports VoLTE services | \- | VOLTE\_INDICATOR | \- |
| ADDITIONAL\_MSIP | MS IP address over S1-MME | ADDITIONAL\_MSIP | \- | \- |
| ADDITIONAL\_MSIP2 | MS IP address 2 over S1-MME | ADDITIONAL\_MSIP2 | \- | \- |
| AMF\_IP | AMF IP address over N1 or N2 | AMF\_IP | \- | \- |
| DPC | Gr destination signaling point code | \- | \- | DPC |
| DSSN | Gr destination subsystem number | \- | \- | DSSN |
| AUTH\_SUCCED\_FLAG | Whether authentication is successful | \- | \- | AUTH\_SUCCED\_FLAG | **Parent topic:** [[Data Models|Data Models]]