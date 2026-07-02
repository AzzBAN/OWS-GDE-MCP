---
title: "APIs Related to Event Registration and Triggering"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001733385106.html"
depth: 5
---
# APIs Related to Event Registration and Triggering

**Spl.EventBus.fireEvent(event,param)**

**Spl.EventBus.fireEvent(prefix,event,param)**

Used to send a custom event.

Input parameters:

**prefix** (string): event prefix

**event** (string): event name

**param** (string/object): event transfer parameter

Example:

// Do not transfer the parameter.
Spl.EventBus.fireEvent("event\_new");
// Transfer the parameter.
Spl.EventBus.fireEvent("event\_new",{"key":"value"});
// Include a prefix.
Spl.EventBus.fireEvent("task","data\_update",{"task\_id":"CM-001","reason":"new\_reason"});

**Spl.EventBus.register(event,callback)**

**Spl.EventBus.register(prefix,event,callback)**

Used to listen to custom events.

Input parameters:

**prefix** (string): event prefix

**event** (string): event name

**callback** (function): Callback method after an event is received. The parameter is the parameter transferred when the event is sent.

Example:

// Do not include a prefix.
Spl.EventBus.register("event\_new", function(param) {
console.log(param);
});
// Include a prefix.
Spl.EventBus.register("task","event\_new", function(param) {
console.log(JSON.stringify(param));
});

**Spl.EventBus.unregister(event,callback)**

**Spl.EventBus.unregister(prefix,event,callback)**

Used to cancel the listening on custom events.

Input parameters:

**prefix** (string): event prefix

**event** (string): event name

**callback** (function): Callback method after an event is received. The parameter is the parameter transferred when the event is sent.

Example:

// Do not include a prefix.
Spl.EventBus.unregister("event\_new", function(param) {
console.log(param);
});
// Include a prefix.
Spl.EventBus.unregister("task","event\_new", function(param) {
console.log(JSON.stringify(param));
});

**Observable**

**Spl.Observable.fireEvent(event,param)**

Used to send global events.

Input parameters:

**event** (string): event name

**param** (string/object): event transfer parameter

Example:

// Do not transfer the parameter.
Spl.Observable.fireEvent("event\_new");
// Transfer the parameter.
Spl.Observable.fireEvent("event\_new",{"key":"value"});

**Spl.Observable.on(event,callback)**

Used to listen to global events. Global events have a prefix of **Global.**, for example, **Global.event\_new**.

Input parameters:

**event** (string): event name

**callback** (function): Callback method after an event is received. The parameter is the parameter transferred when the event is sent.

Example:

Spl.Observable.on("event\_new", function(param) {
console.log(param);
})

**Parent topic:** [[JavaScript APIs|JavaScript APIs]]