---
title: "Environment Planning Suggestions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002404037537.html"
depth: 4
---
# Environment Planning Suggestions

For teams that use the orchestration capability to develop assets, set different environments based on the asset lifecycle phases.

1\. Development: This environment, such as developer operating platform, is used for asset orchestration.

2\. Test: This environment, such as tester operating platform, is used to test assets orchestrated by developers.

3\. Production: This environment, such as the production platform, is used by users. (This environment must be isolated from the development and test environments.)

The following uses the OC scenario as an example. The typical planning is as follows:

1\. An independent data center is used as the ecosystem for developers to develop assets and test personnel to test assets. Development tenants and test tenants are logically isolated (development and test tenants can be combined based on site requirements). After assets are developed and tested, they are released to GDE Store through pipeline scanning.

2\. An independent data center is used as the production system for service users. Rather than providing orchestration capability (no Studio), the production system only deploys the runtime state. The tenant administrator or asset administrator downloads assets from GDE Store and deploys the assets to the runtime state of the production tenant.

![[en-us_image_0000002369315061.png]]

**Parent topic:** [[Overview|Overview]]