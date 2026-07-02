---
title: "Configuring the Tenant-Level Studio Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_dev_overview_008.html"
depth: 4
---
#### Context

There are many page elements on the Studio page, such as the logo, menu, navigation, and help menu. These elements can be displayed or not displayed based on user preferences.

The following table lists the supported configuration methods for Studio elements.

**Table 1** Studio configuration    
| Configuration Level | Operator | Configuration Method | Validation Range |
| :-- | :-- | :-- | :-- |
| Tenant | Tenant administrator | Menu configuration | The configuration takes effect within a tenant and takes effect only in projects created using a blank template. |
| Template | Template developer | Offline editing of the template definition file | The configuration takes effect only in projects created using this template. The priority of the template level is higher than that of the tenant level. That is, during project creation, when the display elements defined in the template are different from those configured using the tenant level configuration method, the project template definition is used. | The following describes how to configure the tenant-level Studio.