---
title: "Adding an API"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_110.html"
depth: 6
---
#### Context

The protocols supported for manual adding and adding by ZIP file import are different.

-   Manual adding
    
    APIs of custom protocols can be added using the API Designer.
    
    1.  REST
    2.  RabbitMQ
        
        RabbitMQ is a northbound protocol and does not support endpoint management configuration.
        
    
-   Adding an API by importing existing files
    1.  SOAP
    2.  REST
        
        One or more XSD files (except a single YAML file) can be directly imported. (Multiple XSD files need to be compressed into a ZIP package.)