---
title: "Rule: Agent in the Runtime-State Environment Can Obtain the Retrieval Result of the Sample Library Only by Using the Fixed Character String {{ctx_lib_data}}"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370397856.html"
depth: 6
---
# Rule: Agent in the Runtime-State Environment Can Obtain the Retrieval Result of the Sample Library Only by Using the Fixed Character String {{ctx\_lib\_data}}

**Description**: The agent orchestration provides the capability of customizing the sample library. The business side presets simple sample library data for the agent to retrieve data. The agent in the runtime-state environment can obtain the retrieval result of the sample library only by using the fixed character string **{{ctx\_lib\_data}}**.

**Check guide**:

1\. Access the agent prompt management page, click the **Sample Library** tab, and create a sample library.

2\. Access the agent flow orchestration page, select the LLM node, and reference the sample library.

**Positive example**:

![[en-us_image_0000002370237568.png]]

![[en-us_image_0000002370087372.png]]

**Tool supported or not**: no

**Specification name**: General\_Ctx\_Variable\_Standardization

**Severity**: minor

**Parent topic:** [[Intelligent Component Orchestration|Intelligent Component Orchestration]]