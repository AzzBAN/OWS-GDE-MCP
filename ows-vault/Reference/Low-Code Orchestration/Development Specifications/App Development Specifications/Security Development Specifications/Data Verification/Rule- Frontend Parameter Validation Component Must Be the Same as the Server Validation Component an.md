---
title: "Rule: Frontend Parameter Validation Component Must Be the Same as the Server Validation Component and the Final Validation Must Be Performed on the Server"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643465.html"
depth: 5
---
# Rule: Frontend Parameter Validation Component Must Be the Same as the Server Validation Component and the Final Validation Must Be Performed on the Server

**Description**: GDE provides the back-end service parameter validation component and the front-end parameter verification component. The front-end parameter validation component must be the same as the back-end service validation component to prevent inconsistency between the front-end and back-end validation. When the back-end service parameter validation is less strict than the front-end service parameter validation, the front-end validation is skipped, causing security risks. All parameters must be validated, and the final validation must be performed at the backend.

**Check guide**: Log in to the develop-state environment, select a desired app, and check the pages one by one. If the parameter validation information is set on the page, check whether the same validation is performed for the parameter in the service in which the parameter setting is submitted. In principle, the validation information must be the same. In special cases, the validation strictness at the backend can be higher than that at the frontend, but cannot be lower than that at the frontend.

**Positive example**:

1.  Check whether parameter validation rules are configured at the frontend.
    
    ![[en-us_image_0000001524383085.png]]
    
2.  View the service that submits the corresponding form.
    
    ![[en-us_image_0000001472860048.png]]
    
    **Tool supported or not**: yes
    
    **Specification name:** Security\_DataCheck\_Inconsistency\_Between\_TheForegroundAndBackground
    
    **Category**: non-bottom-line check item
    
    **Severity**: minor
    
    **Orchestration scenario**: UI orchestration
    

**Parent topic:** [[Data Verification|Data Verification]]