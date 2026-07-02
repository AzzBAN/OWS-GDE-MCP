---
title: "Suggestion: Use Less Than Five Model Properties of Reference Type"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162958920.html"
depth: 6
---
# Suggestion: Use Less Than Five Model Properties of Reference Type

**Description**: For a single model, the total number of properties of reference type should be less than 5. When you query a model of reference type, convert its property value from **id** to **keycode**. When you write data to this model, convert its property value from **keycode** to **id**. The more properties of a reference type in a single model, the more such conversions and the greater the performance overhead.

**Check guide**: Open the property list of a model in the develop-state environment. If there are properties of a reference type, check whether the total number of these properties is less than 5.

**Positive example**: The total number of properties of reference and dependency types is less than 5.

**Negative example**: The total number of properties of reference and dependency types reaches or exceeds 5.

**Tool supported or not**: no

**Specification name**: General\_Model\_Reference\_Type\_Attribute\_Less\_Than\_5

**Severity**: suggestion

**Parent topic:** [[Model|Model]]