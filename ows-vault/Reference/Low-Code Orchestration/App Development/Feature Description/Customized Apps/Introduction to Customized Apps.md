---
title: "Introduction to Customized Apps"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_cust_005.html"
depth: 4
---
# Introduction to Customized Apps

When an app is running on the live network, the released baseline app is customized for different tenants or sites due to differences and changes between sites and service requirements. As a result, the app mixes baseline and customized contents together, making the version management difficult. With the expansion of services, the problem will become more serious. These hinder service deployment and expansion. The pain points are:

-   During an upgrade, the services or features of a general app will overwrite the app customized for a site. The changes must be sorted out manually and incorporated to the target app. This is time-consuming and error-prone. (This poses high skills requirements for the upgrade personnel.)
-   The apps are not well protected, and customized services are mixed in the baseline apps. Therefore, it is difficult for the service personnel to determine the customized contents. The upgrade risk is high.

To resolve preceding problems, the system provides the configuration and development function for customized apps to separate the baseline contents from customized contents, implementing efficient customization. Before customization, developers are advised to analyze possible customization features and plan customization. [Figure 1](#EN-US_TOPIC_0000001442152553__fig1293812917217) shows the customization capabilities. The customization capabilities are described as follows:

-   A project to be customized is called a baseline project.
-   A baseline project can be customized into multiple projects. For example, if the baseline project needs to be used to deliver multiple projects such as A, B, C, and D, you need to perform customization for multiple times to obtain corresponding customized projects.
-   When a baseline project is customized in a project, all customized orchestration elements are placed in only one project for management.
-   In a customized project, you can customize orchestration elements in the baseline project, and add orchestration elements.
-   Elements in a baseline project can be customized in a project only after being configured to customizable.

**Figure 1** Customized project diagram  
![[en-us_image_0000001453828705.png]]

-   The baseline model mod\_a needs to be customized at a site and is customized as mod\_a' in the customized project. The running effect is that the customized model mod\_a' takes effect.
-   The baseline model mod\_b can be ignored in the customized project because it does not need to be customized at a site. The running effect is that the baseline model mod\_b takes effect.
-   The baseline service service\_a needs to be customized at a site and is customized as service\_a' in the customized project. The running effect is that the customized service service\_a' takes effect.
-   The baseline service service\_b can be ignored in the customized project because it does not need to be customized at a site. The running effect is that the service\_b takes effect.
-   To add a requirement at a site, you can add models and services to the customized module or add a module. The new orchestration elements also take effect during running.

**Parent topic:** [[Customized Apps|Customized Apps]]