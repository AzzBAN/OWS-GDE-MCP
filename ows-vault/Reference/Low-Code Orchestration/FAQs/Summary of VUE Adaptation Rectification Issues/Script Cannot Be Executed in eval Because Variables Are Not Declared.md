---
title: "Script Cannot Be Executed in eval Because Variables Are Not Declared"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500896.html"
depth: 3
---
# Script Cannot Be Executed in eval Because Variables Are Not Declared

**pageScriptName: um\_userBasicInfo\_script1**

clickUserTenants = function(data,tenant\_id)
    {
      Nf.promptWindow({
        title:Nf.res("usermgt.tenant.tenantinfo"),
        message : '/app/'+tenantId+'/spl/system/sys\_tenantinfo\_readonly.spl?tenant\_id='+tenant\_id ,
        height : 400,
        winPos:'c',
        closeBtn:true,
        width : 850,
        iframe:true
      });
    }

**Solution:** The script is executed in eval and does not use **var**, **let**, or **const** to declare variables. This issue can be resolved only by modifying jsLib.

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]