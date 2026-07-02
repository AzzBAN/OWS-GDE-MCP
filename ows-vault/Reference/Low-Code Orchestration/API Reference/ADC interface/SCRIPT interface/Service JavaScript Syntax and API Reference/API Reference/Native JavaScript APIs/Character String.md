---
title: "Character String"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_009.html"
depth: 7
---
# Character String

**Table 1** String APIs supported by service JavaScript   
| API | Description | Example |
| :-- | :-- | :-- |
| str.length | Used to obtain the length of a string. | The result of "Test Script".length is 11. The result of "".length is 0. |
| str.charAt(pos) | Used to obtain the character in the specified position. | The result for "Test Script".charAt(0) is "T". The result for "Test Script".charAt(2) is "s". |
| str.indexOf(substr \[ , start \]) | Used to search for a substring. | The result for "Test Script".indexOf("e") is 1. The result for "Test Script".indexOf("x") is -1. |
| str.lastIndexOf(substr \[ , start \]) | Used to search for substrings from the back to the front. | The result for "Test Script".lastIndexOf("e") is 1. |
| str.search(substr) | Used to search for a substring. | The result for "Test Script".search("Script") is 5. The result for "Test Script".search("x") is -1. |
| str.slice(start, end) | Used to extract characters from a string. | The result for "Test Script".slice(5) is "Script". The result for "Test Script".slice(5,6) is "S". |
| str.substring(start, end) | Used to extract characters from a string. | The result for "Test Script".substring(0,3) is "Tes". |
| str.substr(start, length) | Used to extract characters from a string. | It is the same as that of substring. substring is recommended. |
| str.replace(search, replacement) | Used to replace character strings. | The result for "Test Script".replace("e","b") is "Tbst Script". NOTE: By default, the replace () method replaces only the first matching place. To replace all matching places, you can use the regular expression together with the global matching flag g. For example, the result for "Test Script".replace(/t/g, "b") is "Tesb Scripb". |
| str.toUpperCase() | Used to convert to uppercase. | The result for "Test Script".toUpperCase() is "TEST SCRIPT". |
| str.toLowerCase() | Used to convert to lowercase. | The result for "Test Script".toLowerCase() is "test script". |
| str.concat(str1 \[ , ... \]) | Used to concatenate strings. | The result for "Test".concat(" ","Script") is "Test Script". |
| str.trim() | Used to remove white space characters from the beginning and end of a string. | The result for "Test ".trim() is "Test". |
| str.split(separator) | Used to separate strings by delimiters. | The result for "Test Script".split(" ") is \["Test","Script"\]. | ![[note_3.0-en-us.png]]

In the API parameters, the content in the square brackets **\[\]** is optional. For example, in _str_.indexOf(_substr_ \[ , _start_ \]), \[ , _start_ \] is optional. If the start position is not specified, the first character is used as the start position by default. If the start position is specified, the **start** parameter and its previous parameter are separated by a comma (,).

**Parent topic:** [[Native JavaScript APIs|Native JavaScript APIs]]