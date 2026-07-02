---
title: "Configuring a Customized Recorder"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001260563133.html"
depth: 5
---
#### Context

-   When Studio is started, it automatically reads the **userMapping.json** configuration file to check whether an available customized recorder exists.
    -   If parameters **title**, **class\_name**, and **process\_name** in the configuration file are empty, the customized recorder cannot be used because its configurations do not take effect.
    -   If at least one of the three parameters **title,** **class\_name**, and **process\_name** in the configuration file are set and the corresponding executable file is entered in **recorder\_file**, Studio automatically starts the customized recorder.
-   When a recording job is started in Studio, Studio first checks whether the recorded app meets all matching rules in the **userMapping.json** configuration file. If yes, Studio automatically forwards the recording-related message to the client specified by **url**. If no, the default forwarding rule is used.
    -   Check whether the value of **title** contains the name of the app that is being recorded.
    -   Check whether the values of **class\_name** and **process\_name** are the same as the class name and process name of the recorded app and are case sensitive.