---
title: "Array"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_011.html"
depth: 7
---
# Array

**Table 1** Array APIs supported by service JavaScript   
| API | Description | Example |
| :-- | :-- | :-- |
| arr.toString() | Used to convert an array to a character string. Multiple values are separated by commas (,). | The value of \[1,2,3\].toString() is "1,2,3". |
| arr.indexOf(element \[ , start \]) | Used to search for an element. | The value of \["Java","Script"\].indexOf("Script") is 1. If no record is found, the value is -1. |
| arr.lastIndexOf(element \[ , start \]) | Used to query the last index in a range array. If no result is found, the value is -1. | The value of \["Java","Java"\].lastIndexOf("Java") is 1. |
| arr.pop() | Used to remove the last element. | \["Java","Script"\].pop() returns "Script" and the original array is updated to \["Java"\]. |
| arr.push(element) | Used to append an element to the end of an array and return the new length of the array. | The result for \["Java","Script"\].push("J") is 3. After the execution, the original array is updated to \["Java,""Script,""J"\]. |
| arr.shift() | Used to remove the first element and obtain the value of this element. | The result for \["Java","Script"\].shift() is "Java" and the original array is updated to \["Script"\]. |
| arr.unshift(element) | Used to insert an element before an array. | \["J","Script"\].unshift("S"). The original array is updated to \["S","J","Script"\]. |
| arr\[pos\] | Used to obtain and modify the array element at a specified position. | \["Java","Script"\]\[0\], \["Java","Script"\]\[1\]="S" |
| arr.concat(arr\_or\_element \[ , ... \]) | Used to merge arrays. | \["Java"\].concat\["Script"\]. After the execution, the original array is updated to \["Java,""Script"\]. |
| arr.slice(start \[ , end \]) | The captured array contains begin but does not contain end. The original array remains unchanged. | \["Java","Script"\].slice(1) returns \["Script"\] |
| arr.sort(\[ compare\_function \]) | Used to sort array elements. Default order in which elements are converted to character strings | The result for \[1,2,4,3,100\].sort() is \[1,100,2,3,4\]. |
| arr.reverse() | Used to reverse array elements and change the original array. | \[1,2,4,3,100\].reverse(). The original array is changed to \[100,3,4,2,1\]. | ![[note_3.0-en-us.png]]

In the API parameters, the content in the square brackets **\[\]** is optional. For example, in _arr_.indexOf(_element_ \[ , _start_ \]), \[ , _start_ \] is optional. If the start position is not specified, the first character is used as the start position by default. If the start position is specified, the **start** parameter and its previous parameter are separated by a comma (,).

**Parent topic:** [[Native JavaScript APIs|Native JavaScript APIs]]