---
title: "Data Source"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_105.html"
depth: 6
---
#### Procedure

1.  Select **Inbound API** or **Outbound API** as required and click **Design API**.
2.  Go to the **Common Definition** tab page.
    
    Click **Common Definition** of the **Design API** page. The **Common Structure** tab page is displayed by default.
    
    **Figure 1** Accessing the Common Definition page  
    ![[en-us_image_0000001623984341.png]]
    
3.  Choose **Data Source** in the navigation pane.
4.  Add a data source.
    
    **Table 1** Data source parameters   
    | Data Source | Add Method | Description |
    | :-- | :-- | :-- |
    | RabbitMQ | Click and configure basic information as prompted. | Set Address, Port, and TLS enable flag based on site requirements. |
    | ActiveMQ | Enter the username and Broker URL based on site requirements. |
    | Complying with JMS specifications | User-defined name. |
    | JetMQ | Click Add Destination. | For details, see Table 2. | 5.  Configure the data source.
    
    -   Adding a host
        
        Configure the host information of the message middleware of the RabbitMQ type as prompted.
        
    -   Adding a destination
        
        Configure the asset information about the message middleware of the JetMQ, ActiveMQ, or custom type (JMS-compliant products) as prompted. The details are as follows.
        
        ![[en-us_image_0000001649379922.png]]
        
        **Table 2** Parameters  
        | Parameter | Description |
        | :-- | :-- |
        | Name | User-defined name. |
        | Product | Type of the message middleware. |
        | Type | Message sending and receiving mode of the message middleware. The options are as follows:
        -   **Queue**
        -   **Topic**
        
         |
        | Message Type | Type of messages sent and received by the message middleware. The options are as follows:
        
        -   **Text**
        -   **Bytes**
        -   **Map**
        
        The default value is Text. |
        | Response Queue | Response queue of the message middleware. |
        | Message Priority | Message priority of the message middleware. When messages are sent and received through the middleware that references the asset, the messages are sent and received based on the message priority of the asset. The priority ranges from 0 to 9. The priority increases with the value. |
        | Persistence Mode | Persistence mode of the message middleware. The options are as follows:
        
        -   **Non Persistent**
        -   **Persistent**
        
         |
        | Answer Mode | Response mode of the message middleware. The options are as follows:
        
        -   **Auto Acknowledge**
        -   **Client Acknowledge**
        
        The default value is Auto Acknowledge. | 6.  After adding a destination or host, configure the destination or switch.
    
    **Table 3** Parameter description  
    | Data Source | Configuration |
    | :-- | :-- |
    | RabbitMQ | After the host is added, click Add Switch and configure the switch information as prompted. |
    | ActiveMQ | 
    1.  After the destination is added, click the destination. The details page is displayed.
    2.  Click the plus sign (+) next to the destination name and add a value of **Queue** or **Structure**.
    3.  Set the request/response parameters of the destination based on site requirements. For details about the configuration, see [[JetMQ-ActiveMQ-EXTJMSMQ|JetMQ/ActiveMQ/EXTJMSMQ]].
    
     |
    | JetMQ |
    | Complying with JMS specifications | In the GTS Product Convergence Solution, when the API Fabric is used to forward messages, select the message forwarding acknowledge mode based on site requirements, as shown in the following figure.
    
    **Figure 2** Acknowledge Mode  
    ![[en-us_image_0000001649385738.png]]
    
    -   **No acknowledge mode**: Messages are not forwarded.
    -   **automatic acknowledgment** (default): Messages are forwarded automatically.
    -   **manual acknowledgment**: Messages are forwarded only after being acknowledged by the system.