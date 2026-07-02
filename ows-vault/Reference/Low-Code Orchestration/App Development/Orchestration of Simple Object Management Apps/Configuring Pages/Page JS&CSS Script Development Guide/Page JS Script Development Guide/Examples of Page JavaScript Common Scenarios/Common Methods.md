---
title: "Common Methods"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_page_js_002.html"
depth: 7
---
# Common Methods

-   Clears the value of a specified item in the local storage.
    
    Spl.StorageEventBus.clearItem(name)
    
-   Opening a page
    
    Spl.Page.open(url, config, params)
    
-   Closing a page
    
    Spl.Page.close()
    
-   Setting the page title
    
    Spl.Page.setTitle(title)
    
-   Opening a page in the dialog box mode
    
    Spl.Window.open(options)
    
-   Closing a page in the dialog box mode
    
    Spl.Window.close()
    
-   Obtaining the logic to be loaded during page loading
    
    Nf.ready(function(){})
    U.ready(function(){})
    
-   Obtaining the tenant ID
    
    U.getTenantId()
    
-   Obtaining the app name
    
    U.getAppName()
    
-   Obtaining the name of a module in an app
    
    U.getModuleName()
    
-   Obtaining the name of a page
    
    U.getPageName()
    
-   Obtaining the context path
    
    U.getContextPath()
    
-   Obtaining the time zone information
    
    U.getTimeZone()
    
-   Error dialog box. The options are as follows: **confirm**, **alert**, **success**, **info**, **risk**, and **highRisk**.
    
    U.promptError(options, ctx)
    
-   Obtaining a component instance
    
    S(id)
    
-   Obtaining a parameter in a URL request
    
    U.getUrlParameter(key) 
    
-   Obtaining all parameters in a URL
    
    U.getUrlParameters()
    
-   Obtaining a component object on the parent page
    
    Spl.ParentPage.S(id)
    

**Parent topic:** [[Examples of Page JavaScript Common Scenarios|Examples of Page JavaScript Common Scenarios]]