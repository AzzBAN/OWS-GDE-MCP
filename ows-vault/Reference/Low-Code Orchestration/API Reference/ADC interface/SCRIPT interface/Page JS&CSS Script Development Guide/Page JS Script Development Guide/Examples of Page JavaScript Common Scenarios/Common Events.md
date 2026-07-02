---
title: "Common Events"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_page_js_004.html"
depth: 7
---
# Common Events

An event is a program response that is automatically triggered by some behaviors on a web page. You can customize the response content by registering an event.

The actions include page loading completion, input field change, button clicks, and so on.

-   Registration event: Spl.EventBus.register(id, eventName, callback)
-   Triggering event: Spl.EventBus.fireEvent(id, eventName, params)
-   Cancellation event: Spl.EventBus.unregister(id, eventName, callback)
-   Use the event processing component to register the table refresh and load events with the DataGrid registration table.
    
    // grid\_after\_refresh event: Triggered after the table is refreshed.
    Spl.EventBus.register('datagrid', 'grid-after-refresh', function(param){ });
    // Load event
    Spl.EventBus.register("datagrid", "load", function(data){ });
    
-   Use the event processing component behavior: TreePanel node operation.
    
    // Click a node to trigger an event.
    Spl.EventBus.register("Component ID", "node-click", function(){ })
    // Double-click a node to trigger an event.
    Spl.EventBus.register("Component ID", "db-click", function(){ })
    // Event triggered when a node is expanded
    Spl.EventBus.register("Component ID", "expand", function(){ })
    
-   Use the event processing component behavior: BorderLayoutPanel collapse operation.
    
    // Subpanel collapse event
    Spl.EventBus.register("Border layout component ID", "collapse", function(args){ })
    // region-panel folding event
    Spl.EventBus.register("Border layout component ID", "border-west-collapse", function(args){ })
    

**Parent topic:** [[Examples of Page JavaScript Common Scenarios|Examples of Page JavaScript Common Scenarios]]