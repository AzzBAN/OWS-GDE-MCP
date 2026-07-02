---
title: "Rule: Service Loopback Cannot Be Called"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804196.html"
depth: 5
---
# Rule: Service Loopback Cannot Be Called

**Description**: Calls initiated from a service cannot be called back to the source service in any way. Otherwise, cyclic calls may occur. If an infinite loop occurs in the script, a large number of performance resources will be consumed and the performance impact will last a period of time. The execution of the script with an infinite loop takes a long time, and the execution of the activity that the script belongs to also takes a long time. If the activity is a synchronous activity, performance of a data operation of a corresponding model is also affected.

**Check guide**: View the activities whose **Action** is **RunScript** on the develop-state page, and check whether an infinite loop exists in these scripts. The infinite loop can be the infinite loop of the script itself and the rule infinite loop caused by directly or indirectly modifying the model data that the rule belongs to.

Check whether the service that the script belongs to is directly or indirectly called in the script. If yes, ensure that the initial call can be ended within a small number of cyclic (or recursive) calling times.

**Negative example**:

1.  The script cannot be configured to recall the source service, that is, the source service cannot be cyclically called in the script.
    
    ![[en-us_image_0000001471322342.png]]
    
    The following figure shows how to call the service where the script is located.
    
    ![[en-us_image_0000001150523231.png]]
    
2.  The service call chain cannot contain cyclic call configurations.
    
    In the following figure, 1 -> 2 -> 1 forms a call loop. When configuring services, avoid service call loops. The number of times that a service is called is counted during service running. If the number is large, specifically, the loop is large, the loop is considered an infinite loop. To reduce the stack space and memory usage during service running, do not set a service call chain to an infinite loop.
    
    ![[en-us_image_0000001471330482.png]]
    
    ![[en-us_image_0000001521810053.png]]
    
    **Positive example**
    
    ![[en-us_image_0000001817466041.png]]
    
    ![[en-us_image_0000001687733520.png]]
    
    **Tool supported or not**: yes
    
    **Specification name**: Security\_DOS\_LogicFlow\_Not\_CyclicCallback
    
    **Category**: non-bottom-line check item
    
    **Severity**: minor
    
    **Orchestration scenario**: UI orchestration
    

**Parent topic:** [[Anti-DoS|Anti-DoS]]