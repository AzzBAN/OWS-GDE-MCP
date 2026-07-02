---
title: "Suggestion: Set Open Level of Orchestration Elements to Module or Project Level"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403949.html"
depth: 5
---
# Suggestion: Set Open Level of Orchestration Elements to Module or Project Level

**Description**: The GDE develop-state environment provides the open level setting function for some orchestration elements. Developers can set the open level to open the access capabilities of the corresponding orchestration elements to a certain range. Currently, the open levels listed in the following table are supported.

**Table 1** Open levels    
| Open Level | Capability Explanation | Default Configuration | Suggestion |
| :-- | :-- | :-- | :-- |
| Module | Other orchestration elements in the same module can call the orchestration element of this openness level. | Default | Recommended. The configuration complies with the minimum permission principle. You are advised to use this level. |
| Project | Other orchestration elements in the same project can call the orchestration element of this openness level. | Non-default | Evaluation is required. This level is used when it is required after service scenario evaluation. |
| Public | An orchestration element in any project can call the orchestration element of this openness level. | Non-default | Exercise caution when using this level. This configuration expands the attack scope and may bring security and compatibility problems. | **Check guide**: Orchestration elements that support the openness level configuration include models, services, events, as well as tool orchestration and flow orchestration in agent orchestration. The following uses the Model element as an example. The operations for other elements are similar.

1.  Log in to the develop-state environment, select a desired project, choose **Model** from the menu, and drag **Data Model** or select an existing model.
2.  In the displayed dialog box or on the right, check whether **Open Level** is set to **Module**.

**Positive example**:

When creating a model, set **Open Level** to **Module**.

![[en-us_image_0000001521796013.png]]

**Tool supported or not**: yes

**Specification name**: Security\_AccessControl\_Open\_Level

**Category**: non-bottom-line check item

**Severity**: suggestion

**Orchestration scenario**: general job orchestration and agent orchestration

**Parent topic:** [[Access Control|Access Control]]