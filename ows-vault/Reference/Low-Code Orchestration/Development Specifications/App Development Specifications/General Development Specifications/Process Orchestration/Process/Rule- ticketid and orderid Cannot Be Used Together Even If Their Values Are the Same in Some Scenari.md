---
title: "Rule: ticketid and orderid Cannot Be Used Together Even If Their Values Are the Same in Some Scenarios"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283628.html"
depth: 6
---
# Rule: ticketid and orderid Cannot Be Used Together Even If Their Values Are the Same in Some Scenarios

**Description**: When an API provided by ADC is used to query the workflow instance and ticket information, if the API returns **orderid** which indicates the ticket ID or **ticketid** which indicates the process instance ID at the same time, the values of the two parameters may be different. Even if the values are the same, the service meanings are different, you can use the value of **ticketid** as a ticket ID.

**Check guide**: Check the script which uses an API for operating tickets, check the input and output parameters of the API, determine whether the parameters are **orderid** or **ticketid**, and transfer the corresponding parameter as required.

**Positive example**:

In this example, the API requires that the **ticketid** parameter be transferred.

![[en-us_image_0000001166297085.png]]

**Negative example**:

1\. In this example, the API requires that the **ticketid** parameter be transferred. Actually, the **orderid** parameter is transferred. If the values of the two parameters are different, the API fails to be called.

![[en-us_image_0000001119537302.png]]

2\. In this example, the values of **orderid** and **ticketid** are reversed. When the two values are different, the API fails to be called.

![[en-us_image_0000001119377384.png]]

**Tool supported or not**: no

**Specification name**: General\_Process\_Forbidden\_Mix\_TicketID\_and\_OrderID

**Severity**: major

**Parent topic:** [[Process|Process]]