---
title: "JSON"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_013.html"
depth: 7
---
# JSON

**Table 1** JSON APIs supported by service JavaScript   
| API | Description | Example |
| :-- | :-- | :-- |
| JSON.parse(str) | Used to convert a JSON character string to an object. | 
var str = '{"name": "Tom", "age": 30}';
var obj = JSON.parse(str);

 |
| JSON.stringify(obj) | Used to convert an object to a character string. Not all objects can be converted to JSON strings. | var obj = {
    name: "Tom",
    age: 30
};
var str = JSON.stringify(obj);

 | **Parent topic:** [[Native JavaScript APIs|Native JavaScript APIs]]