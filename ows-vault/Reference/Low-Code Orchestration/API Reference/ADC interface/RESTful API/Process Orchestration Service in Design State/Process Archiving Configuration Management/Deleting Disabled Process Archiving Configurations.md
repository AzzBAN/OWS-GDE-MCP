---
title: "Deleting Disabled Process Archiving Configurations"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002514764730.html"
depth: 6
---
#### Function Description

It starts with GDE 24.2, Interface script invoked by the instance: var url\_params = {"id": "2c92802b967b218d01967b8995690000"}; var response = ServiceInvoker.delete("/adc-studio-bpm/rest/v1/archive-config/delete/2c92802b967b218d01967b8995690000", url\_params);. This interface is used to delete disabled process archiving configurations. This operation can be performed only when the configuration status is disabled. The format of the request parameter must be strictly verified to ensure that the ID complies with the system specifications.