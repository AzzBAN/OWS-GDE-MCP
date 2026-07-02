---
title: "U"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001733451108.html"
depth: 5
---
# U

**U.platform**

Used to specify the client platform information. The value is **Android** or **iOS**.

Input parameters:

Example:

// Determine whether the client uses iOS.
if(U.platform == "iOS"){
console.log("user is using iOS!");
}else{
console.log("user is using Android!");
}

**U.setParam(key, value)**

Used to store key value pairs, but this API does not persist the data. After **webview** is cleared, data will be lost.

Input parameters:

**key** (string): key

**value** (string): value

Example:

U.setParam("taskId","CM-001")

**U.readLocalData(key)**

Used to read data stored locally or read data stored by the setParam method.

Input parameters:

**key** (string): key

 
| Key | Meaning |
| :-- | :-- |
| username | User name |
| fullname | Full user name |
| tenant\_id | Tenant ID |
| appBaseDir | Root directory for storing apps |
| location | Location information. The format is "lat=XXX,lng=XXX". If there is no location information, the value is No Location. |
| screenResolution | Screen resolution (format: 1600 x 1200) |
| sdk | SDK version of the mobile |
| statusBarHeight | Height of the status bar |
| utc | UTC time of the server. The format is "1481253462321". |
| now | Current time of the server. The format is "2016-12-09 03:17:42". |
| localtime | Local time zone obtained after the conversion of the server time (format: 2016-12-09 11:17:42) |
| locale | Language and country (format: en\_US) |
| timezone | Time zone (format: GMT+08:00) |
| inprocess\_task | Ticket that is being processed (The ticket ID is returned.) |
| UUID | UUID | Example:

U.setParam("taskId","CM-001");
// Read the data stored by the setParam method.
var taskId = U.readLocalData("taskId");
// Read the data provided by the system.
var username = U.readLocalData("username");

**U.fullScreen(on)**

Used to specify whether to use the full screen mode (the tab page in the lower part is hidden in full screen mode).

Input parameters:

**on** (boolean): whether to use the full screen mode

Example:

// Use the full screen mode.
U.fullScreen(true);

**U.goBack(tab)**

Used to return to a native page.

Input parameters:

**tab** (string): returned tab

Example:

// Return to the **from\_home\_page\_to\_android** page.
U.goBack({
page: "from\_home\_page\_to\_android"
});

**U.dispatchMsg(msg,param,callback)**

Universal API for native interaction

Input parameters:

**msg** (string): message type

 
| Value | Meaning |
| :-- | :-- |
| hideFrame | Hides the tab pages at the bottom. The effect is the same as that of using the full screen mode. |
| revealFrame | Shows the tab pages at the bottom. The effect is the same as that of removing the full screen mode. |
| pageForward | Indicates the system page to be redirected to. The page parameter is mandatory. The following parameters are optional:
-   **chat**
-   **message**: message tab
-   **camera**
-   **contacts**
-   **upload\_monitor**: Monitoring results need to be uploaded.
-   **map**

 |
| deleteAppMsg | Deletes task messages. |
| handle\_task | Sets the task as the current task. | **param** (object): message parameter

**callback** (function): callback method. Apply only to iOS. iOS needs to use the callback method to transfer the callback logic after it obtains data.

Example:

// Return to the tab page.
U.dispatchMsg("pageForward", tab);

**U.isOnline()**

Used to specify whether the mobile phone is online (that is, connected to the OWS server).

Input parameters

Example:

// Check whether the mobile phone is online.
var isOnline = U.isOnline();

**U.isGpsOpen(callback)**

Used to specify whether GPS is enabled.

Input parameters

**callback** (function): callback method. Apply only to iOS. iOS needs to use the callback method to transfer the callback logic after it obtains data.

Example:

// Check whether GPS is enabled on the mobile phone.
//android
var isGPSOpen = U.isGpsOpen();
//iOS
U.isGpsOpen(function(value){
console.log("GPS open status = "+ value);
});

**U.getSysParam(key)**

Used to obtain system parameters.

Input parameters:

**key** (string): **currentTime**: current UTC time; **username**: login user name; **url**: loading URL, that is, the part following **main.html#**

Example:
// Obtain the current system time.
this.rightValue = U.getSysParam("now");
// Obtain the current system time.
init\_time = U.getSysParam("localtime");
// Obtain the user.
U.getSysParam("username");
// Obtain the current system language.
var i18Locale = U.getSysParam("locale");

**U.openUrl(url)**

Used to open a URI specified by the system or a URL. Only iOS URLs or URIs starting with **tel:**, **http:**, or **https:** are supported.

Input parameters:

**url** (string): URL or URI to be opened

Example:

//iOS
// Make a call.
U.openUrl("tel:88678992743");
// Open a web page.
U.openUrl("http://www.baidu.com");

**U.getLocation(callback, waittime, type)**

Used to obtain the location information asynchronously. If the location information cannot be obtained, wait until the specified maximum waiting duration is reached.

Input parameters:

**callback** (function): callback method after the location information is obtained

**waittime** (integer): maximum waiting duration, in seconds

**type** (string): obtained location information. The value can be **GPS** or **Others**. If the value is not **GPS**, the network location is preferentially used.

Example:

Nf.PageReady(function() {
// Define the callback function.
var callbackFunction = function(location){C("A").setValue(location);};
var callbackFunction2 = function(location){C("B").setValue(location);};
// Set the click event of the control whose ID is **location** to obtain the location information.
C("location").on("click",function(){
U.getLocation(GlobalCallBackFunc.register(callbackFunction),90,"nogps");
});
C("locationGPS").on("click",function(){
//Set the obtaining mode to GPS preferred.
U.getLocation(GlobalCallBackFunc.register(callbackFunction2),90,"GPS");
});
});

