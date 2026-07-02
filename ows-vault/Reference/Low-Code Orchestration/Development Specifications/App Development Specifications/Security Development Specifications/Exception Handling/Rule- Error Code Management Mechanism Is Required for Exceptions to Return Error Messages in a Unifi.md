---
title: "Rule: Error Code Management Mechanism Is Required for Exceptions to Return Error Messages in a Unified Manner"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403969.html"
depth: 5
---
# Rule: Error Code Management Mechanism Is Required for Exceptions to Return Error Messages in a Unified Manner

**Description**: When an exception occurs, information that is useful to attackers, such as the database version, database structure, OS version, stack tracing, file name and path information, and TQL query string, cannot be returned to the client. The information can be used by attackers to initiate further attacks. It is recommended that a unified and default error message page be redirected for information filtering.

**Check guide**: Check whether the unified exception page customized by GDE is used. When the developer develops apps, an error code is displayed for the user.

**Positive example**:

![[en-us_image_0000001471192416.png]]

**Note**: This rule focuses on whether the error code management mechanism is used. For details about how to use defined error code, see **GDE** **Orchestration** > **Basic Orchestration Configuration** > **General Job Orchestration** > **Configuring Error Codes** in GDE product documentation.

**Tool supported or not**: yes

**Specification name**: Security\_Exception\_ShouldUseErrorCode

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Exception Handling|Exception Handling]]