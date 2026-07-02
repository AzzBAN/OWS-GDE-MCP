---
title: "About Network Operation Automation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/mcp_002.html"
depth: 3
---
# About Network Operation Automation

Network O&M personnel, especially senior network O&M personnel, need to perform routine adjustments to network configurations. They need to modify scripts based on their understanding of network products and deliver the scripts to the network through devices or EMS clients. Application Development Center (ADC) provides network operation automation modules with the corresponding orchestration capabilities to standardize and automate routine network configuration change actions. This improves the efficiency of network configuration change actions and reduces network failures caused by manual operations.

In the develop-state environment, the configuration of the network operation automation module includes the configuration items inside and outside the project.

![[en-us_image_0000001133727594.png]]

Basic concepts related to network operation automation are as follows:

-   **Command**
    
    Commands are used by senior network O&M personnel to change routine network configurations. Commands are classified into the following types: general commands, diagnosis commands, proactive maintenance commands, and configuration commands. The execution of diagnosis, configuration, and proactive maintenance commands depends on OWS model APIs. Therefore, the three types of commands are used only in the OWS O&M automation domain. In other domains, general commands are used.
    
-   **Script**
    
    Service personnel can compile commands to be sent to devices or EMS clients in Python scripts and associate the commands with scripts to directly execute scripts when commands are executed
    
-   **Application scenario**
    
    When the asset development team needs to enable the interworking with devices or EMSs and perform operations such as querying and changing device information, network operation automation can be configured.
    
-   **Implementation principle**
    
    The network operation automation module provides a command-related API. Service development personnel can call this API to transfer the login information of the target EMS and device so that the MCP probe can interwork with the target EMS and device. At the same time, the MCP probe sends the commands and returns the execution results to the service development personnel.
    

**Parent topic:** [[Network Operation Automation|Network Operation Automation]]