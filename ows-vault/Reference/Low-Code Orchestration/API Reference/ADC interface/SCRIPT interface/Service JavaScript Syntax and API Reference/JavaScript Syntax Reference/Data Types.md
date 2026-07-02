---
title: "Data Types"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_003.html"
depth: 6
---
#### number

In JavaScript, integers and floating point numbers are not distinguished. But numbers are stored as floating-point values. In this case, pay attention to the following when using JavaScript:

-   Decimals in JavaScript are not accurate.
-   Integers in JavaScript are accurate within the range between -(253\-1) and (253\-1). Integers beyond this range are not accurate. If the integer is greater than (253\-1), convert it into a character string.

There are several special values:

-   **Infinity**: The value cannot be represented in JavaScript. For example, the calculation result of 1/0 is Infinity. The result of -1 / 0 is -Infinity.
-   **NaN**: It is short for Not A Number, indicating that the value is not a number. For example, the calculation result of 0/0 is NaN. The result of 'abc' \* 123 is NaN.