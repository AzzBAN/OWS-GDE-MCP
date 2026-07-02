---
title: "Suggestion: Use the JSON Tool Provided by API Fabric to Replace the Built-in JS Tool"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001663507201.html"
depth: 6
---
# Suggestion: Use the JSON Tool Provided by API Fabric to Replace the Built-in JS Tool

**Description**: If the built-in JSON objects of the JS are used to parse packets, errors may occur. As a result, packets cannot be parsed correctly. You are advised to use the JSON tool **com.huawei.fabric.common.utils.JsonUtils** provided by API Fabric.

**Check guide**:

Check whether all JS scripts in the API package contain the JSON usage in the following figure.

![[en-us_image_0000001661687833.png]]

**Recommended usage**:

var obj = MessageDecode.jsonDecode("...")
var bytes = MessageEncode.jsonEncode(obj)

**Tool supported or not**: no

**Specification name**: General\_API\_Prioritize\_Using \_the\_SDK\_Provided\_by\_Fabric

**Severity**: suggestion

**Parent topic:** [[Openness Integration|Openness Integration]]