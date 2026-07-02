---
title: "Suggestion: Ensure Cohesion and Atomicity of JOBS Flow Design"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002328346894.html"
depth: 6
---
# Suggestion: Ensure Cohesion and Atomicity of JOBS Flow Design

**Specification name**: General\_DataFactory\_Unified\_Schedule\_Cohesion\_Atomicity

**Description**: You are advised to ensure the cohesion and atomicity of JOBS flow design and not to include multiple irrelevant computing task workflows in one flow.

**Check guide**: Check a JOBS flow. If there are multiple data flows in the JOBS flow, check whether the data flows are irrelevant computing task workflows. If yes, split the irrelevant computing task workflows to different JOBS flows.

**Impact**: If multiple irrelevant computing task workflows are configured in a flow, the service atomicity of the flow may be lost, the usability of functions such as flow-based recalculation and retry functions may deteriorate, and the topology dependencies between flows may be disordered.

**Parent topic:** [[Data Job Schedule|Data Job Schedule]]