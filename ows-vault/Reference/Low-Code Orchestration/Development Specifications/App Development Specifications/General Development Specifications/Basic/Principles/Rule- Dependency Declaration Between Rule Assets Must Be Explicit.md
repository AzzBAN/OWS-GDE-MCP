---
title: "Rule: Dependency Declaration Between Rule Assets Must Be Explicit"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001522076945.html"
depth: 6
---
# Rule: Dependency Declaration Between Rule Assets Must Be Explicit

**Description**: Dependencies should be explicitly defined for assets to facilitate use.

1\. For the building block and app assets on which the app depends, the corresponding dependency needs to be added and saved during packaging.

2\. Assets should not have circular references.

**Check guide**: If there is an external dependency, check whether the project that depends on the configuration exists in the basic project definition. During the configuration, you are advised to add the earliest version to the dependency in addition to the name of the project that depends on the configuration.

**Tool supported or not**: no

**Specification name**: General\_Basic\_Explicit\_Dependency

**Severity**: major

**Parent topic:** [[Principles|Principles]]