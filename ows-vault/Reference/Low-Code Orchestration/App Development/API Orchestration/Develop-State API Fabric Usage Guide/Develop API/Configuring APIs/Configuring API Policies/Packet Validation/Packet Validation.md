---
title: "Packet Validation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_061.html"
depth: 7
children: ["Parameter Verification", "JSON Protection", "API Deduplication"]
---
# Packet Validation

-   **[[Parameter Verification|Parameter Verification]]**  
    Northbound request packets of the SOAP protocol support XSD verification and filtering, and northbound request packets of the HTTP protocol support Content-Type verification. The API Fabric intercepts request packets that fail the verification.
-   **[[JSON Protection|JSON Protection]]**  
    If the request body is in JSON format, you can configure a JSON protection policy to standardize the JSON content of the request body and verify the JSON content.
-   **[[API Deduplication|API Deduplication]]**  
    The API Fabric supports API deduplication to prevent an interface from being repeatedly called by the same request in a specified period. Currently, the API Fabric supports operation-level definition.

**Parent topic:** [[Configuring API Policies|Configuring API Policies]]

## Sub-topics

- [[Parameter Verification]]
- [[JSON Protection]]
- [[API Deduplication]]
