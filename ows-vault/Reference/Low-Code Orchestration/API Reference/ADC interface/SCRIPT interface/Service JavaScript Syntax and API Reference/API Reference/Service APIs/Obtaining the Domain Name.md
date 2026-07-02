---
title: "Obtaining the Domain Name"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_036.html"
depth: 7
---
# Obtaining the Domain Name

**Table 1** getDomainName function   
| API | Description | Example |
| :-- | :-- | :-- |
| ApplicationEnvironment.getDomainName() | Obtains the domain name of the environment where the app is deployed. If multiple domain names are configured in the environment, the domain name return priority is as follows: tenant-level domain name > system domain name > default domain name. | 
var s = ApplicationEnvironment.getDomainName();
return {domain:s};

Return value: https://{IP address}:{Port number} or https://{DomainName} | **Parent topic:** [[Service APIs|Service APIs]]