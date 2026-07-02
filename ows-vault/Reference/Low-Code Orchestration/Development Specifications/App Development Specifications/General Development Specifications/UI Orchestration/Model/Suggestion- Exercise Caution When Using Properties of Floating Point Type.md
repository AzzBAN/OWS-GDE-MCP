---
title: "Suggestion: Exercise Caution When Using Properties of Floating Point Type"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523353.html"
depth: 6
---
# Suggestion: Exercise Caution When Using Properties of Floating Point Type

**Description**: Model properties of Floating Point type are stored as decimal fields in relational databases and as double-precision floating-point numbers in Elasticsearch. The decimal type has restrictions on the number of valid digits and decimal places, and the double-precision floating-point number has the feature of inaccurate value. Therefore, when using the properties of Floating Point type, you must consider the range and precision of the stored number, in addition, the stored value may be inconsistent with the queried value (for example, truncation or a value that cannot be accurately represented by a floating-point number).

**Check guide**: Review the properties of Floating Point type and check whether the preceding conditions are fully considered.

**Negative example**: When properties of Floating Point type are used to save prices and amounts, accurate values must be ensured. Otherwise, the saved data may be distorted because the underlying data storage uses inaccurate data types. You can multiply the value by 10 times, save the integer, and process the integer by the corresponding multiple when using it.

**Exception scenarios**: none

**Tool supported or not**: no

**Specification name**: General\_Model\_Use\_Decimal\_Attributes\_with\_Care

**Severity**: suggestion

**Parent topic:** [[Model|Model]]