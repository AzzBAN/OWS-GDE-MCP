---
title: "Rule: Privacy Statement Must Be Configured for Tenants If Personal Data Is Involved in an Asset"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283736.html"
depth: 5
---
# Rule: Privacy Statement Must Be Configured for Tenants If Personal Data Is Involved in an Asset

**Description**: If personal data (including data that is collected, used, transferred, and stored) is involved when a product provides normal services, a privacy statement must be provided on the product UI to describe the type, purpose, processing method, and time limit of all personal data collected by the product.

The privacy statement consists of two parts: platform-level privacy statement and tenant-level privacy statement.

Platform-level privacy statement includes the statement about personal data in the existing functions of the platform.

The platform-level privacy statement is released by the platform and managed by O&M personnel online. Developers can view but cannot manage the privacy statement.

If personal data is involved in functions (except for functions provided by the platform) provided by developers, the tenant-level privacy statement must be customized and provided. You can choose **Administration** > **Security Configuration** > **Declaration Configuration** from the menu to view the configuration.

The tenant administrator manages the tenant-level privacy statement on the UI. Once the statement is changed, the user will receive a confirmation notification upon login.

**Check guide**: If the asset involves personal data (for details about the personal data scope, see [[Appendix 2- Examples of Personal Data|Appendix 2: Examples of Personal Data]]), add personal data description to the asset introduction and contact the administrator to modify the tenant-level privacy statement. Input points that may involve personal data:

-   Users enter fields required by the asset page and beyond the privacy statement scope.
-   The Excel file to be imported contains fields beyond the privacy statement scope.
-   Fields beyond the privacy statement scope are transferred through the inbound API.

**Negative example**:

A new model and page are created in the asset, and the user is required to enter the ID card number.

The tenant administrator does not add the description of the ID card number to the tenant-level privacy statement.

**Positive example**:

After importing an asset involving personal data, the tenant administrator needs to modify the privacy statement. The administrator can choose **Administration** > **Security Center** > **Privacy Statement** from the menu bar. On the displayed page, click **Create** and add the tenant privacy statement description.

**Note:** The privacy statement must be reviewed by the tenant administrator in the local legal affairs department.

**Tool-based reference:** The tool provides auxiliary scanning capabilities.

**Tool supported or not**: no

**Specification name**: Security\_PrivacyProtection\_ShouldRefreshPrivacyStatement

**Severity**: major

**Orchestration scenarios**: all

**Parent topic:** [[Privacy Protection|Privacy Protection]]