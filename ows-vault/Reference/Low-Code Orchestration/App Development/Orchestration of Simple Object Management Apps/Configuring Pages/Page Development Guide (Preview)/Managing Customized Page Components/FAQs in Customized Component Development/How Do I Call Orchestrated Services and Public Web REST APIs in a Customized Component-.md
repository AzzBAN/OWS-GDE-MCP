---
title: "How Do I Call Orchestrated Services and Public Web REST APIs in a Customized Component?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_032.html"
depth: 7
---
#### Procedure

1.  Add the vigour-ui dependency to the **package.json** file. An example is as follows:
    
    "dependencies": {
        "@adc/vigour-ui": "1.10.143",
        "vue-i18n": "8.15.0",
        "jquery-ui": "^1.12.1"
      }
    
2.  Introduce the following tool classes to the header of the customized component:
    
    import { U, MessageProcessor } from "@adc/vigour-ui/lib/spl";
    
3.  Call the following service code in related codes:
    
    MessageProcessor.process({
            serviceId: "/chaos/modul1/modul1\_fangjihu\_get\_list",
            data: {
              start: 0,
              limit: 10
            },
            success: function (data) {
              console.log(JSON.stringify(data));
            }
          });
    
4.  To call the open web REST API, refer to the following codes:
    
    MessageProcessor.process({
            url: "/adc-ui/web/rest/v1/tenant-time-zone/current-time-zone",
            data: {
              zoneId: "UTC"
            },
            dataType: "text",
            method: "get",
            async: false,
            success: function (data) {
              console.log(JSON.stringify(data));
            },
            error: function (data) {
              console.log(JSON.stringify(data));
            }
          });
    
    MessageProcessor.process({
            url: " /adc-ui/web/rest/v1/tenant-time-zone/current-time-zone",
            dataType: "text",
            method: "get",
            async: false,
            success: function (data) {
              console.log(JSON.stringify(data));
            },
            error: function (data) {
              console.log(JSON.stringify(data));
            }
          });