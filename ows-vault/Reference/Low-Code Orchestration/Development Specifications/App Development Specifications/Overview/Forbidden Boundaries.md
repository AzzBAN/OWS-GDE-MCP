---
title: "Forbidden Boundaries"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363441.html"
depth: 4
---
# Forbidden Boundaries

For asset development, especially microservice development of service PEs, some boundaries that cannot be restricted by technical means must be forbidden based on the document and disclaimer requirements. If the service uses capabilities in forbidden boundaries, the compatibility cannot be ensured.

 
| Scenario | Compatibility Policy |
| :-- | :-- |
| Use the platform microservice ContextPath to concatenate the URL in the customized JavaScript (JS) file. | Incompatible |
| Front-end/terminal-customized JS directly depends on the system JS library (such as jQuery and Vue). | Incompatible |
| Front-end/terminal-customized JS and CSS directly depend on the DOM element structure. | Incompatible |
| Directly access the dynamic table where the database model is located and model data through JDBC. | Incompatible |
| The multi-process technology is used in Python FaaS. | Incompatible |
| The Allow Access to Internal DOM switch is enabled in the common configuration of the page or dashboard. | Incompatible |
| Use AJAX to directly access web interfaces that are not in the public interface list. | Incompatible | **Parent topic:** [[Overview|Overview]]