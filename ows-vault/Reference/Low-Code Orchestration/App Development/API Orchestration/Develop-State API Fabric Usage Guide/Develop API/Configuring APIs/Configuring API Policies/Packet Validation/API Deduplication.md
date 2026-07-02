---
title: "API Deduplication"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_064.html"
depth: 8
---
#### Context

The API Fabric supports API deduplication. After defining the deduplication field in an API request, the system determines whether the API is called by the same request based on the field in the method to prevent the API from being called by the same request repeatedly in a specified period.

For example, if your click **Submit** twice on the frontend page, an API in the API Fabric is repeatedly called.