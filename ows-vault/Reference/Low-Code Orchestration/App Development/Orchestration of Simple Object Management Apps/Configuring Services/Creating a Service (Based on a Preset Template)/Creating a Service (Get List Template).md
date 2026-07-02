---
title: "Creating a Service (Get List Template)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_020.html"
depth: 5
---
#### Context

After a **Get List** template is selected and is associated with a model, the generated service automatically generates input and output parameters based on the model.

There is a property type conversion from model fields to service input and output parameters. By default, the conversion is performed based on the following rules:

-   The output for the field of the reference type on the model side is an ID, which is translated into a key code on the service side.
-   The output for the field of the file type on the model side is a token, which is translated in to a JSON array on the service side. The JSON array contains detailed information about each file.
-   The output for the field of the password type on the model side is ciphertext, which is translated into an empty string on the service side.
-   The output for the field of the user and user group type on the model side is user:id group:id, which is translated to user:name group:name on the service side.

You can modify the conversion rules through configuration.