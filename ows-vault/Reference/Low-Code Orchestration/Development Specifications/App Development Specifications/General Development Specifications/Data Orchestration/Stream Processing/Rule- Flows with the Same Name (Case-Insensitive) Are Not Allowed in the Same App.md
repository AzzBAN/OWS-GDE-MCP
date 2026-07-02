---
title: "Rule: Flows with the Same Name (Case-Insensitive) Are Not Allowed in the Same App"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001871779666.html"
depth: 6
---
# Rule: Flows with the Same Name (Case-Insensitive) Are Not Allowed in the Same App

**Specification name**: General\_DataFactory\_Stream\_Flow\_Name\_Case\_Insensitive

**Description**: The names of data orchestration flows are case insensitive. An app cannot contain flows with the same name (even the same letters in different cases are not allowed).

**Check guide**: Check the names of all flows in the same app. If some flows have the same name (case-insensitive), change the flow names.

**Impact**: If this rule is violated, some flows may be lost during app installation, resulting in an app upgrade or installation failure.

**Parent topic:** [[Stream Processing|Stream Processing]]