---
title: "Examples"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_027.html"
depth: 5
---
# Examples

Run Script template

1\. Obtain input parameters and output parameters.

//Obtain the parameters configured in **Parameters** of the Run Script node.
var alarmName = \_message.alarmName;
var alarmId = \_message.alarmId;
//Process the intermediate logic.
var solution = "The solution of alarmName:\[" + alarmName + "\],alarmId:\[" + alarmId+ "\] is: Restart the system.";
var result = {};
result.alarmId = alarmId;
result.solution = solution;
//Use the returned result of the object type as the output parameter of the node.
return result

2\. Use context variables and read common parameters.

//Obtain the parameters configured in **Parameters** of the Run Script node.
var alarmName = \_message.alarmName;
var alarmId = \_message.alarmId;
//Process the intermediate logic.
var solution = "The solution of alarmName:\[" + alarmName + "\],alarmId:\[" + alarmId+ "\] is: Restart the system.";
var alarm = {};
alarm.alarmId = alarmId;
alarm.solution = solution;

//Obtain the system environment information. To get other information, use the API of \_runtime.
alarm.username = \_runtime.userName
alarm.timeZone= \_runtime.timeZone

//Obtain the script context information. To get other information, use the API of \_context.
//Obtain app parameters.
alarm.nodeIp = \_context.getAppParameter("nodeIp")
//Use the returned result of the object type as the output parameter of the node.
return alarm

3\. Call the service to maintain the model instance data.

/\*\*
\* URL format:
\* For ADC APIs, the format is **/Service name/**_xxx_**/**_xxx_**/**_xxx_.
\* For APIs of other microservices, the format is **/**_App name:Service name_**/**_xxx_**/**_xxx_**/**_xxx_. The app name and service name depend on the target microservice.
 \*\*/
//Obtain the parameters configured in **Parameters** of the Run Script node.
var alarmName = \_message.alarmName;
var alarmId = \_message.alarmId;
var request = {
"alarmId" : alarmId,
"alarmName" : alarmName
};
//Send a POST request.
var createresult = ServiceInvoker.post("/adc-service/rest/v1/services/sample/template/create\_alarm", request);

//Obtain the public REST get method interfaces exposed by the microservice developed by GDE or the business side.
var geturi = "/_Application name: Microservice name_/xxx/xxx/xxx?alarmName = {} && alarmId = {}"
var getresult = ServiceInvoker.get(geturi, request);

//Obtain the public REST delete method interfaces exposed by the microservice developed by GDE or the business side.
var deleteuri = "/appid:adc-service/rest/v1/xxx?alarmName = {} && alarmId = {}"
var deleteresult = ServiceInvoker.delete(deleteuri, request);

var result = {
"result" : true
};
//Use the returned result of the object type as the output parameter of the node.
return result

4\. Rectify faults and print debug logs.

//Obtain the parameters configured in **Parameters** of the Run Script node.
var alarmName = \_message.alarmName;
var alarmLocatoion = \_message.alarmLocation;
//If all parameters are empty, error logs are printed and an exception occurs.
if (!alarmname && !alarmLocatoion) {
    console.error("Both alarmname and alarmLocatoion are empty.")
    throw new ScriptError('Both alarmname and alarmid are empty.')
}
//If the alarm name is empty, an exception occurs. Otherwise, common logs are printed.
if (alarmName) {
    console.info("alarmName is:" + alarmName)
} else {
    console.error("alarmName is empty.")
    throw new ScriptError('AlarmName is empty.')
}
try {
    var location = JSON.parse(alarmLocatoion)
    return location.city
} catch (e) {
    console.error('Parse location error')
    throw new ScriptError('Parse location error.', \[alarmName\])
}
return 'unknown city';

Validator template

1\. Verify common field.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var value = \_context.value
//If the verification fails, an exception occurs.
if (value != '100'){
    throw new ScriptError("Validate failed."))
}
//The verification is successful and no data needs to be returned.

2\. Verify the permission of an array field.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var arrayValue = \_context.value
//If the verification fails, an exception occurs and the specified error code is used.
if (arrayValue.length < 1){
    throw new ScriptError("Validate failed. Child alarm is empty", new ErrorCode('100000x',\[name\]))
}
//The verification is successful and no data needs to be returned.

3\. Verify the permission of an object field.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var objectValue = \_context.value
//If the verification fails, an exception occurs and the specified error code is used.
if (!objectValue.location){
    throw new ScriptError("Validate failed. Location is empty", new ErrorCode('100000x',\[name\]))
}
//If the verification fails, an exception occurs and the specified error code is used.
if (!objecVvalue.parentAlarm){
    throw new ScriptError("Validate failed.Parent alarm is empty", new ErrorCode('100000x',\[name\]))
}
//The verification is successful and no data needs to be returned.

