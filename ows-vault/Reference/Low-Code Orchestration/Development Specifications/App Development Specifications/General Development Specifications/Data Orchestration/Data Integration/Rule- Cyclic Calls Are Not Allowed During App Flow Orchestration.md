---
title: "Rule: Cyclic Calls Are Not Allowed During App Flow Orchestration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001604352964.html"
depth: 6
---
# Rule: Cyclic Calls Are Not Allowed During App Flow Orchestration

**Specification name**: General\_DataFactory\_AIP\_Avoiding\_Cyclic\_Dependencies

**Description**: When the HttpListener(S), HttpRequest, SocketsListener(S), SocketsSender, KafkaConsumer(S), KafkaProducer, WMQSender, WMQReceiver(S), Compress, or Uncompress operator is used to orchestrate app flows, if cyclic calls are involved, a large number of system resources are occupied, and even the system may become unavailable.

**Check guide**:

-   Check whether the HttpListener(S) and HttpRequest operators use the same address (that is, same request address, host, and port). If yes, a cyclic call is involved. (The check method for SocketsListener(S) and SocketsSender is similar.)
-   Check whether the KafkaProducer and KafkaConsumer(S) operators have the same data source and consumption topic. If yes, a cyclic call is involved.
-   Check whether the server address, port, topic, and queue of the WMQSender operator are the same as those of the WMQReceiver(S) operator. If yes, a cyclic call is involved.
-   Check whether the input file path of the Compress operator is the output file path of the Uncompress operator, or the output file path of Compress is the input file path of Uncompress. If yes, the decompressed file will be compressed again or the compressed file will be decompressed again, and a cyclic call is involved.

The operators in these checks may be on a single canvas, on different canvases of the same app, or on different canvases different apps.

**Negtive example**: For the HttpListener(S) operator, the actual host IP address is 10.0.0.1, the port is 8080, and the request address is **/appname/rest/aip/test**. For the HttpRequest operator, the requested host IP address is 10.0.0.1, the port is 8080, and the request address is **/appname/rest/aip/test**.

-   Parameter configuration of the HttpListener(S) operator is as follows:
    
    -   The value of **HTTP\_ROUTE\_PREFIX** in the runtime-state environment is **/appname/rest/aip/**.
    -   The value of **SERVICE.LISTEN.IP** in the runtime-state environment is **10.0.0.1**.
    -   The value of **SERVICE.LISTEN.PORT** in the runtime-state environment is **8080**.
    
    **Figure 1** HttpListener(S)  
    ![[en-us_image_0000001654214589.png]]
    

-   Parameter configuration of the HttpRequest operator is as shown in the following figure.
    
    **Figure 2** HttpRequest  
    ![[en-us_image_0000001654574329.png]]
    

**Impact**: Cyclic calls occupy a large number of system resources and may even cause system unavailability.

**Parent topic:** [[Data Integration|Data Integration]]