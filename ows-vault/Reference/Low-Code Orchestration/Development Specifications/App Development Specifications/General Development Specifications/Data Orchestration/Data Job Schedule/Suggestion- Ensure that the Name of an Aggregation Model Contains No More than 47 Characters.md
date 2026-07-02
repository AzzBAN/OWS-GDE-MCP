---
title: "Suggestion: Ensure that the Name of an Aggregation Model Contains No More than 47 Characters"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001613744640.html"
depth: 6
---
# Suggestion: Ensure that the Name of an Aggregation Model Contains No More than 47 Characters

**Specification name**: General\_DataFactory\_Aggregation\_Calculation\_No\_Long\_Model\_Name

**Description**: When creating an aggregation model, ensure that its name contains no more than 47 characters. If the name contains more than 47 characters, the names of aggregation and computing tasks are highly similar, which may cause task name confusion and reduce subsequent development efficiency.

**Check guide**: Check whether the name of the aggregation model contains more than 47 characters.

**Positive example**: When naming an aggregation model, ensure that the name has business meaning and is short and easy to identify, for example, **SDR\_HTTP\_THRUPUT\_REGION**.

**Parent topic:** [[Data Job Schedule|Data Job Schedule]]