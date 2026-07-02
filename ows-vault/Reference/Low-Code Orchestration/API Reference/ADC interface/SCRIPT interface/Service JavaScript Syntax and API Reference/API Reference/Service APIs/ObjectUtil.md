---
title: "ObjectUtil"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_035.html"
depth: 7
---
# ObjectUtil

This API belongs to the object operation tool class.

**Table 1** ObjectUtil API   
| API | Description | Example |
| :-- | :-- | :-- |
| ObjectUtil.isNullOrEmpty(obj) | Determines whether an object is null or empty. Parameters: obj: object to be determined Returned value: The value is of the Boolean type. The value true indicates that the object is empty. Otherwise, the object is not empty. Note: true is returned for this API only when the input parameter is null, undefined, "null" (null character string), or "undefined" (undefined character string). | let foo = ObjectUtil.isNullOrEmpty(null) // true foo = ObjectUtil.isNullOrEmpty("null") // true foo = ObjectUtil.isNullOrEmpty(undefined) // true foo = ObjectUtil.isNullOrEmpty("undefined") // true foo = ObjectUtil.isNullOrEmpty("") // false; let obj = {}; foo = ObjectUtil.isNullOrEmpty(obj) // false |
| ObjectUtil.read(obj, prop1\[,prop2,prop3...\]) | Reads the property value of a specified path from an object to simulate the optional link syntax in the native JavaScript. This method does not report a null pointer. If the corresponding property link does not exist, undefined is returned. Parameters:
-   **obj**: object whose properties need to be read
-   **prop1, prop2**: property in the property link

Returned value: property value in the input parameter object. If the corresponding property chain does not exist in the object, undefined is returned. | let obj = {"a": 1, "b": {"bb": 2}} let foo = ObjectUtil.read(obj, "a") // 1 foo = ObjectUtil.read(obj, "b") // {"bb": 2} foo = ObjectUtil.read(obj, "b", "bb") // 2 foo = ObjectUtil.read(obj, "b", "cc") // undefined foo = ObjectUtil.read(obj, "b", "cc", "dd") // undefined | **Parent topic:** [[Service APIs|Service APIs]]