---
title: "Rule: Names of Images in a ZIP Package Must Be Unique, Excluding Chinese and English Brackets"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523401.html"
depth: 6
---
# Rule: Names of Images in a ZIP Package Must Be Unique, Excluding Chinese and English Brackets

**Description**: The ZIP package to be uploaded cannot contain images with the same name, for example, **（name）** and **(name)**.

**Check guide**: Open the ZIP package of the document to be uploaded and check whether the files with the same name (excluding Chinese and English brackets) exist in the **images** folder.

**Negative example**: Both **demo（notes）.zip** and **demo(notes).zip** exist in the ZIP package.

**Tool supported or not**: no

**Specification name**: General\_Document\_Images\_Name\_Not\_Equals\_In\_Zip

**Severity**: minor

**Parent topic:** [[Document|Document]]