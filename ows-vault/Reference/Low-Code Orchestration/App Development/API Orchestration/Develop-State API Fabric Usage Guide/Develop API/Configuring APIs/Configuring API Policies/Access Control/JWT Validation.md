---
title: "JWT Validation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_052.html"
depth: 8
---
#### Context

If a JWT validation policy is configured, the API Fabric verifies the JWT token after receiving the request. During JWT token verification, the digital signature is verified first. If the verification fails, a 401 response is returned and a security log is recorded. After the digital signature is successfully verified, the declaration is verified. If the verification fails, a 403 response is returned and a security log is recorded.