---
title: "Rule: Services and Rules Cannot Be Dramatically Called"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643325.html"
depth: 6
---
# Rule: Services and Rules Cannot Be Dramatically Called

**Description**: To prevent CPU peak or service response delay, do not use the following typical scenarios during script development:

1\. A large amount of data is operated in JavaScript, which increases the memory usage and service response time.

2\. A large amount of data in the model triggers rules. The JavaScript script triggered by the rules uses a loop, which increases the CPU consumption.

**Check guide**:

-   Check whether a large amount of data is queried and processed in the script, especially whether a large number of cyclic nested operations are performed.
-   Check whether a large number of rules are triggered and whether the rules trigger other rules in cascading mode.

**Positive example**:

while(list.hasNext())
{
//Processing logic
}
ServiceInvoker.post("/adc-service/rest/v1/events/fire/{projectName}/{moduleName}/{eventName}", request);

**Negative example**:

while(list.hasNext())
{
    ServiceInvoker.post("/adc-service/rest/v1/events/fire/{projectName}/{moduleName}/{eventName}", request);
}

**Tool supported or not**: no

**Specification name**: General\_Service\_Avoid\_Large\_Number\_of\_Service\_Invoking\_and\_Triggering\_JS\_Invoking

**Severity**: minor

**Parent topic:** [[Service|Service]]