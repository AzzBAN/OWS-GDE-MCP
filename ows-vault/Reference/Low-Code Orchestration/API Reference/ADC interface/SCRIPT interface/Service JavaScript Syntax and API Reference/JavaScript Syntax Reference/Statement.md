---
title: "Statement"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_006.html"
depth: 6
---
# Statement

To improve the code readability, compile the JavaScript script based on the following requirements:

-   Do not write multiple statements in one line.
-   Use a semicolon (;) at the end of each statement.
-   Even if there is only one line of code in the code block of control statements and loop statements, braces must be used.
-   Use spaces to indent statements appropriately and keep the indentation style consistent across the entire script.

**Table 1** Statements supported by service JavaScript   
| Statement | Description | Example |
| :-- | :-- | :-- |
| Comment | For better understanding of a script logic, use comments to describe the script logic if necessary. For the convenience of developers in different countries and regions, write comments in English and avoid using multi-byte characters. | Line comment:
//Comment in a line.

Block comment:

/\*
Comment in a block.
Comment in a block.
\*/

 |
| Variable declaration (var) and value | When using a variable, you must explicitly declare the variable using the keyword var. Do not assign a value to a variable when the variable is not declared. | var radius = 5;
var diameter = radius \* 2;
var area;
area = 3.14 \* radius \* radius;

 |
| Control statement (if) | To avoid logic uncertainty caused by implicit type conversion, ensure that the expression calculation result in the if statement is of the Boolean type. | var a = 1;
var b = 2;
var result;
var op = "+";

if (op == "+") {
    result = a + b;
} else if (op == "-") {
    result = a - b;
} else {
    result = 0;
}

 |
| Control statement (switch) | Only numeric and string values should be used for control. If the Boolean type needs to be used for control, use if... Else statement. Use literals instead of variables to express values in the case statement. The break statement must be used at the end of the code block of each case statement to avoid process errors. Unless the processing logic is specified, this must be the case. Multiple cases in the same switch statement should not have the same value. | var a = 1;
var b = 2;
var result;
var op = "+";

switch (op) {
    case "+":
        result = a + b;
        break;
    case "-":
        result = a - b;
        break;
    default:
        result = 0;
        break;
}

 |
| Loop statement (for) | Check whether the loop control variable in the for loop needs to be re-declared. If you want to reuse a previously declared variable, you do not need to use the var keyword for declaration. Otherwise, use the var keyword for declaration. The conditions in the for statement must be the same as those in the if statement. Do not use floating point numbers and integers that exceed the safe integer range for loop control of equality judgment because these values are not accurate and may never be equal. Do not introduce implicit type conversion in loop control to avoid extra performance overhead and unintentional uncertainty. Note that the variables declared in the loop body may function beyond the loop body. The local variables used in the loop body should not have the same names as the variables outside the loop body. If you need to assign a value to a variable outside the loop, declare the variable before the loop. You can use the continue and break statements in the loop body. | var sum = 0;
for (var i = 1; i <= 10; ++i) {
    sum += i;
}

 |
| Loop statements (while, do, ...) while) | The conditions in the while statement must be the same as those in the if statement. Note that the variables declared in the loop body may function beyond the loop body. The local variables used in the loop body should not have the same names as the variables outside the loop body. If you need to assign a value to a variable outside the loop, declare the variable before the loop. You can use the continue and break statements in the loop body. | while:

var sum = 0;
var i = 1;
while (i <= 10) {
    sum += i;
    i++;
}

do ... while:

var sum = 0;
var i = 1;
do {
    sum += i;
    i++;
} while (i <= 10)

 |
| Capture error (try... catch ... finally { | Not all errors in the try block can be caught by catch. For example, when the program in the try block is executed, errors such as insufficient memory or exceeding the limit of the number of script execution instructions cannot be captured by the catch command. In this case, the script execution is terminated. Do not use the return, break, or continue statement in the finally block to end the finally block abnormally. | try ... catch:

try {
    do\_something\_may\_cause\_error();
} catch (err) {
    process\_error(err);
}

try ... finally {

try {
    do\_something\_may\_cause\_error();
} finally {
    do\_something\_regardless\_of\_error();
}

try ... catch ... finally {

try {
    do\_something\_may\_cause\_error();
} catch (err) {
    process\_error(err);
} finally {
    do\_something\_regardless\_of\_error();
}

 |
| Throwing an Error (throw) | Although the native JavaScript can throw data of any type, it is recommended that only the ScriptError object defined by ADC be thrown to better connect to the orchestration capabilities such as the ADC service and GUI, and use the error code capability. | throw new ScriptError("Process order failed.");

 |
| Defining a Function | Do not define nested functions. Arrow functions are not supported. Do not use functions to create objects. Variables used only inside a function must be explicitly declared in the function to avoid modifying variables with the same name outside the function. Do not depend on the dynamic scope and lexical scope features. If variables need to be transferred to a function, the variables must be transferred in explicit mode through the input parameters of the function. The variables cannot depend on the context of the function to be invoked or the context of the function to be defined. | function hello(name) {
    console.log('Hello ' + name + "!");
}

 |
| Creating an Object (new) | Create an object. | \- | **Parent topic:** [[JavaScript Syntax Reference|JavaScript Syntax Reference]]