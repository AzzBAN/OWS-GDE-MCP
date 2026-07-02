---
title: "Common Functions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_023.html"
depth: 5
---
#### Context

[Table 1](#EN-US_TOPIC_0000001140217831__en-us_topic_0232094735_table0377191782416) describes the methods and functions of the **Common functions** translator.

**Table 1** Description of methods of the Common functions translator  
| Method Name | Description |
| :-- | :-- |
| result() | Returns the result. |
| xmlToJson() | Converts XML objects of input/output elements into JSON objects. For example, if the XML object is jackboy, the JSON object is {"name":"jack","sex":"boy"}. |
| safeHtml() | Securely filter the input HTML. |
| empty() | Returns an empty value. |
| currentUser() | Returns the current login user. |
| currentTime() | Returns the current time. |
| userGroupAllInfoTranslator() | Converts fields of the user group type, including all user group fields. |
| userGroupDisplayTranslator() | Convert the user group field type to the name display type. |
| UserIdToUserAccount() | Converts the user ID into the user name. |
| utc2Local() | Converts the UTC time into the local time. |
| Local2utc() | Converts the local time into the UTC time. |
| utc2LocalWithDST() | Converts the UTC time to the local time and marks the DST. After the DST starts, the UTC time is converted to the local time to differentiate the DST. After the time conversion, the DST suffix is used for the DST time. |
| utc2Long() | Converts the UTC time into a timestamp of the long integer type. |
| aesDecrypt() | Decrypts the input/output element of the service using the AES algorithm. |
| aesEncrypt() | Encrypts the input/output element of the service using the AES algorithm. |
| copyFile() | Copies files. |
| UserIdToUserAccountWithoutException | Converts the user ID to the user name. If an exception occurs during the conversion, the user name is displayed as unknown. |
| long2utc | Converts a timestamp of a long integer type to the UTC time. |
| long2local | Converts a timestamp of a long integer type to a local time. |
| toPinyin() | For the string type, Chinese characters can be converted to Chinese pinyin. The pinyin translator supports only basic Chinese characters, that is, Chinese characters ranging from 19968 to 40869 (Unicode code 4E00 to 9FA5). Custom separators are supported. |