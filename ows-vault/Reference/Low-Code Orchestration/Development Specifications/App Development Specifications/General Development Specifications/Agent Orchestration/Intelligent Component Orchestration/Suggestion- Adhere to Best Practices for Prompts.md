---
title: "Suggestion: Adhere to Best Practices for Prompts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002370557732.html"
depth: 6
---
# Suggestion: Adhere to Best Practices for Prompts

**Description**: The agent orchestration service allows business personnel customize prompts based on site requirements. However, prompt customization must comply with the content specifications. Direct and indirect prompt injection is prohibited, including but not limited to target hijacking, negative guidance, and role play.

**Check guide**: Go to the agent tool management page and check the prompt content.

**Positive example**:

![[en-us_image_0000002370203206.png]]

**Best practice of the prompt**:

**The following is an example of providing a single sample or a few samples in the prompt**:

1\. Single-sample prompts provide one example, so they are called single-sample prompts. The idea is that the model has an example that it can imitate to best complete the task.

2\. Few sample prompts provide multiple examples (three to five in most cases) for the model. The idea is similar to that of single-sample prompts, but multiple examples increase the chances of the model following the pattern.

3\. For more complex tasks, more examples may be required, but examples cannot be too many due to the input length limit of the model.

Core idea: Provide one to five input/output examples in the prompt.

Applicable scenarios/Advantages: When the no-sample prompt effect is poor, this idea is that the model has an example that it can imitate to best complete the task.

Key points/Precautions: The quality and diversity of examples are critical.

Template:

Task: \[Task description\]
Example 1:
Input: \[input example 1\]
Output: \[output example 1\]

Example 2:
Input: \[input example 2\]
Output: \[output example 2\]

Example 3:
Input: \[input example 3\]
Output: \[output example 3\]

Handle the following information:
Input: \[actual input\]
Output:

**Identity setting: system/role/context prompt**

1\. The system prompt sets the overall context and purpose of the LLM.

2\. The role prompt assigns a specific role or identity to be used to the LLM.

3\. The context prompt provides details or background information related to the current dialog or task.

Core idea: Define the AI identity, that is, what is your task, who are you, and what do you know.

Applicable scenarios/Advantages: Customize the tone, style, and knowledge focus of the AI to improve the relevance of the answers. The effects are much better when the three are used together.

Key points/Precautions: Define the background, role, and context clearly and accurately.

Template:

1\. System prompt

You are \[role description\]. Your task is \[task description\]. Ensure your response \[specific requirements\].

2\. Role prompt

Answer the following questions as \[role\] in \[tone\].
\[Question or task\]

3\. Context prompt

Background: \[Provide related background information.\]
Context: \[Describe the current context.\]
Task: \[Provide specific task requirements.\]

**Tool supported or not**: no

**Specification name**: General\_Tools\_Name\_Standardization

**Severity**: suggestion

**Parent topic:** [[Intelligent Component Orchestration|Intelligent Component Orchestration]]