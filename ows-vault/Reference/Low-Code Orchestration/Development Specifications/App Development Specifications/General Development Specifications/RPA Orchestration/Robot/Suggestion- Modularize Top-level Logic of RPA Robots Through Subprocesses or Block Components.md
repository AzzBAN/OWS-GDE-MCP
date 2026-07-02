---
title: "Suggestion: Modularize Top-level Logic of RPA Robots Through Subprocesses or Block Components"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643397.html"
depth: 6
---
# Suggestion: Modularize Top-level Logic of RPA Robots Through Subprocesses or Block Components

**Description**: All functions cannot be stacked in one script. The robot process can be modularized by subprocesses to improve the process development and maintenance efficiency.

**Check guide**: Check the main script of the process, which includes only subprocesses and block components.

**Positive example**: A clear layered logic is designed.

![[en-us_image_0000001469921692.png]]

**Negative example**: All service logics are stacked in one script, making the development and maintenance difficult.

![[en-us_image_0000001469920996.png]]

**Tool supported or not**: no

**Specification name**: General\_RPA\_Top\_Level\_Logic\_should\_Be\_Modularized

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]