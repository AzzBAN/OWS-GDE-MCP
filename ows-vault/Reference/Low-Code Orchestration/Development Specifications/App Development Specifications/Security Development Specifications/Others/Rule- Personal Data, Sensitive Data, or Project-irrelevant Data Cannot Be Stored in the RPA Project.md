---
title: "Rule: Personal Data, Sensitive Data, or Project-irrelevant Data Cannot Be Stored in the RPA Project Directory"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963848.html"
depth: 5
---
# Rule: Personal Data, Sensitive Data, or Project-irrelevant Data Cannot Be Stored in the RPA Project Directory

**Description**: When a project in Studio is packaged and released, the project directory is compressed into a release package. If personal data or sensitive data is stored in this directory, data leakage risks exist.

**Check guide**: Check the project package directory to ensure that there is no personal or sensitive data file.

**Positive example**: none

**Negative example**: The account password file is stored in the project directory and compressed into a package during release package creation.

**Tool supported or not**: no

**Specifications name**: Security\_SensitiveData\_RPA\_DoNotStoreInProject

**Severity**: critical

**Orchestration scenario**: RPA orchestration

**Parent topic:** [[Others|Others]]