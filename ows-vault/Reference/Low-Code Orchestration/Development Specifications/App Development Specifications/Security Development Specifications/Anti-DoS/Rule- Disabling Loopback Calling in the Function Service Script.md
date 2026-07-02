---
title: "Rule: Disabling Loopback Calling in the Function Service Script"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283732.html"
depth: 5
---
# Rule: Disabling Loopback Calling in the Function Service Script

**Description**: Calls initiated from a function service cannot be called back to the source function service in any way. Otherwise, cyclic calls may occur. If an infinite loop occurs in the script, a large number of performance resources are consumed. As a result, system resources are used up.

**Check guide**: Check whether the ServiceInvoker.post method is used in the function script and whether the calling address of the ServiceInvoker.post method is the release address of the script.

**Negative example**:

![[en-us_image_0000001471013932.png]]

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_FaaS\_Function\_Not\_CyclicCallback

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: function service

**Parent topic:** [[Anti-DoS|Anti-DoS]]