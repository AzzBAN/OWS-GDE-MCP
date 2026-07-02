---
title: "Rule: Do Not Use Global Variables in Common Functions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001615507192.html"
depth: 6
---
# Rule: Do Not Use Global Variables in Common Functions

**Description**: If a global variable is defined in a common function, the variable may be used or modified by different APIs at the same time, resulting in unexpected results.

**Check guide**:

Check whether the common JS functions in the API package contain variables that are not declared using **var** or **let**.

**Negative example**:

The definition similar to that of **response** in the following function changes the **response** variable to a global variable:

...
function getFaultBody(\_\_headers, \_exception) {
	if (\_exception && \_exception.serviceSoapEnvelope && JSON.stringify(\_exception.serviceSoapEnvelope) !== {}){
                var envelope = \_exception.serviceSoapEnvelope;
		**response = {};**
		**response.error = {};**
...

**Rectification suggestion**:

Use **var** or **let** to define variables in the common functions as local variables in the method.

**Tool supported or not**: no

**Specification name**: General\_API\_Avoid\_Using\_Global\_Variable\_in\_Public\_Scripts

**Severity**: major

**Parent topic:** [[Openness Integration|Openness Integration]]