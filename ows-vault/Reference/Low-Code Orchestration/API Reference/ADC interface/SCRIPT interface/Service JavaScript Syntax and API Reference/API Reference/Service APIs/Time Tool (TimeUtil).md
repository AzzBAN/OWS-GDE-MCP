---
title: "Time Tool (TimeUtil)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_028.html"
depth: 7
---
# Time Tool (TimeUtil)

**Table 1** Time tool description   
| API | Description | Example |
| :-- | :-- | :-- |
| TimeUtil.getUTCString() | Obtains the UTC real-time time without the time zone flag for value transfer and calculation. | 
var now = TimeUtil.getUTCString();
var result = {
    "now":now,
    "utc2Local":TimeUtil.utc2Local(now,"UTC+8")
}
return result;

 |
| TimeUtil.getUTCLong() | Obtains the UTC timestamp. |
| TimeUtil.utc2Local(utcTime\[, zoneId\]) | Converts a UTC time string to a time zone string. | TimeUtil.utc2Local("2021-11-8 17:39:21");
TimeUtil.utc2Local("2021-11-8 17:39:21", "UTC+8");
TimeUtil.local2Utc("2021-11-8 17:39:21", "UTC+8",false);

 |
| TimeUtil.utc2LocalWithDST(utcTime\[ , zoneId\]) | Converts the UTC time of string type to the local time of string type. If the DST time is used, the DST suffix is automatically added. |
| TimeUtil.utcLong2Local(utcLong\[ , zoneId\]) | Converts the UTC time of long type to the local time of string type. |
| TimeUtil.local2Utc(utcTime\[ , zoneId, isDST\]) | Converts the local time of string type to the UTC time of string type. |
| TimeUtil.plusYears(\[currentTime , \]years) | Adds years based on currentTime. | TimeUtil.plusYears(1);
TimeUtil.plusYears("2021-11-9 15:41:28" ,1);

These APIs support digits in the character format, for example:

TimeUtil.plusYears("1");
TimeUtil.plusYears("2021-11-9 15:41:28" ,"1");

You are advised not to forcibly perform character conversion in the script. Negative example:

TimeUtil.plusYears(parseInt("1"));
TimeUtil.plusYears("2021-11-9 15:41:28" ,parseInt("1"));

 |
| TimeUtil.plusMonths(\[currentTime , \]months) | Adds months based on currentTime. |
| TimeUtil.plusWeeks(\[currentTime , \]weeks) | Adds weeks based on currentTime. |
| TimeUtil.plusDays(\[currentTime , \]days) | Adds days based on currentTime. |
| TimeUtil.plusHours(\[currentTime , \]hours) | Adds hours based on currentTime. |
| TimeUtil.plusMinutes(\[currentTime , \]minutes) | Adds minutes based on currentTime. |
| TimeUtil.plusSeconds(\[currentTime , \]seconds) | Adds seconds based on currentTime. |
| TimeUtil.sleep (timeout) | Enables the current thread to sleep for a period of time, which can be used in polling retry scenarios. Parameters: timeout: sleep time, in milliseconds. The value range is \[10,5000\]. Note: The single sleep time must be between 10 ms to 5000 ms. If the sleep time exceeds 5000 ms, an error is reported. In addition, a single script can sleep for a maximum of 2 minutes at a time. If the sleep time exceeds 2 minutes, a response is returned immediately. | for(var i=0;i var resp = ServiceInvoker.post(url, \_message) if(resp.result == true){ break; } TimeUtil.sleep(5000); } |
| TimeUtil.compare(time1, time2) | Compares two time strings. If the former is greater than the latter, 1 is returned. If the former is less than the latter, -1 is returned. If the former is equal to the latter, 0 is returned. Parameters: time1: time string 1. The format is yyyy-MM-dd HH:mm:ss. time2: time string 2. The format is yyyy-MM-dd HH:mm:ss. | let res = TimeUtil.compare("2023-01-02 00:00:00", "2023-01-01 00:00:00") // 1 res = TimeUtil.compare("2023-01-01 00:00:00", "2023-01-02 00:00:00") // -1 res = TimeUtil.compare("2023-01-01 00:00:00", "2023-01-01 00:00:00") // 0 |
| TimeUtil.nextTransition(time, zoneId) | Returns the next DST change point of the corresponding time zone after the specified time point. Parameters: time: UTC time string. The format is yyyy-MM-dd HH:mm:ss. zoneId: time zone ID | let transition = TimeUtil.nextTransition("2023-06-30 00:00:00", "Europe/London") // "2023-10-29 01:00:00" |
| TimeUtil.prevTransition(time, zoneId) | Returns the previous DST change point of the corresponding time zone after the specified time point. Parameters: time: UTC time string. The format is yyyy-MM-dd HH:mm:ss. zoneId: time zone ID | transition = TimeUtil.prevTransition("2023-06-30 00:00:00", "Europe/London") // "2023-03-26 02:00:00 DST" |
| TimeUtil.isInDST(time, zoneId) | Checks whether the time corresponding to the specified time zone is in the DST time. Parameters: time: UTC time string. The format is yyyy-MM-dd HH:mm:ss. zoneId: time zone ID | let isInDst = TimeUtil.isInDst ("2023-06-30 00:00:00", "Europe/London") // true |
| TimeUtil.getUtcOffset(zoneId) | Obtains the time difference between the time in a specified time zone and UTC, in milliseconds. Parameters: zoneId: time zone ID | let offset = TimeUtil.getUtcOffset("UTC") // 0 |
| TimeUtil.iso8601ToUtc(iso8601\_time) | Converts a time in ISO8601 format to a UTC time string. Parameters: iso8601\_time: time string in ISO8601 format | let utc = TimeUtil.iso8601ToUtc("2023-06-30T08:00:00+08:00") // "2023-06-30 00:00:00" |
| TimeUtil. utcToIso8601(utcTime, zoneId) | Converts a UTC time string into a time string in the ISO8601 format of the corresponding time zone. Parameters: utcTime: UTC time string. The format is yyyy-MM-dd HH:mm:ss. zoneId: time zone ID | let iso8601\_time = TimeUtil.utcToIso8601 ("2023-06-30 00:00:00", "Asia/Shanghai") // "2023-06-30T08:00:00.000+08:00" |
| TimeUtil.formatTimestamp() | Converts the input timestamp into a specified string. | TimeUtil.formatTimestamp(timestamp, "yyyy-MM-dd HH:mm:ss") |
| TimeUtil.parseTimestamp() | Converts the input time string in a timestamp. | TimeUtil.parseTimestamp(dateStr, "yyyy-MM-dd HH:mm:ss") | ![[note_3.0-en-us.png]]

In the API parameters, the content in the square brackets **\[\]** is optional.

**Parent topic:** [[Service APIs|Service APIs]]