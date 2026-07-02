---
title: "Suggestion: Use Flow Dependencies Instead of Task Dependencies"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002362345301.html"
depth: 6
---
# Suggestion: Use Flow Dependencies Instead of Task Dependencies

**Specification name**: General\_DataFactory\_Unified\_Schedule\_Prioritize\_Process\_Dependencies

**Description**: In the production system, there are a large number of flows and tasks. Flow dependencies instead of task dependencies are preferentially used as flow dependencies make the dependencies simpler and clearer.

**Check guide**: Check a JOBS flow. If there are dependent operators in the JOBS flow, check these dependent operators. If task dependencies are used, evaluate the impact of replacing task dependencies with flow dependencies. If the replacement has no impact or little impact, replace task dependencies with flow dependencies.

**Impact**: If a large number of dependent tasks are used, the topology dependencies between flows may be disordered and difficult to maintain.

![[en-us_image_0000002362346205.png]]

**Parent topic:** [[Data Job Schedule|Data Job Schedule]]