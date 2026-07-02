---
title: "APIs Related to Event Registration and Triggering"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001316638968.html"
depth: 9
---
# APIs Related to Event Registration and Triggering

The Spl.EventBus.fireEvent(event,param) API is used to trigger the customized event.

  
| Parameter | Property | Description |
| :-- | :-- | :-- |
| event | String | Event name |
| param | String/Object | Event transfer parameter | Example:

// Do not transfer the parameter.
Spl.EventBus.fireEvent("event\_new");
// Transfer the parameter.
Spl.EventBus.fireEvent("event\_new", { key: "value" });
// Register a customized event.
Spl.EventBus.register(event,callback)

  
| Parameter | Property | Description |
| :-- | :-- | :-- |
| event | String | Event name |
| callback | Function | Callback method after an event is received. The parameter is the parameter transferred when the event is sent. | Example:

Spl.EventBus.register("event\_new", function (param) {
  console.log(param);
});

Deregister a customized event. (When the input parameter requires callback, the callback function of a cancellation event must be the same as that of a listening event.)

Spl.EventBus.unregister(event,callback)

Example:

Nf.PageReady(function(){
// Register an event.
  Spl.EventBus.register("event\_new", function(param){
    console.log(param)
  });
// Trigger the registered event.
  C("wltest1").on("click", function(){
    Spl.EventBus.fireEvent("event\_new","111");
  })
// Deregister the customized event.
  C("wltest2").on("click", function(){
    Spl.EventBus.unregister("event\_new");
  });
})

The Spl.Observable.fireEvent(event) and Spl.Observable.fireEvent(event,param) APIs are used to trigger the global events.

The Spl.Observable.on(event,callback) API is used to register the global event.

The Spl.Observable.un(event,callback) API is used to unbind the global event.

**Parent topic:** [[APIs Related to Request Services and Event Registration|APIs Related to Request Services and Event Registration]]