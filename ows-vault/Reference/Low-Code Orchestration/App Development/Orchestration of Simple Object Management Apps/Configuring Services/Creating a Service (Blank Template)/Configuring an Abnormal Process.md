---
title: "Configuring an Abnormal Process"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_053.html"
depth: 5
---
#### Context

Exception handling: On the model operation and common operation nodes, you need to configure **Exception Handling** to determine whether to ignore exceptions.

-   If **Ignore** is selected, exceptions will be ignored.
-   If **Ignore** is not selected, the exception branch or process is used when an exception occurs. By default, this check box is not selected.
    -   Abnormal branch: For a node that has been connected, drag the edge point again and add a node branch to connect to the node. If an exception occurs on a node that has an exception branch, the exception branch is preferentially used.
    -   Exception process: process started from the exception node, which is similar to try catch in the code to capture exceptions. After the exception node is configured, if an operation exception occurs in a service and no exception branch exists, the exception process is automatically executed.
        
        ![[en-us_image_0000001121755218.png]]