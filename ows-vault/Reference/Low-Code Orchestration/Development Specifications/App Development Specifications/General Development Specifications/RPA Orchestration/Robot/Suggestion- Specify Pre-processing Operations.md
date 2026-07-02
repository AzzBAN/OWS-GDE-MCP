---
title: "Suggestion: Specify Pre-processing Operations"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001768145112.html"
depth: 6
---
# Suggestion: Specify Pre-processing Operations

**Description**: You need to check whether a robot script contains specific pre-processing operations used to initialize the running environment and ensure the proper running of service scripts.

**Check guide**: Delete historical data downloaded for previous tasks, create folders and files required by a process, and close programs, such as Excel, Word, and WPS, that may affect robot processes.

**Positive example**: As shown in the following figure, the project obtains the authentication token, initializes the environment, deletes junk data, and backs up data in the pre-processing operations.

![[en-us_image_0000001746824314.png]]

**Tool supported or not**: no

**Specification name**: General\_RPA\_Clarify\_Pre\_Operation

**Severity**: suggestion

**Parent topic:** [[Robot|Robot]]