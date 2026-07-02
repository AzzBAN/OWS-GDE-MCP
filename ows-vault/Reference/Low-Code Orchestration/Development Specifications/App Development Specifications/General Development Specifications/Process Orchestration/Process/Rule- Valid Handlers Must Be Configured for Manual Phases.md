---
title: "Rule: Valid Handlers Must Be Configured for Manual Phases"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162958980.html"
depth: 6
---
# Rule: Valid Handlers Must Be Configured for Manual Phases

**Description**: If no handler is configured for a manual phase or the handler is invalid (for example, the handler obtained through a variable is empty, or the user or group does not exist in the system), the system cannot dispatch the process to the correct handler. As a result, the process is suspended. Even if automatic submission is configured, the handler must be configured to prevent the SLA timeout and manual intervention failure due to delayed submission.

**Check guide**:

Open the process editor, select a phase, and view the configuration of **Assignments** in the **Main properties** area on the right.

**Positive example**:

1\. Handlers are configured for all manual processes, and correct handlers can be obtained during process transfer.

**Negative example**:

1\. No handler is configured for a manual phase.

![[en-us_image_0000001470084912.png]]

2\. A handler is configured for the manual phase, but the correct handler cannot be obtained during process transfer. For example, the handler obtained through a variable is empty, or the user or group does not exist in the system.

**Tool supported or not**: no

**Specification name**: General\_Process\_Valid\_Handler\_Must\_Be\_Configured\_for\_the\_Manual\_Node

**Severity**: major

**Parent topic:** [[Process|Process]]