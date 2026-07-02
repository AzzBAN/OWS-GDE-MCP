---
title: "Rule: Personal Data, Sensitive Data, or Project-irrelevant Process Files Cannot Be Stored in the RPA Project Directory"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963780.html"
depth: 6
---
# Rule: Personal Data, Sensitive Data, or Project-irrelevant Process Files Cannot Be Stored in the RPA Project Directory

**Description**: When a project in Studio is packaged and released, the project directory is compressed into a release package. If a personal data or sensitive data file is stored in this directory, improper data disclosure risks may occur.

**Check guide**: Check the project package directory to ensure that there is no personal or sensitive data file.

**Positive example**: none

**Negative example**: The account password file is stored in the project directory and compressed into a package during release package creation.

![[en-us_image_0000001520912021.png]]

**Tool supported or not**: no

**Specification name**: General\_RPA\_Forbidden\_Keep\_Sensitive\_File\_in\_Project

**Severity**: major

**Orchestration scenario**: RPA orchestration

**Parent topic:** [[Robot|Robot]]