---
title: "Obtaining the Location Information"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457277245.html"
depth: 7
---
#### U.getLocation(callback, type, detail)

![[notice_3.0-en-us.png]]

-   When calling this API, you need to modify the value of the internationalization resource item whose **Key** is **location\_permission\_detail** to describe the specific usage scenario and purpose (such as providing the attendance service) of the location information. If you do not need such services, you can revoke this permission at any time. Your use of other services will not be affected.
-   App developers should determine a proper API calling frequency based on the personal information protection policies, regulations, and standards, and the business scenarios and functions.

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| callback | String | Callback method name |
| type | String | Type. The value can be network or gps (default value). |
| detail | String | Details. The value of cityName can be transferred. | Callback Parameters

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| code | Return result. The value can be 0 (success), -1 (obtaining the location failed), or -2 (obtaining the city name failed). | 0 |
| latitude | Latitude | xx.884208516537555 |
| longitude | Longitude | xx.87906437298003 |
| cityName | City | XX city |
| errorMessage | Error information | get location error | Example:

U.getLocation(function(result){}, "gps");

U.getLocation(function(result){}, "network");

U.getLocation(function(result){}, "gps", "cityName");
// result: {"code":0,"cityName":"_XX_ city","latitude":"_xx_.884208516537555","longitude":"_xx_.87906437298003"}
// result: {"code":-1,"errorMessage":"get location error"} 
// result: {"code":-2,"errorMessage":"get city name error"}