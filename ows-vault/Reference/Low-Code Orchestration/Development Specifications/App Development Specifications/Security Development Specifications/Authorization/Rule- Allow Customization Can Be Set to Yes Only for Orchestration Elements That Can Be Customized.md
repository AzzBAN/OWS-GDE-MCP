---
title: "Rule: Allow Customization Can Be Set to Yes Only for Orchestration Elements That Can Be Customized"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002471039952.html"
depth: 5
---
# Rule: Allow Customization Can Be Set to Yes Only for Orchestration Elements That Can Be Customized

**Description**: GDE provides the capability of controlling whether orchestration elements can be customized to prevent service process exceptions caused by unexpected customization of service elements. **Allow Customization** can be set by developers to **Yes** only for orchestration elements that can be customized.

**Check guide**:

**Allow Customization** can be set to **Yes** only for models that can be customized.

In the model list, click the edit icon of each model to check whether **Allow Customization** for the model is properly set.

As shown in the following figure, **Allow Customization** is set to **No** for the model.

![[en-us_image_0000002357888053.png]]

**Positive example**: Models with **Allow Customization** being set to **Yes** actually need to be customized.

**Negative example**: Customization is allowed for models that do not need to be customized, for example, app internal models that are not exposed externally.

**Allow Customization** can be set to **Yes** only for agents that can be customized.

The flows, tools, prompts, and prompt sample libraries in the agent orchestration provide the customization control capability to prevent service process exceptions caused by unexpected customization. **Allow Customization** can be set by developers to **Yes** only for agent orchestration elements that can be customized.

**Check guide**: In the element list of agent orchestration, click the edit icon of each element to check whether **Allow Customization** for the element is properly set. The following uses flow orchestration elements as an example. The operations for other elements are similar.

![[en-us_image_0000002365094017.png]]

**Positive example**: Elements with **Allow Customization** being set to **Yes** actually need to be customized.

**Negative example**: Customization is allowed for elements that do not need to be customized, for example, app internal flows that are not exposed externally.

**Tool supported or not**: yes

**Specification name**: Security\_Date\_Is\_Customization

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: general job orchestration and agent orchestration

**Parent topic:** [[Authorization|Authorization]]