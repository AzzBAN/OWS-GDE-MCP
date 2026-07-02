---
title: "Comparison Among Multi-Version APIs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_026.html"
depth: 6
---
# Comparison Among Multi-Version APIs

For service APIs, the JavaScript script engine has the following versions:

-   For APIs of ADC 1.5 or earlier versions, the engine version displayed on the GUI is **V 1.5**.
-   For APIs of ADC 1.6, the engine version displayed on the GUI is **V 1.6**.
-   For APIs of the latest ADC version, that is, 2.0 or later, the engine version displayed on the GUI is **Latest**.

The scripts created on the latest ADC version must be compiled based on the latest APIs.

Unless otherwise specified, the APIs described in this document refer to the APIs of the latest ADC version. This topic describes the differences between APIs of each version.

In 1.5 and earlier versions, APIs are used only for asset compatibility and scripts cannot be created.

The service APIs that are not described in this section cannot be used in the new script in ADC 1.6 and the special service APIs in ADC cannot be used for scripts in the latest ADC version. Native JavaScript APIs are the same in the two versions.

**Table 1** API differences between multiple versions    
| APIs of ADC 1.5 or Earlier Versions | APIs of ADC 1.6 | APIs of the Latest ADC Version (2.0 and Later) | Description |
| :-- | :-- | :-- | :-- |
| Context |
| message | \_CONTEXT | \_runtime | 
-   The **\_CONTEXT** context variable in 1.6 contains **tenantId**, **userName**, **userId**, and **language**.
-   In 2.0, the corresponding context variable is **\_runtime**, which contains the members with the same name in 1.6 and has the same meanings.

 |
| message (service node) | message (service node) | \_message \_context.message | -   In 1.6, the service node obtains messages through the **message** variable.
-   In 2.0, the corresponding variable is **\_message** or **\_context.message**.

 |
