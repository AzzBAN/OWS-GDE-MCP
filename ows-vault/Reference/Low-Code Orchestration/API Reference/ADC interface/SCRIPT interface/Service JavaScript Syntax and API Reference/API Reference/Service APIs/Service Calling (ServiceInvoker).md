---
title: "Service Calling (ServiceInvoker)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_023.html"
depth: 7
---
# Service Calling (ServiceInvoker)

In JavaScript, the ServiceInvoker interface can be used to call the CSE service.

Request and response messages can only be encoded in the application/json type. The request and response message bodies must be JSON objects and cannot be JSON arrays or texts in other formats.

Message headers cannot be transferred or obtained.

The execution time of the called service is controlled by the timeout interval (usually 1 minute) of the CSE client. The timeout interval varies depending on product specifications and cannot be specified in a script.

**Table 1** Service calling API description   
| API | Description | Example |
| :-- | :-- | :-- |
| ServiceInvoker.get(uri \[ , uriParams \]) ServiceInvoker.delete(uri \[ , uriParams \]) | Used to call the CSE service synchronously. Parameters:
-   **uri**: URI of the CSE service. Its value is a string.
-   **uriParams**: URI parameter of the object type. This parameter is optional.

Returned value: Response message body, which is of the object type. When a service fails to be called, an error is reported. | var requestMessage = {
    "uri": "/project1/module1/book",
    "start": 0,
    "limit": 10,
    "condition\_tql": "author = 'Tom'"
};
ServiceInvoker.post("/adc-model/rest/v1/model-instances/baseinstances-find", requestMessage);

 |
| ServiceInvoker.post(uri ,message \[ , uriParams \]) | Used to call the post service of CSE synchronously. Parameters:

-   **uri**: URI of the CSE service. Its value is a string.
-   **message**: Message body of a request. Its value is an object.
-   **uriParams**: URI parameter of the object type.

Returned value: Response message body of the object type. This parameter is optional. When a service fails to be called, an error is reported. |
| ServiceInvoker.invoke(uri ,message \[ , uriParams \]); | Same as the above. |
| ServiceInvoker.patch(uri ,message \[ , uriParams \]); | Used to call the patch service of CSE synchronously. Parameters:

-   **uri**: URI of the CSE service. Its value is a string.
-   **message**: Message body of a request. Its value is an object.
-   **uriParams**: URI parameter of the object type. This parameter is optional.

Returned value: Response message body, which is of the object type. When a service fails to be called, an error is reported. |
| ServiceInvoker.put(uri , message \[ , uriParams \]); | Used to call the put service of CSE synchronously. Parameters:

-   **uri**: URI of the CSE service. Its value is a string.
-   **message**: Message body of a request. Its value is an object.
-   **uriParams**: URI parameter of the object type. This parameter is optional.

Returned value: None | **Parent topic:** [[Service APIs|Service APIs]]