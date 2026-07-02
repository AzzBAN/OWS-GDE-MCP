---
title: "Rule: Cross-Module Parent Permission Configuration Must Depend on the Module"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804076.html"
depth: 6
---
# Rule: Cross-Module Parent Permission Configuration Must Depend on the Module

**Description**: You can configure the parent permission. If the parent permission is not the permission item of the current module, add the module where the parent permission is located to the dependent module in the module configuration.

**Check guide**: 1. Query the parent permission ID of the permission item and check whether the permission item belongs to another module. 2. If no, check whether the module where the parent permission is located is added to the module on which the current module depends.

**Tool supported or not**: no

**Specification name**: General\_Permission\_Not\_CurrentModule\_Parent\_Need\_Config\_Module\_Dependency

**Severity**: major

**Parent topic:** [[Permission|Permission]]