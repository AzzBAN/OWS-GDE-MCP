---
title: "Operators and Expressions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_005.html"
depth: 6
---
# Operators and Expressions

**Table 1** Operators supported by service JavaScript  
| Operator | Description |
| :-- | :-- |
| Arithmetic operators |
| +, -, \*, /, %, ++, -- | The operands must be of the numeric type. |
| +=, -=, \*=, /=, %= |
| Assembling character strings |
| + | The addition of a character string and a number is actually a combination of character strings. Therefore, when using the + operator, pay attention to the type of the operand. |
| += |
| Test operators |
| \==, ! = | Note that if the operand types are inconsistent, implicit type conversion occurs. |
| \===, ! == | \- |
| \>, >=, <, <= | Note that if the operand types are inconsistent, implicit type conversion occurs. |
| Logical operators |
| &&, ||, ! | The operands must be of the Boolean type. |
| Other |
| ... ? ... : ... | The first operand should be of the Boolean type. The types of the last two operands must be the same. |
| typeof | \- | ![[note_3.0-en-us.png]]

-   Pay attention to the impact of special values such as undefined, null, NaN, and Infinity on the calculation result. If necessary, perform verification first.
-   Implicit type conversions should be avoided to avoid uncertainty and incomprehensibility.

**Parent topic:** [[JavaScript Syntax Reference|JavaScript Syntax Reference]]