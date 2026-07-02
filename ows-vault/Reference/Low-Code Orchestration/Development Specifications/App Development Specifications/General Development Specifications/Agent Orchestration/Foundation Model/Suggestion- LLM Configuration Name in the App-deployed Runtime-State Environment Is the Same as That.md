---
title: "Suggestion: LLM Configuration Name in the App-deployed Runtime-State Environment Is the Same as That Used in the Develop-State Environment During Orchestration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002343774225.html"
depth: 6
---
# Suggestion: LLM Configuration Name in the App-deployed Runtime-State Environment Is the Same as That Used in the Develop-State Environment During Orchestration

**Description**: The orchestrated app runs in the runtime-state environment. The LLM configuration name and model name used in the runtime-state environment and develop-state environment during orchestration must be the same.

When **Allow Foundation Model Switching** is disabled (disabled by default), the LLM configuration name and model name used in the runtime-state environment must be the same as those used in the develop-state environment during orchestration.

When **Allow Foundation Model Switching** is enabled, the configuration name and model name used in the runtime-state environment can be different from those used in the develop-state environment during orchestration. The names can be adjusted during running.

**Check guide**: Find the foundation model access configuration in the environment and check whether the configuration name and model name in the develop-state environment are the same as those in the runtime-state environment.

![[en-us_image_0000002370261810.png]]

**Positive example**:

**Rule**:

Foundation model series - R&D organization

——Foundation model 1

——Foundation model 2

**Example 1**:

GTSLLM series - AIPDU

——Product-GTSLLM-Standard

——DeepSeek-R1-Distill-GTSLLM-Pro

**Example 2**:

UniAIGC series - BPIT

——GTS-Domain-LLM

**Tool supported or not**: no

**Specification name**: General\_Agent\_Tools\_Standardization

**Severity**: suggestion

**Parent topic:** [[Foundation Model|Foundation Model]]