**U.getSelectedPhotos(taskId, group, item)**

Used to obtain selected photos.

Input parameters:

**taskId** (string): ticket ID

**group** (string): request data

**item** (string): item to be obtained

Example:

// Obtain selected photos.
self.bavar signaturePath = U.getSelectedPhotos(taskId, group, item);

**U.uploadTaskPhotos(taskId, moduleName, itemsToSubmit,uploadType)**

Used to upload files and return the batch ID.

Input parameters:

**taskId** (string): ticket ID

**moduleName** (string): request data

**itemsToSubmit** (string): item to be submitted

**uploadType** (string): type of the file to be uploaded

Example:

Scenario 1: Uploading photos

Scenario 2: Uploading signatures

Scenario 3: Uploading photos and signatures

For details about the three scenarios, see the following example:

// Submit the photo and signature.
function submitPhotos() {
var task\_id = CurrentPage().parameters\['orderid'\];
var results\_photo = \[\];var results\_signature = \[\];
// Obtain all components on the current page.
var widget\_maps = CurrentPage().getPageWidgets();
$.each(widget\_maps, function (key, value) {
if (value.getType() == "Nf.mspl.form.dataField.Photograph") {
results\_signature.push(value.getGroupAndItem());
}
});
U.uploadTaskPhotos(task\_id, "photos-of-signature", JSON.stringify(results\_signature));
}

Precautions:

This API is also used for the scenario where the signature control on a page needs to be uploaded, because the getType interface of the signature control returns **Nf.mspl.form.dataField.Photograph**.

if(value.getType() == "Nf.mspl.form.dataField.Photograph"){
results\_signature.push(value.getGroupAndItem());
}

**U.loadOperationLog(taskId)**

Used to load operation logs.

Input parameters:

**taskId** (string): ticket ID

Example:

// Load operation logs.

U.loadOperationLog(taskId);

**U.isFileExist(path)**

Used to determine whether a file exists.

Input parameters:

**path** (string): file path

Example:

// Determine whether a file exists.

U.isFileExist(path);

**U.getTaskDirPath(taskId)**

Used to obtain the folder path of the task based on the ticket ID.

Input parameters:

**taskId**: ticket ID

Example:

// Obtain the folder path.

U.getTaskDirPath(taskId);

**U.sendSMS(to,content)**

Used to send an SMS message.

Input parameters:

**to**: address to which the SMS message is sent

**content**: SMS message content

Example:

**U.getSDCacheDir()**

Used to obtain the root directory of the SD card.

Input parameters

Example:

**U.timeTransByZone (time, utcToLocal)**

Used to convert time based on the time zone.

Input parameters:

**time**: time to be converted

**utcToLocal**: The value **true** indicates that the local time is converted. The value **false** indicates that the UTC time is converted.

Example:

**U.getPhotoDetail (taskId, group, item)**

Used to obtain photo details.

The format of the returned data is as follows:

\["file:///storage/task-photo-thumb-1424853641516.png","file:///storage/task-photo-thumb-1424854626657.png"\]

Input parameters:

**taskId**: ticket ID

**group**: configured in **Parameters** under **Photograph**. It is used to distinguish content in different controls.

**item**: value of **name** under **Photograph**. It is used to distinguish content in different controls.

Note: Generally, the content of different controls is distinguished by the values of **group** and **item**. Set **group** and **item** to different values for different controls.

Example:

// Obtain photo details.
U.getPhotoDetail(taskId, "group", "item");

**U.getFormPhotoDetail (taskId, itemsToSubmit)**

Used to obtain photo details. The returned value is of the JSON format.

Input parameters:

**taskId**: ticket ID

**itemsToSubmit**: all uploaded photos in the form

Example:

C("submit").on("click", function(){
var validate\_result = C("form").validate();
if(!validate\_result){
console.log("validate\_result fail.");
return;
}
console.log("photo\_graph submit");
var results = \[\];
// Obtain all photos in the form.
var widget\_maps = CurrentPage().getPageWidgets();
$.each(widget\_maps, function (key, value) {
console.log("type=" + value.getType());
if (value.getType() == "Nf.mspl.form.dataField.Photograph") {
results.push(value.getGroupAndItem());
}
});
// Obtain details.
var details = U.getFormPhotoDetail(task\_id, JSON.stringify(results));
console.log("page photoDetail info = " + details);
})

**U.getPhotoUploadStatus (options)**

Used to obtain the photo upload status, including the following options:

**nophoto**, **uploading**, **uploadfailed**, **uploadwaiting**, and **uploaded**

Input parameters:

**options**: list of required parameters, including **taskId**, **group**, **item**, and **success**. **success** indicates the callback method after the query is successful.

Example:

function photo\_upload() {
console.log("=======photo\_upload is beSubmit:");
U.getPhotoUploadStatus({
taskId:"liuyantask",
group:"liuyangroup",
item:"liuyanitem",
success:function(result){
console.log("===getPhotoUploadStatus result:"+result.result);
}
});
}
Nf.PageReady(function() {
C("photo\_upload").on("click",photo\_upload);
});

**U.doRedirectAction (options)**

Used to perform redirection based on the information in **options**.

Input parameters:

**options**: list of required parameters. The value is **url**, **location**, **parameters**, or **recordHistory**.

Example:

U.doRedirectAction({url:"test.mspl",parameters:{name:"name"},recordHistory:false})

**Parent topic:** [[JavaScript APIs|JavaScript APIs]]