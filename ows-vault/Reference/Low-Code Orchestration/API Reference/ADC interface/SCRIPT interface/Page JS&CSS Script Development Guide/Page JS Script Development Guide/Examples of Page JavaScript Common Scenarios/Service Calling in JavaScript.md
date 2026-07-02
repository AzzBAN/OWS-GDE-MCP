---
title: "Service Calling in JavaScript"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_page_js_006.html"
depth: 7
---
#### Calling a Service in a Project

	// App service mode
	MessageProcessor.process({
        "serviceId": "/projectName/moduleName/serviceName",
        "async": false,
        "data": p,
        "success": function (data) {
            result = data;
        }
    });