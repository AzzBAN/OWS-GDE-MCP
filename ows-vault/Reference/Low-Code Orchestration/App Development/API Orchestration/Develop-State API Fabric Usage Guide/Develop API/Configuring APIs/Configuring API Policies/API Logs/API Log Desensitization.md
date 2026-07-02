---
title: "API Log Desensitization"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_059.html"
depth: 8
---
#### Restrictions and Description

-   After the configuration is successful, the content of these fields is displayed as **\*\*\*\*\*\*** in the runtime-state logs. Only method-level configuration is supported.
-   If both endpoint method–level and API method–level desensitization policies are configured for a transparent transmission API, the two policies must be the same. Otherwise, the endpoint method–level policy may overwrite the API method–level policy.
-   The user-defined desensitization rule takes effect only for **interface logs**. Other types of logs **do not** comply with this rule. By default, all sensitive fields are desensitized.
-   If an XPath directory has been configured for **Prefix** (that is, **Prefix** is set to **//**), you are advised not to configure an XPath desensitization rule.
-   If **Parameter Name** is configured using the fastjson syntax and contains a hyphen (-), set the parameter name based on the example **\['test-01'\]**.
-   When using **JPath desensitization** rules, configure them based on the fastjson specifications.
-   If five or more desensitization rules are configured, exact desensitization is used. To retain fuzzy desensitization, change the value of **sys\_sensitive\_fuzzy\_enable** to **true** by referring to "Commissioning > Feature Commissioning > API Fabric Feature Commissioning > Modifying System Configurations" in _GDE x.x.x Product Documentation_.