| \- | ParameterService.getName(name) | \_context.getAppParameter(name) | The API formats are different, but the parameters and return values are the same. |
| message.header.commonValues.currentLang | \_CONTEXT.language | \_runtime.language | Used to obtain the language. |
| message.header.commonValues.currentTimeZone | None | \_runtime.timeZone | Used to obtain the time zone. |
| message.header.commonValues.ip | None | \_runtime.clientIp | Used to obtain the source IP address. (This parameter is available only for services called from the frontend.) |
| message.header.commonValues.currentTenant | \_CONTEXT.tenantId | \_runtime.tenantId | Used to obtain the tenant ID. |
| message.header.commonValues.currentUser | \_CONTEXT.userName | \_runtime.userName | Used to obtain the user name. (This parameter is set by the caller in the context. If the call is from other microservices, this parameter may be empty when it is not set.) |
| None | \_CONTEXT.userId | \_runtime.userId | Used to obtain the user ID. |
| message.header.tracker\_id | None | \_runtime.trackerId | Used to obtain the tracker ID. |
| Error and Error Code |
| If an error needs to be displayed, use JsException.printError() to set it. The method is as follows: throw new JsException("aaaaaaaa", \["b", "c"\]); If the verification fails in a validator, a dialog box needs to be displayed. To do so, use the following method: return new ValidateResult("aaaaaaaa", \["b", "c\]); | new ValidateResult(errorCode, errorArgs, pass) | new ErrorCode(code \[ , args \]) new ScriptError(message \[ , errorCode \]) new ScriptError(errorCode) | -   In 1.6, if the validator fails to be verified, ValidateResult needs to be returned.
-   If the verification of the latest version fails, the ScriptError message needs to be thrown.

 |
| Log |
| var LOGGER = JsLogger.getLogger() To print frontend logs, use var log = JsLogger.getServiceDebugLogger() log .error("message") | JsLogger.debug(message) JsLogger.warn(message) JsLogger.info(message) JsLogger.error(message) | console.debug(message, \[ arg, \[ , ... \] \]) console.warn(message, \[ arg, \[ , ... \] \]) console.info(message, \[ arg, \[ , ... \] \]) console.error(message, \[ arg, \[ , ... \] \]) | -   Only character strings can be output by APIs of ADC 1.6.
-   APIs of the latest ADC version can use placeholders to replace formatted content.

 |
| Service call |
| Call the legacy asset service in four-segment mode. The input and output parameters are Message. var request = Message();request.header = message.header;request.body = {};var response = CloudServiceAccessor.process("app.service.xxx.xxxxxx", request); Directly call the CSE service. The input and output parameters are object. var request = {};//Service request object. You can also directly use the message, which is a native JavaScript object. request.text1 = "arg1xxx"; //Example of setting request parameters: var response = ServiceInvoker.post("xxxx", request); | ServiceInvoker.get(uri \[ , uriParams \]) ServiceInvoker.delete(uri \[ , uriParams \]) ServiceInvoker.post(uri \[ , message \]) ServiceInvoker.invoke(uri \[ , message \]); | The content in 1.6 is the same as that in 2.0 and later versions. |
| TQL |
| RunScriptUtil.tqlEscape | TqlUtils.tqlEscape(content) | TQL.escapeString(content) TQL.escapeIdentifier(content) | -   APIs of ADC 1.6 can only be used to escape character strings and cannot be used to escape identifiers.
-   For APIs of the latest ADC version, you need to use the APIs for escaping character strings or identifiers based on the actual application scenarios of the content to be escaped.

 |
| Lock |
| \- | Lock.acquire(lockName, ttl) | Same value |
| \- | Lock.release(lockName) | In 1.6, this API does not exist. |
| Obtaining the UUID using a script |
| JavaScriptUtil.getUUid() | None | Encoder.randomUUID() | In 1.6, this API does not exist. |
| base64 |
| DigestUtils.encodeBase64 DigestUtils.decodeBase64 | None | Encoder.decodeBase64 Encoder.encodeBase64 | In 1.6, this API does not exist. |
| Validator context |
| The context is a ValidateContext object. The properties are as follows:

-   parentJson
-   jsonObject
-   jsonArray
-   string
-   elementName
-   message

 | The context is a native JavaScript object of Rhino. The properties are as follows:

-   parentValue // Value of the parent node
-   value // Field value
-   name // Field name
-   message // flow message body
-   project // Project name
-   module // Module name

 | The context is a native JavaScript object of Rhino. The properties are as follows:

-   parentValue // Value of the parent node
-   value // Field value
-   name // Field name
-   message // flow message body
-   project // Project name
-   module // Module name

 | \- |
| Translator context |
| In 1.0, the context is a ValidateContext object. The properties are as follows:

-   parentJson
-   jsonObject
-   jsonArray
-   string
-   message

 | -   parentValue // Value of the parent node
-   parentArray // Array of the parent node
-   value // Field value
-   name // Field name
-   message // flow message body
-   project // Project name
-   module // Module name
-   tenantId // Tenant ID
-   userName // User name

 | -   parentValue // Value of the parent node
-   parentArray // Array of the parent node
-   value // Field value
-   name // Field name
-   message // flow message body
-   project // Project name
-   module // Module name
-   tenantId // Tenant ID
-   userName // User name

 | \- |
| Time tool |
| JavaScriptTimeUtil.compare(String, String) | Same as the API of the latest version | TimeUtil.compare(String, String) | \- |
| JavaScriptTimeUtil.convertCalendar(long, String) | Same as the API of the latest version | N/A | This method involves the Java class Calendar. Therefore, this method is no longer supported. |
| JavaScriptTimeUtil.convertCalendar(String, String) | Same as the API of the latest version | N/A | This method involves the Java class Calendar. Therefore, this method is no longer supported. |
| JavaScriptTimeUtil.convertString(Calendar) | Same as the API of the latest version | N/A | This method involves the Java class Calendar. Therefore, this method is no longer supported. |
| JavaScriptTimeUtil.getGapTime(String) | Same as the API of the latest version | TimeUtil.getUtcOffset(String) | \- |
| JavaScriptTimeUtil.getShiftTime(String, String) | Same as the API of the latest version | N/A | This function can be implemented based on TimeUtil.getUTCLong(String). |
| JavaScriptTimeUtil.getShiftTimeLong(long, long) | Same as the API of the latest version | N/A | This method can be implemented by date format conversion. |
| JavaScriptTimeUtil.getShiftTimeString(String, String) | Same as the API of the latest version | N/A | This method can be implemented by date format conversion. |
| JavaScriptTimeUtil.getTimeString(long) | Same as the API of the latest version | N/A | This method can be implemented using Date of the native JavaScript. |
| JavaScriptTimeUtil.getTimeZone(String) | Same as the API of the latest version | N/A | This method involves the Java class TimeZone. Therefore, this method is no longer supported. |
| JavaScriptTimeUtil.isInDST(String, String) | Same as the API of the latest version | TimeUtil.isInDST(String, String) | \- |
| JavaScriptTimeUtil.ISO8601ToUTC(String) | Same as the API of the latest version | TimeUtil.iso8601ToUtc(String) | \- |
| JavaScriptTimeUtil.local2Utc(String, String) | Same as the API of the latest version | TimeUtil.local2Utc(String, String) | \- |
| JavaScriptTimeUtil.longTime2String(long) | Same as the API of the latest version | N/A | This method can be implemented using Date of the native JavaScript. |
| JavaScriptTimeUtil.nearTransitions(Calendar) | Same as the API of the latest version | N/A | This method involves the Java class Calendar. Therefore, this method is no longer supported. |
| JavaScriptTimeUtil.nearTransitions(String, String) | Same as the API of the latest version | N/A | This method can be implemented using TimeUtil.nextTransition and TimeUtil.prevTransition. |
| JavaScriptTimeUtil.nextTransition(Calendar) | Same as the API of the latest version | N/A | This method involves the Java class Calendar. Therefore, this method is no longer supported. |
| JavaScriptTimeUtil.nextTransition(String, String) | Same as the API of the latest version | TimeUtil.nextTransition(String, String) | \- |
| JavaScriptTimeUtil.plusDays(int) | Same as the API of the latest version | TimeUtil.plusDays(int) | \- |
| JavaScriptTimeUtil.plusDays(String, int) | Same as the API of the latest version | TimeUtil.plusDays(String, int) | \- |
| JavaScriptTimeUtil.plusHours(int) | Same as the API of the latest version | TimeUtil.plusHours(int) | \- |
| JavaScriptTimeUtil.plusHours(String, int) | Same as the API of the latest version | TimeUtil.plusHours(String, int) | \- |
| JavaScriptTimeUtil.plusMinutes(int) | Same as the API of the latest version | TimeUtil.plusMinutes(int) | \- |
| JavaScriptTimeUtil.plusMinutes(String, int) | Same as the API of the latest version | TimeUtil.plusMinutes(String, int) | \- |
| JavaScriptTimeUtil.plusMonths(int) | Same as the API of the latest version | TimeUtil.plusMonths(int) | \- |
| JavaScriptTimeUtil.plusMonths(String, int) | Same as the API of the latest version | TimeUtil.plusMonths(String, int) | \- |
| JavaScriptTimeUtil.plusSeconds(int) | Same as the API of the latest version | TimeUtil.plusSeconds(int) | \- |
| JavaScriptTimeUtil.plusSeconds(String, int) | Same as the API of the latest version | TimeUtil.plusSeconds(String, int) | \- |
| JavaScriptTimeUtil.plusWeeks(int) | Same as the API of the latest version | TimeUtil.plusWeeks(int) | \- |
| JavaScriptTimeUtil.plusWeeks(String, int) | Same as the API of the latest version | TimeUtil.plusWeeks(String, int) | \- |
| JavaScriptTimeUtil.plusYears(int) | Same as the API of the latest version | TimeUtil.plusYears(int) | \- |
| JavaScriptTimeUtil.plusYears(String, int) | Same as the API of the latest version | TimeUtil.plusYears(String, int) | \- |
| JavaScriptTimeUtil.prevTransition(Calendar) | Same as the API of the latest version | N/A | This method involves the Java class Calendar. Therefore, this method is no longer supported. |
| JavaScriptTimeUtil.prevTransition(String, String) | Same as the API of the latest version | TimeUtil.prevTransition(String, String) | \- |
| JavaScriptTimeUtil.UTC2ISO8601(String, String) | Same as the API of the latest version | TimeUtil.utcToIso8601(String, String) | \- |
| JavaScriptTimeUtil.utc2local(String, String) | Same as the API of the latest version | TimeUtil.utc2local(String, String) | \- |
| JavaScriptTimeUtil.utc2localWithDST(String, String) | Same as the API of the latest version | TimeUtil.utc2localWithDST(String, String) | \- |
| JavaScriptTimeUtil.utc2TenantLocal(String, String) | Same as the API of the latest version | N/A | The native JavaScript can be used to convert the date format, for example, let originalDateString = "20/03/2022 22:45:30" //Your Date string(dd/MM/yyyy HH:mm:ss) let parts = originalDateString.split("/") let dateParts = parts\[2\].split(" ") let newDateString = \`${dateParts\[0\]}-${parts\[1\]}-${parts\[0\]} ${dateParts\[1\]}\` console.log(newDateString) // 2022-03-20 22:45:30 |
| JavaScriptTimeUtil.utc2TenantLocalWithDST(String, String) | Same as the API of the latest version | N/A | You can convert the date and time character string of the tenant to a standard date and time character string, and then use TimeUtil.utc2LocalWithDst to implement the method. |
| JavaScriptTimeUtil.utcLong2Local(long, String) | Same as the API of the latest version | TimeUtil.utcLong2Local(long, String) | \- |
| JavaScriptTimeUtil.validateFormat(String, String, boolean) | Same as the API of the latest version | N/A | This method can be implemented using regular expressions of JavaScript. | **Table 2** Capabilities not provided in the new version   
| Scenario | 1.5 or Earlier Versions | 1.6 and 2.0 and Later Versions |
| :-- | :-- | :-- |
| Validator | Directly call the validation method: JsValidator.dataExistCheck(t\_data, value, res, "") | Not provided |
| Use the Validate object:
 validateResult = Validator.validate(alarms, {
            name: "Alarm Filter.alarm\_field",
            required: true,
            dataExist: {
               "modelName": "validate1\_field", 
               "field": "field\_name", 
               "condition": "" 
            }
});

 | Not provided | **Parent topic:** [[API Reference|API Reference]]