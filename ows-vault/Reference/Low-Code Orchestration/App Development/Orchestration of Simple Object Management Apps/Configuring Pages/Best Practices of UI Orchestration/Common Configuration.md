---
title: "Common Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adcui/commonConfig.html"
depth: 5
---
#### Obtaining Global Variables on the Page

Configure the method of obtaining window variables in the component, for example, **window.locale**.

**Configuration method**: #Global\[key\]

**Example**

![[en-us_image_0000001845174792.png]]

**Application scenario**

1\. Obtain the global variables provided by the platform, for example, **window.locale** and **window.tenantId**.

2\. If parameters contain sensitive data, you are advised to use the _#Global\[key\]_ variable to transfer parameters to prevent sensitive data from being displayed on the page in plaintext.