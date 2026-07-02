---
title: "Introduction to Element Validator Capabilities"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_005.html"
depth: 5
---
# Introduction to Element Validator Capabilities

Element validators are used to verify input elements of services. Validators vary according to input parameter types.

**Table 1** Introduction to element validator capabilities  
| Input Element Type | Verification Type |
| :-- | :-- |
| String | 
-   Common verification
    -   **text**
    -   **Date**
    -   **TQL expression**
    -   **enum**: enumerated value.
    -   **IP address**: Enter an IP address in the correct format.
    -   **phone**: Enter a phone number in the correct format.
    -   **email**: Enter an email address in _x@y.z_ format.
    -   **alphanumeric**: The value can contain only letters, digits, and underscores (\_), and cannot start with a digit.
-   Existence verification
-   Run Script

 |
| Object/Array | Run Script |
| Integer | -   Common verification
    -   int32
    -   int64
-   Run Script

 |
| Decimal | -   Common verification
    -   double
    -   float
-   Run Script

 |
| Boolean | -   Run Script

 | **Parent topic:** [[Configuring the Element Validator|Configuring the Element Validator]]