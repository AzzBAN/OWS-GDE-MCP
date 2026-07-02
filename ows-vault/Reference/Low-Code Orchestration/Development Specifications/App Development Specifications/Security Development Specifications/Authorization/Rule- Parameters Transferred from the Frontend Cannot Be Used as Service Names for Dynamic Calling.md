---
title: "Rule: Parameters Transferred from the Frontend Cannot Be Used as Service Names for Dynamic Calling"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403953.html"
depth: 5
---
# Rule: Parameters Transferred from the Frontend Cannot Be Used as Service Names for Dynamic Calling

**Description**: Another service can be called in JavaScript. If the called service is transferred as a parameter, an open service execution capability is provided, which may result in unauthorized access.

**Check guide**: Check whether the parameters transferred from the frontend are used as or combined with the service URI in the JavaScript code where another service is called.

**Negative example**:

The input parameter **service\_name** is directly used as the URI parameter of the called service, which may bring risks of unauthorized operations.

var service\_name = \_message.service\_name;
var request = {};
var response = ServiceInvoker.post(service\_name, request);

**Positive example**:

The URL is fixed during service calling.

var request = {};
var response = ServiceInvoker.post("/adc-batch/rest/v1/export-tasks/actions/create", request);

**Tool supported or not**: yes

**Specification name**: Security\_Authority\_InputParameter\_Is\_ServiceInvoke

**Category**: non-bottom-line check item

**Severity**: critical

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Authorization|Authorization]]