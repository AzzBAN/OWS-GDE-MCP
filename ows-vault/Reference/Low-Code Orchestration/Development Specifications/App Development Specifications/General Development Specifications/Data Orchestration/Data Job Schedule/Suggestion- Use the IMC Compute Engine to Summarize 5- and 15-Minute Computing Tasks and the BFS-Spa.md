---
title: "Suggestion: Use the IMC Compute Engine to Summarize 5- and 15-Minute Computing Tasks and the BFS-Spark Compute Engine to Summarize Hourly or Longer Computing Tasks"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001614064512.html"
depth: 6
---
# Suggestion: Use the IMC Compute Engine to Summarize 5- and 15-Minute Computing Tasks and the BFS-Spark Compute Engine to Summarize Hourly or Longer Computing Tasks

**Specification name**: General\_DataFactory\_Aggregation\_Calculation\_IMC\_Suitable\_Scenario

**Description**: During aggregation and computing, the IMC engine executes computing tasks in the memory. The computing performance is high, but a large amount of memory is occupied. Therefore, for high running efficiency, the IMC engine is suitable for processing small-granularity computing tasks, such as 5- and 15-minute tasks. You are advised to use the BFS-Spark compute engine for hourly or longer computing tasks. If the aggregation interval is longer than one day, you are advised to set **Enable Rolling Computing** to **Yes** to achieve optimal running efficiency.

**Impact**: Hourly IMC computing tasks occupy too many memory resources, reducing computing efficiency.

**Check guide**: Check whether there are hourly IMC computing tasks.

**Positive example**: Create an hourly BFS-Spark aggregation and computing task that depend on a 15-minute IMC aggregation and computing task.

**Parent topic:** [[Data Job Schedule|Data Job Schedule]]