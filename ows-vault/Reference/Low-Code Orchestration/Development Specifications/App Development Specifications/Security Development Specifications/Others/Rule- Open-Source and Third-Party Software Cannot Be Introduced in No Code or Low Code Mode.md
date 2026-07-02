---
title: "Rule: Open-Source and Third-Party Software Cannot Be Introduced in No Code or Low Code Mode"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349123768.html"
depth: 5
---
# Rule: Open-Source and Third-Party Software Cannot Be Introduced in No Code or Low Code Mode

**Description**: The improper use of the open-source and third-party software may cause the intellectual property rights (IPR), vulnerabilities, and legal risks. Therefore, in the No Code or Low Code scenario, the open-source or third-party software cannot be introduced through the ways that include but not limited to following:

-   Overall replication: Developers copy the open-source and third-party software as self-developed assets to the asset package.
-   Fragment reference: Developer copy only some code of open-source and third-party software to the asset package.
-   External links: Developers reference the external URLs of the open-source and third-party software on pages.
    
    ![[notice_3.0-en-us.png]]
    
    If developers introduce the open-source or third-party software into the asset package in any form, the mode automatically switches to the Pro Code mode from the No Code or Low Code mode. In the Pro Code mode, developers are responsible for security responsibilities. The quick test process cannot be adapted to. The asset package can be released only after passing the ICSL test.
    

**Check guide**: Check the asset configuration and code.

**Note**: For development teams that have deployed CloudDragon, you can integrate FOSSbot with the CloudDragon pipeline to scan the open-source software.

**Tool supported or not**: yes

**Specification name**: Security\_Others\_Forbid\_Import\_OpenSourceSoftwareAndThirdPartySoftware

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: all

**Parent topic:** [[Others|Others]]