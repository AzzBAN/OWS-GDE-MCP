---
title: "Suggestion: Do Not Call External APIs Cyclically in Scripts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283576.html"
depth: 6
---
# Suggestion: Do Not Call External APIs Cyclically in Scripts

**Description**: In the script, ServiceInvoker can be used to call APIs of other microservices. This prevents the service calling from being time-consuming due to cyclic calling of external APIs in the script. Batch processing APIs provided by external systems can also be used.

**Check guide**: Check whether ServiceInvoker exists in a loop.

**Positive example**: ServiceInvoker.post("/project/module/service",req)

**Negative example**:

for(var i=0;i<num;i++){

ServiceInvoker.post("/adc-model/rest/v1/xxx",req)

}

**Tool supported or not**: no

**Specification name**: General\_Service\_Start\_Value\_Cannot\_Exceed\_10000

**Severity**: suggestion

**Parent topic:** [[Service|Service]]