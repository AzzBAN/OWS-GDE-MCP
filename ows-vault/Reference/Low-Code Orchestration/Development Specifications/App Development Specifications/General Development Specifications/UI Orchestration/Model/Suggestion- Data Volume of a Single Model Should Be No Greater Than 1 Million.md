---
title: "Suggestion: Data Volume of a Single Model Should Be No Greater Than 1 Million"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643317.html"
depth: 6
---
# Suggestion: Data Volume of a Single Model Should Be No Greater Than 1 Million

**Description**: The data volume that can be carried by each type of model is limited. For example, it is recommended that the data volume of a single table in a relational database be less than or equal to 1 million. A common data model is used as an example. A model corresponds to a table in a relational database. If the data volume of a single table is too large, the performance of adding, deleting, modifying, and querying data in the table is greatly affected. To prevent such performance problems, the business side must properly plan the data volume of each model to reduce unnecessary rows and use features such as model data archiving to prevent continuous increase of model data volume.

**Check guide**: Evaluating the data volume of each model is essential for model design. The model should be fully evaluated and tested when it is designed. If the data volume of a model exceeds the specifications, you can use the model division method to support a larger scale.

**Negative example**: When you define a model, do not consider the data volume of the model and the impact of the data volume on performance.

**Exception scenario**: If the data volume of a model exceeds the specifications, the model can be used on the basis of sufficient evaluation and test, for example, operations are not frequent, the impact on performance overhead is small, and the response time requirement is not high.

**Tool supported or not**: no

**Specification name**: General\_Model\_Evaluate\_And\_Design\_The\_Data\_Volume\_Of\_The\_Model

**Severity**: suggestion

**Parent topic:** [[Model|Model]]