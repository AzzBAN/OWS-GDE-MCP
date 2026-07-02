---
title: "Security Statement"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001167375506.html"
depth: 5
---
# Security Statement

This section describes possible security risks when RPA is used and provides operation suggestions.

When RPA is used, the following security risks may exist. Read the following content and perform operations based on suggestions:

-   If sensitive information or personal data is used during development, the information may be disclosed. You are advised to obtain user authorization, plan the saving and export locations of the project before development, and delete the local project information after the design is complete to prevent other users from obtaining the information.
-   RPA provides security protection for robots by means of prompt messages, role permission separation, and whitelist control for high-risk commands. However, due to business scenario requirements, users can record any operation and develop executable scripts such as Python scripts. Therefore, users are liable for the security risks caused by these operations and executable scripts. Save a project in a specific user directory to prevent the project from being tampered with or attacked by other users. Exercise caution when opening a project whose source is unknown.
-   You are advised to isolate physical executors from other systems and install antivirus software. If some antivirus software detects that the agent software and executor software are malicious, configure a whitelist for antivirus software.
-   You are advised to install and use RPA as a user with low permissions in **C:\\Program Files**. Users need to pay attention to and bear the security risks caused by operations such as executor installation and use by high-privilege users due to business scenario requirements.
-   When email-related controls are used, RPA performs security hardening for information bombing. A single chatbot can send emails to a maximum of 100 recipients at the same time, and can send emails to the same recipient for a maximum of 20 times at an interval of 0.5 seconds.
-   When Excel controls are used, macros or formulas can be used to process Excel and CSV data based on service requirements. However, data-driven engine (DDE) injection attacks may be caused. Exercise caution when performing this operation.
-   When file processing controls are used, the capabilities of the OS are used to operate the file system. Consider the impact on the file system during development. Do not write large files, delete temporary files, or delete important files by mistake.
-   RPA restricts the types and sizes of files in a compressed package to prevent the import of .zip compression bombs (compressed packages that are suspicious and generate a large amount of data after decompression).

Besides, you understand and agree that your use of the Service must comply with applicable laws and regulations. We only provide a standard service upon your requests and are not responsible for the legal compliance of your use.

**Parent topic:** [[Quick Start|Quick Start]]