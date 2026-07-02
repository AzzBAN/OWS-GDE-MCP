---
title: "Exception Diagram Element Usage"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_084.html"
depth: 5
---
#### Context

In the API development process, the method in the endpoint is invoked. An exception occurs during invocation. In this case, you need to add the exception capture diagram element to the diagram element orchestration so that the exception cause can be accurately located during API test.

The process variable **\_exception** is preset in the exception capture diagram element. The variable contains the **\_exception.name** and **\_exception.cause**. **\_exception.name** indicates the name of an exception, and **\_exception.cause** indicates the details of the exception.