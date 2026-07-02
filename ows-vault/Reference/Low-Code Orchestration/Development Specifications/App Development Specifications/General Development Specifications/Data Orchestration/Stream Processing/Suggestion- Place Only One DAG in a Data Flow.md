---
title: "Suggestion: Place Only One DAG in a Data Flow"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001917578969.html"
depth: 6
---
# Suggestion: Place Only One DAG in a Data Flow

**Specification name**: General\_DataFactory\_Stream\_One\_DAG

**Description**: Place only one directed acyclic graph (DAG) in a data flow. If there are multiple DAGs, you are advised to split them into multiple flows.

**Check guide**: Check the number of DAGs in the data flow.

**Impact**: If a data flow contains multiple DAGs, the flow readability is poor, there is a high probability that an error is reported during app running, and flow-based operations cannot run properly.

**Parent topic:** [[Stream Processing|Stream Processing]]