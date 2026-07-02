---
title: "Comparison Between JUEL and TEL"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/workflow_057.html"
depth: 5
---
# Comparison Between JUEL and TEL

Although JUEL and TEL are two languages with differences in syntax and functions, their functions are basically matched and can be replaced with each other.

![[note_3.0-en-us.png]]

This topic only lists the common TEL specifications of BPM. For details, see the TEL general syntax specifications.

   
| Category | JUEL | TEL | Difference |
| :-- | :-- | :-- | :-- |
| Distinguishing constants and variables | 
-   Variable: The variable is packaged in **${}**, for example, **${api\_input.title eq "abc"}**.
-   Constant: The constant is not packaged in **${}**, for example, **abc** and **"abc"**.

 | -   Variable: The variable is unquoted or is package in double quotation marks ("). A variable that is unquoted must start with a letter, digit, or an underscore (\_). A variable that is packaged in double quotation marks (") is escaped using backslashes (\\), for example, **api\_input.title = 'abc'** and **"api\_input"."title" = 'abc'**.
-   Constant: The constant is packaged in single quotation marks ('), for example, **'api\_input.title'**.

 | The variable is packaged by ${} in JUEL while the variable is unquoted or is packaged in double quotation marks (") in TEL. |
| Variable access | The variable can be accessed through a period (.), get, or square brackets (\[\]). The following shows examples:

-   ${api\_input.title = "abc"}
-   ${api\_input."title" = "abc"}
-   ${api\_input.get("title") = "abc"}
-   ${api\_input\["title"\] = "abc"}

 | The variable can be accessed through a period (.) or \[index\]. The following shows examples:

-   api\_input.title = 'abc'
-   api\_input.users\[0\] = 'test'

 | The variable cannot be accessed by using get or \["Variable name"\] in TEL. |
| Relation operators | -   \==, !=, <, >, <=, >=
-   eq, ne, lt, gt, le, ge

For example, ${8 == 8} or ${8 eq 8}. The using method of other operators is similar to the example. | \=, !=, <, >, <=, >= | 1.  Alias is not used in TEL.
2.  An equal sign (=) is used to indicate equal to in TEL.
3.  Comparison: Only the comparison between two digits is supported in TEL while the comparison between character strings, JSON (converted to character strings), and digits is supported in JUEL.

 |
| Logical operators | and or &&, or or ||, not or ! | and, or, ! | In TEL, each operator is unique and does not have an alias. |
| Arithmetic operators | +, -, \*, div or /, mod or % | +, -, \*, /, % | In TEL, each operator is unique and does not have an alias. |
| Null operation | empty A

-   If A is a null object, **true** is returned.
-   If A is an empty string, **true** is returned.
-   If A is an empty array, **true** is returned.
-   Otherwise, **false** is returned.

 | -   string.is\_empty(null) = true
-   string.is\_empty('') = true
-   string.is\_empty(' ') = false
-   string.is\_empty('bob") = false
-   collection.is\_empty(list\_input) = false //No data exists in the list.
-   collection.is\_empty(map\_input) = false //No data exists in the map.
-   collection.is\_empty(null) = true

 | An operator is used to determine whether an object is empty in JUEL while different methods are provided for determining whether an object is empty in TEL. |
| Ternary expression | ${A ? B : C} | A ? B : C | The syntax is the same. (For details about how to distinguish variables and constants, see the first item in the table.) |
| Common built-in functions | N/A | Multiple functions corresponding to string, math, crypto, collection, and time are provided. | \- |
| BPM built-in functions | The following functions can be customized for extension:

-   BpmUtils.isLastTaskSuccess()
-   BpmUtils.isAllTaskSuccess()
-   BpmUtils.getLastTaskResult()
-   BpmUtils.getAllTaskResult()

 | The following functions can be customized based on the TEL extension registration mechanism for extension:

-   bpm\_utils.is\_last\_task\_success()
-   bpm\_utils.is\_all\_tasks\_success()
-   bpm\_utils.get\_last\_task\_result()
-   bpm\_utils.get\_all\_tasks\_result()

 | The customized extension is supported both in JUEL and TEL. | **Parent topic:** [[Guidance for the Conditional Expressions|Guidance for the Conditional Expressions]]