---
title: "Rule: Validator Must Be Used to Verify Service Input Parameters"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208519047.html"
depth: 5
---
# Rule: Validator Must Be Used to Verify Service Input Parameters

**Description**: A service may receive untrusted data from users, network connections, or other sources, and transfer the data as business services to internal or external target modules or systems or directly store the data. The target module or system may not be able to distinguish and process untrusted data. Untrusted data that is not verified may cause injection attacks of a certain type, which severely affects the system. Therefore, untrusted data must be verified.

GDE provides developers with the capability of validating service input parameters, that is, validators. Validators are classified into three types. The three types of validators can coexist. The validation is successful only when all the configured validators pass the validation.

-   Common validation: provides common validation capabilities to validate data of the text, digit, date, TQL expression, and IP address types. Developers can validate specified fields through simple configuration.
-   Run Script: provides the customized validation capability. If the capability cannot meet the requirements of complex business scenarios, developers can compile JavaScript code to customize validation.
-   Existence validation: provides the capability of checking whether a parameter to be validated already exists.
    

**Check guide**: Log in to the develop-state environment, select a desired project, select the service corresponding to the corresponding module, click the desired service node, check whether validators are configured for all elements in the **Input Parameter Configuration** area on the right, and check whether proper validation rules are configured for security attack risks involved in services.

**Positive example**:

Take a parameter of the string type as an example. Access the corresponding service, select a validator for the service input parameters in the **Input** area, and configure the validation rule.

![[en-us_image_0000001522121553.png]]

Take the default validation type of the platform as an example. In addition to the text type, some default validation types are provided and corresponding validation rules are provided. For example, if there is the IP address type, only the IP address in the standard format can be entered.

A. Configure a common validator based on service requirements. Developers can select required validation items based on their service input during development.

Example of the blacklist mode:

![[en-us_image_0000001522125049.png]]

Example of the platform validator mode (supporting the IP address, email address, phone number, and Greek letters)

![[en-us_image_0000001522283357.png]]

Example of the regular expression (whitelist mechanism):

![[en-us_image_0000001522125545.png]]

B. The integer type supports common length validation.

![[en-us_image_0000001522281913.png]]

C. The decimal floating type supports range validation.

![[en-us_image_0000001471245470.png]]

D. Common types support existence verification and Run Script.

![[en-us_image_0000001522285457.png]]

**Exception scenarios**:

1\. If the input parameters come from trusted sources, the validator is not mandatory. For example, the service access scope has been restricted, and no untrusted data source exists in the access scope.

Example of trustworthy input: For parameters that are not directly transferred by the frontend service, the service entry has been validated. Data read from the database has been validated when being entered into the database. If the data source is not controlled by the service, the data is not trustworthy input.

2\. If data has been validated in other modes, the validator is not mandatory. For example, if another service is called, the called service has been validated.

**Validation example in a typical web attack scenario**:

Text parameters may be used to concatenate TQL statements. Concatenating commands may introduce security issues such as TQL injection and command injection. Developers do not know how to validate these parameters. Therefore, examples are provided based on typical web attack scenarios in Huawei specifications.

-   **Text blacklist validation mode**:

**Special Characters** is set to **~!@#$^<>**, indicating the blacklist validation mode. Special characters configured in the blacklist cannot exist in the text content.

![[en-us_image_0000001522285693.png]]

After the configuration, when you enter a character in the blacklist, the system displays a message indicating that the special character is not allowed.

-   **Text whitelist validation mode: (preferred)**:

**Regex** is set to **^\[A-Za-z0-9\]+$**, indicating the whitelist validation mode. Only the character strings that match the regular expression can be entered.

![[en-us_image_0000001522445505.png]]

After the configuration, when you enter a character not in the whitelist, the system displays a message indicating that the character is not allowed.

-   **TQL injection scenario**

If the parameters to be validated are used for concatenating TQL statements, set the validator as follows:

Blacklist mode:"';%\_/\\^\[

Whitelist mode: ^\[A-Za-z0-9\]+$

-   **XSS injection scenario**

If the parameters to be validated are used for displaying page components, set the validator as follows:

Blacklist mode: &<>"'/()

Whitelist mode: ^\[A-Za-z0-9\]+$

-   **Command injection scenario**

If the parameters to be validated are used for concatenating background commands, set the validator as follows:

Blacklist mode: |;&$><\`\\!\\n

Whitelist mode: ^\[A-Za-z0-9\]+$

-   **CSV injection scenario**

If the parameters to be validated are used for generating a CSV file, set the validator as follows:

Blacklist mode: =+-@

Whitelist mode: ^\[A-Za-z0-9\]+$

Note: In all injection scenarios, it is recommended that only letters and digits be allowed, as listed in the whitelist. If the service has special requirements, compile the regular expression based on site requirements.

**Tool supported or not**: yes

**Specification name**: Security\_DataCheck\_LogicFlow\_\_ParameterNoCheck

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: all

**Parent topic:** [[Data Verification|Data Verification]]