4\. Call services to perform the complex verification.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var alarm = \_context.value
//If the verification fails, an exception occurs and the specified error code is used.
if (!alarm.location){
    throw new ScriptError("Validate failed. Location is empty", new ErrorCode('100000x',\[name\]))
}
//If the verification fails, an exception occurs and the specified error code is used.
if (!alarm.parentAlarm){
    throw new ScriptError("Validate failed.Parent alarm is empty", new ErrorCode('100000x',\[name\]))
}
var request = {}
request.sourceLocation = ojectValue.location
request.targetCity = 'Bei Jing'
//Call services to verify the validity.
var result = ServiceInvoker.post("/adc-service/rest/v1/services/sample/template/check\_location\_in\_city", request);
//If the verification fails, an exception occurs and the specified error code is used.
if (!result){
    throw new ScriptError("Validate failed. Location" + ojectValue.location + " is not in Bei Jing")
}
//The verification is successful and no data needs to be returned.

5\. Use context variables and read app parameters.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var alarmIp = \_context.value;
//Process the intermediate logic.
//Obtain the system environment information. To get other information, use the API of \_runtime.
var username = \_runtime.userName
console.info("operator is:" + alarmName)
//Obtain the script context information. To get other information, use the API of \_context.
//Obtain the app parameters _\[ip1, ip2, ...\]_.
var nodeIps = \_context.getAppParameter("nodeIps")
//If the verification fails, an exception occurs and the specified error code is used.
if (!alarmIp || nodeIps.indexOf(alarmIp)<0 ){
    throw new ScriptError("Alarm Node IP is not correct.", new ErrorCode('100000x',\[name,alarmIp\]))
}
//The verification is successful and no data needs to be returned.

6\. Rectify faults and print debug logs.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var alarmLocatoion = \_context.value;
//If the alarm address is empty, the verification fails. Otherwise, common logs are printed.
if (alarmLocatoion) {
    console.info("alarmLocation is:" + alarmLocation)
} else {
    console.error("alarmLocation is empty")
    throw new ScriptError('AlarmLocation is empty.')
}
try {
    //Check whether the location character string is in the valid JSON format.
    var location = JSON.parse(alarmLocatoion)
} catch (e) {
    console.error('Parse location error')
    throw new ScriptError('Parse location error.',  new ErrorCode('100000x',\[alarmLocatoion\]))
}
//The verification is successful and no data needs to be returned.

Translator template

1\. Convert common fields.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var value = \_context.value
//View the conversion result.
return "translate field:"+name+". alarmid:"+value

2\. Convert an array field.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var alarms = \_context.value
for (var alarm in alarms){
    if (!alarm.resolvedDate){
         alarm.resolvedDate = new Date().getTime()
    }
}
//View the conversion result.
return alarms

3\. Convert an object field.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name = \_context.name
var alarm = \_context.value
if (!alarm.resolvedDate){
       alarm.resolvedDate = new Date().getTime()
    }
}
//View the conversion result.
return alarm

4\. Use context variables and read app parameters.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name= \_context.name;
var solution = \_context.value;
//Process the intermediate logic.
//Obtain the system environment information. To get other information, use the API of \_runtime.
userName = \_runtime.userName

//Obtain the script context information. To get other information, use the API of \_context.
//Obtain app parameters.
nodeName = \_context.getAppParameter("nodeName")

var resolved = nodeName + " resolved by "userName + ".solution is " + solution;
//View the conversion result.
return resolved

5\. Call services to perform complex conversion.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var name= \_context.name;
var alarm = \_context.parentValue;
var location = \_context.value;
if (location){
    var request = {};
    request.location = location;
    //Convert to the longitude and latitude.
    location = ServiceInvoker.post("/adc-service/rest/v1/services/sample/template/transform\_geo\_location", request);
} else {
    location = "\[0,0\]";
}
return location;

6\. Rectify faults and print debug logs.

//Obtain the parameter name and value of the field where the validator is located.
//var objectValue = \_context.parentValue The parent node of the current message node is obtained and the value is an object.
//var arrayValue = \_context.parentArray The array where the parent node of the current message node is located is obtained and the value is an array.
var alarmLocatoion = \_context.value;
//If the alarm address is empty, the verification fails. Otherwise, common logs are printed.
if (alarmLocatoion) {
    console.info("alarmLocation is:" + alarmLocation)
} else {
    console.error("alarmLocation is empty")
    throw new ScriptError('AlarmLocation is empty.')
}
try {
    var location = JSON.parse(alarmLocatoion)
    return location.city
} catch (e) {
    console.error('Parse location error')
    throw new ScriptError('Parse location error.', new ErrorCode('100000x',\[alarmLocatoion\]))
}

**Parent topic:** [[Service JavaScript Syntax and API Reference|Service JavaScript Syntax and API Reference]]