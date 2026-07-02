---
title: "Developing a Script Task Node"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_studio_guide_workflow_0033.html"
depth: 4
---
#### Usage Description (New Assets)

The new engine uses JavaScript in a unified manner. Variables and methods specific to BPM are extended and implemented based on the new JavaScript engine framework in CommonSDK for script task to compile and execute JavaScript.

![[note_3.0-en-us.png]]

When a JavaScript script is customized, the code can be automatically supplemented.

The script format is defined as follows: scriptFormat="JavaScript2.0". For details, see the JavaScript engine of the service.

-   Flow execution context variable: \_context
    
    The context variable obtained from **\_execution** can be directly used by developers to compile code, which reduces the obtaining steps. You can also obtain the context variable from **\_execution** and use it later. The variable name is **\_context**.
    
-   Variable used during flow execution: **\_execution**
    
    var \_execution = {
    // Obtain the ID.
    function getId() : string,
    // Obtain the value of **processInstanceId**.
    function getProcessInstanceId() : string,
    // Obtain the value of the variable based on the variable name.
    function getVariable(name : string) : object,
    // Obtain the value of the variable on the current node based on the variable name.
    function getVariableLocal(name : string) : object,
    // Set the value of the corresponding variable name.
    function setVariable(name : string, value : object),
    // Set the value of the corresponding variable name on the current node.
    function setVariableLocal(name : string, value : object),
    // Check whether variables exist.
    function hasVariables() : boolean,
    // Check whether variables exist on the current node.
    function hasVariablesLocal() : boolean,
    // Check whether the specified variable exists.
    function hasVariable(name : string) : boolean,
    / /Check whether the specified variable exists on the current node.
    function hasVariableLocal(name : string) : boolean,
    // Delete the specified variable.
    function removeVariable(name : string),
    //Delete the specified value from the current node.
    function removeVariableLocal(name : string),
    // Delete multiple specified variables.
    function removeVariables(names : array),
    // Delete multiple specified variables from the current node.
    function removeVariablesLocal(names : array),
    // Delete all variables.
    function removeVariables(),
    // Delete all variables from the current node.
    function removeVariablesLocal()
    };
    
-   Flow execution tool class: BpmUtils
    
    var BpmUtils = {
    // Check whether the previous task is successfully executed.
    function isLastTaskSuccess() : boolean,
    //Check whether all tasks are successfully executed.
    function isAllTaskSuccess(): boolean,
    // Obtain the result of the previous task.
    function getLastTaskResult() : object,
    // Obtain the results of all tasks.
    function getAllTaskResult() : object
    };
    
-   Log printing: The console provided by the JavaScript engine in CommonSDK is used.
    
    console.info("Test info.");
    console.warn("Test warn.");
    console.error("Test error.");
    
-   Service calling: ServiceInvoker provided by the JavaScript engine in CommonSDK is used.
-   Exception and error code: Exceptions and error codes provided by the JavaScript engine in CommonSDK are used.
    
    throw new ScriptError("mock error msg", new ErrorCode("errcode1", \["arg1", "arg2"\]));
    
-   Common context variable: **\_runtime** provided by the JavaScript engine in CommonSDK is used to obtain information, such as the current tenant and user. This variable is read-only.
    
    var ret = {};
    ret.tenantId = \_runtime.tenantId;
    ret.userName = \_runtime.userName;
    ret.language = \_runtime.language;
    return ret;