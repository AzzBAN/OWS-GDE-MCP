---
title: "Math"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_012.html"
depth: 7
---
# Math

**Table 1** Math APIs supported by service JavaScript   
| API | Description | Example |
| :-- | :-- | :-- |
| Math.round(num) | Round up num. | Math.round (10.5) returns 11. Math.round(-10.5) returns - 10. |
| Math.ceil(num) | Round up num. | Math.ceil(10.1) returns 11. Math.ceil(-10.1) returns - 10. |
| Math.floor(num) | Round down num. | Math.floor(50.99) returns 50. |
| Math.trunc(num) | Obtains the integer part of num. | Math.trunc(10.1) returns 10. Math.trunc(-10.1) returns -10. |
| Math.sign(num) | Check whether num is a negative number (return -1), 0 (return 0), and positive number (return 1). | Math.sign(10) returns 1. Math.sign(-10) returns -1. |
| Math.abs(num) | Calculates the absolute value of num. | Math.abs(-10) returns 10. Math.abs(10) Range 10. |
| Math.pow(base, exp) | Finds the exp power of base. | Math.pow(2, 4) returns 16. |
| Math.sqrt(num) | Find the square root of num. | Math.sqrt(4) returns 2. |
| Math.min(num, \[ , ... \]) | Calculates the minimum value. | Math.min(2, 3, 4) returns 2. |
| Math.max(num, \[ , ... \]) | Calculates the maximum value. | Math.max(2, 3, 4) Range 4. |
| Math.random() | The value is a random number ranging from 0 (inclusive) to 1 (exclusive). Do not use the return value of this API as a secure random number. | A floating-point number in the range 0 (included) to 1 (excluded). | **Parent topic:** [[Native JavaScript APIs|Native JavaScript APIs]]