---
title: "Basic Usage"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adcui/commonUsage.html"
depth: 5
---
#### Page Registration Event and Triggering Event

Example 1 – Component value change event

//For details about the event name, see the component document.

Spl.EventBus.register(id, eventName, func); //Registration event

Spl.EventBus.fireEvent(id, eventName, params); //Triggering event

Example 2 – Button click event

Spl.EventBus.register("operation", "click", function (event) {
    //todo
});

Example 3 – Form-related events

//Event after form submission

Spl.EventBus.register('ticket\_ticketForm', 'after-submit', function (event) {

    result = event.data.result;

    id = event.data.id;

});

//Event before form submission

Spl.EventBus.register('ticket\_ticketForm', 'before-submit', function (event) {

    //**event.data** stores the data to be submitted.

});

//Form submission success event

Spl.EventBus.register('templateForm', 'submit-success', function (event) {

    //TODO

});