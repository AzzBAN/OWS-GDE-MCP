---
title: "Suggestion: The Number of Nested Layers of the Foreach Operator Should Be No Greater Than Four"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001653992941.html"
depth: 6
---
# Suggestion: The Number of Nested Layers of the Foreach Operator Should Be No Greater Than Four

**Specification name**: General\_DataFactory\_AIP\_ Avoiding\_Many\_Nesting

**Description**: It is recommended that a maximum of four layers be nested in the Foreach operator.

**Check guide**: Check whether more than four layers are nested in the Foreach operator in the app flow.

**Impact**: Too many nested layers of the Foreach operator may cause DoS attacks.

**Parent topic:** [[Data Integration|Data Integration]]