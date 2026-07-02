---
title: "Rule: Returning Excessively Large Command Output Is Forbidden in the Python Command Script"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963772.html"
depth: 5
---
# Rule: Returning Excessively Large Command Output Is Forbidden in the Python Command Script

**Description**: Users can compile logic in the Python script to return the command output to the upper layer. However, returning excessively large command output is not allowed in the returned result. The command output size cannot exceed 2 MB. If it exceeds 2 MB, the command output may be truncated.

**Check guide**: Check the process of constructing the command output in the script and ensure that the size of the returned command output does not exceed 2 MB.

**Tool supported or not**: yes

**Specification name**: General\_MCP\_Forbidden\_Return\_Oversized\_Results\_in\_Python\_Instruction\_Scripts

**Severity**: major

**Parent topic:** [[Network Operation Automation|Network Operation Automation]]