---
title: "Suggestion: Do Not Store or Transfer a Large Number of Large Objects "
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403821.html"
depth: 6
---
# Suggestion: Do Not Store or Transfer a Large Number of Large Objects

**Description**: Do not store a large number of (more than 1000) large objects (objects whose properties exceed 200 and array length exceeds 1000) to prevent excessive occupation of memory and network resources, which may cause system memory overflow and slow response.

**Check guide**:

Check whether the JS script continuously adds records to the collection. The collection property in the JS script cannot add objects to the collection without restrictions.

Check whether the JS script frequently uses a large number of large objects as the parameters for calling other services.

**Negative example**:

var objects = \[\]
for (var i = 1;i<10000;i++){
var request = {}
var response = ServiceInvoker.post("/adc-service/rest/v1/services/xxys/test1/test1\_alarm\_get\_list", request);
    objects.push(response)
}

**Tool supported or not**: no

**Specification name**: General\_Service\_Avoids\_Hold\_or\_Transfer\_Huge\_Large\_Objects

**Severity**: suggestion

**Parent topic:** [[Service|Service]]