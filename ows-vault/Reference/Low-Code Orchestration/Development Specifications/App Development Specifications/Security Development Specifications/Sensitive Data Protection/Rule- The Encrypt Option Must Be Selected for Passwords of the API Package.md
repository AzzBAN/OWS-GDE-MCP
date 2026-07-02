---
title: "Rule: The Encrypt Option Must Be Selected for Passwords of the API Package"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123744.html"
depth: 5
---
# Rule: The Encrypt Option Must Be Selected for Passwords of the API Package

**Description**: During app development, project-level public parameters can be configured. The password for connecting to a third-party system can be configured. If **Encrypt** is not selected for the password, the unencrypted password is directly displayed and stored.

**Check guide**: Log in to the develop-state environment, go to the project management page, select the project to be checked, click **Edit**, and check whether there is a password whose **Encrypt** is not selected.

**Positive example**:

1.  Choose **Project Management**, select the project package to be checked, and choose **More** > **Common Parameter Configuration**.
    
    ![[en-us_image_0000001471525848.png]]
    
    ![[en-us_image_0000001522246169.png]]
    
2.  Select the common parameter related to the sensitive data to be checked and check whether the **Encrypt** option is enabled.
    
    ![[en-us_image_0000001471526364.png]]
    
    Specific example:
    
    ![[en-us_image_0000001471047460.png]]
    

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_InterfaceParam\_NotUsePasswordType

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: API orchestration - API integration and orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]