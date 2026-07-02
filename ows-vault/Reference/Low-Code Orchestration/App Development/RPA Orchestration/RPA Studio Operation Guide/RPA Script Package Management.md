---
title: "RPA Script Package Management"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_studio_dev_rpa_0002.html"
depth: 4
---
#### Prerequisites

-   You have logged in to the develop-state environment and created RPA-related projects and modules based on site requirements. For details, see [[Setting Up a Project|Setting Up a Project]].
-   A script package has been recorded using RPA Studio and released to obtain the ZIP package. For details, see [[RPA Development Guide|RPA Development Guide]].
-   If the **Application service call 2.0** control is used in the script and **Open Level** of the service called by the control is set to **Module** or **Project**, ensure that the script and the called service belong to the same module or project and the project is deployed to the runtime-state environment. Otherwise, the script fails to call the service.
-   (Optional) The script package (if exists) has been imported to the system based on [[Managing RPA Plugin Packages|Managing RPA Plugin Packages]].
-   (Optional) You have downloaded the required script file from GDE Store.