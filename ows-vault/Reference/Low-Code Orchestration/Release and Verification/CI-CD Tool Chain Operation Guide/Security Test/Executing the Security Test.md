---
title: "Executing the Security Test"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_mate_security_test_run.html"
depth: 4
---
# Executing the Security Test

1.  On the **App Pipeline** tab page, click **Deliver**, and configure the environment, username, and password.
    
    **Figure 1** Page displayed after you click OK  
    ![[en-us_image_0000001829075049.png]]
    
    **Table 1** Parameters for setting the environment and login information  
    | Name | Description |
    | :-- | :-- |
    | Environment | Environment where the pipeline is to be executed. Select a desired one from the drop-down list. |
    | Username | User name of the human-machine user for logging in to the selected environment
    -   W3 accounts cannot be used to perform security tests.
    -   A human-machine user must be bound to a machine-machine user who has the machine-machine role **gam\_tenantadmin**.
    
     |
    | Password | Password of the human-machine user for logging in to the selected environment | 2.  After the environment and login information is configured, click **Deliver** and wait for the pipeline to perform the security test.

**Parent topic:** [[Security Test|Security Test]]