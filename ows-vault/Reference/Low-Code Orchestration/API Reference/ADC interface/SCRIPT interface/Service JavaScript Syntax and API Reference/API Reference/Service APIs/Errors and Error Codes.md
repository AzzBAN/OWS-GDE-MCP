---
title: "Errors and Error Codes"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_021.html"
depth: 7
---
# Errors and Error Codes

In JavaScript, the ErrorCode and ScriptError classes can be used to construct error codes and errors, respectively. The script error object can be thrown by JavaScript.

**Table 1** Errors and error code APIs   
| API | Description | Example |
| :-- | :-- | :-- |
| new ErrorCode(code \[ , args \]) | Used to create an error code object. Parameters:
-   **code**: error code, which is a string.
-   **arg**: error code parameter of the array type. This parameter is optional.

Returned value: error code object | var errorCode = new ErrorCode("00123456", \["order1", "close"\]);

 |
| new ScriptError(message \[ , errorCode \]) new ScriptError(errorCode) | Used to create a script error object. Parameters:

-   **message**: error information, which is a string.
-   **errorCode**: error code object type. Set this parameter to the object of an error code.

Returned value: Script error object | throw new ScriptError("Process order failed.");
throw new ScriptError("Process order failed.", new ErrorCode("00123456", \["order1", "close"\]));
throw new ScriptError(new ErrorCode("00123456", \["order1", "close"\]));

 |
| ErrorCodeTranslator.translate(errorCode:ErrorCode,lang:String) ErrorCodeTranslator.translate(code:String,args:NativeArray,lang:String) | Used to translate service script error codes. Parameters:

-   **errorCode**: error code type
-   **lang**: international language, such as **en\_US** and **zh\_CN**. It can be left empty and the default value is **en\_US**.

Returned value: error code object Parameters:

-   **code**: error code, which is a string.
-   **args**: variable value in the internationalization template. The value is of the array type. This parameter can be left empty as required.
-   **lang**: international language, such as en\_US and zh\_CN. It can be left empty and the default value is en\_US.

Returned value: error code object | var errorCode = new ErrorCode('errorCode', args, "message!!!!!!", "solution!!!!!!"); JSON.stringify(ErrorCodeTranslator.translate(errorCode, 'en\_US') ErrorCodeTranslator.translate('errorCode', args, 'en\_US') | **Parent topic:** [[Service APIs|Service APIs]]