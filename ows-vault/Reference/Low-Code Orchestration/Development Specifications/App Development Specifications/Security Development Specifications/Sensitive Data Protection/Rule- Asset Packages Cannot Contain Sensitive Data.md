---
title: "Rule: Asset Packages Cannot Contain Sensitive Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208200523.html"
depth: 5
---
# Rule: Asset Packages Cannot Contain Sensitive Data

**Description**: If sensitive data is stored in assets, any person who can access the assets can analyze and discover the sensitive data, leading to improper data disclosure.

**Check guide**:

Check the following content that may contain sensitive data:

-   Text inputs, such as source code, comments, third-party interworking configuration, default values of input parameters, and hidden fields
-   Orchestration scripts and common definition configuration (such as variables and dictionaries) in API integration assets
    
    (1) Check whether all API orchestration scripts contain sensitive data, including the Service and Task diagram elements.
    
    ![[en-us_image_0000001668330808.png]]
    
    (2) Check whether the public definition contains sensitive data.
    
    ![[en-us_image_0000001716250377.png]]
    
-   In the flow configuration for data orchestration, check whether sensitive data is included in operators related to all types of flows, including but not limited to all custom SQL statements, custom functions, tenant parameters, system parameters, and flow parameters.
    
    ![[en-us_image_0000001773588460.png]]
    
-   Typical sensitive data, such as passwords, sessions, CSRF tokens, tickets, and OTPs For details, see [Appendix 1: Sensitive Data](../nottoctopics/en-us_topic_0000001100692676.html).

**Negative example**:

-   Passwords and mobile numbers are hardcoded based on the parameter mapping in the API integration asset. The email address information is defined in the common variables.

![[en-us_image_0000001668330812.png]]

![[en-us_image_0000001668171072.png]]

-   In the flow configuration for data orchestration, passwords, mobile numbers, and email addresses are hardcoded using custom SQL statements, custom functions, and parameters.

**Positive example**:

1.  Sensitive data to be transmitted is stored in models through model customization. Sensitive data such as passwords is encrypted. For details, see [[Rule- Property Type of the Model That Contains Sensitive Data Must Be Set to Password|Rule: Property Type of the Model That Contains Sensitive Data Must Be Set to Password]].
2.  During asset orchestration and running, the service API is called to obtain the data stored in the model for service processing.
3.  During asset orchestration and running, sensitive personal data and sensitive data such as passwords cannot be transferred to assets in plaintext.

**Tool supported or not**: yes except for data orchestration

**Note**: Currently, the tool supports the following sensitive data: Huawei employee IDs, mobile phone numbers, fixed-line phone numbers, session IDs, email addresses, ID card numbers, IP addresses, and passwords. Other sensitive data will be extended in the future.

**Specification name**: Security\_SensitiveData\_No\_Hard\_Coding\_In\_App

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: all

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]