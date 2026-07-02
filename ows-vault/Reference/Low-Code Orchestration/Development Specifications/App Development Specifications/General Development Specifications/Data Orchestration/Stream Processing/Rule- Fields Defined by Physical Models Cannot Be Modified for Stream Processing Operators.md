---
title: "Rule: Fields Defined by Physical Models Cannot Be Modified for Stream Processing Operators"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002179488742.html"
depth: 6
---
# Rule: Fields Defined by Physical Models Cannot Be Modified for Stream Processing Operators

**Specification name**: General\_DataFactory\_Stream\_Physical\_Model\_Field\_Restriction

**Note**: Operators of stream processing engines driven by physical models cannot modify the fields defined by physical models.

**Check guide**: Check whether fields defined by physical models need to be modified for stream processing operators. If yes, create a new physical model.

**Impact**: If physical models do not match the fields, data may be abnormal, even an error may be reported, and the flow may fail to be executed.

**Parent topic:** [[Stream Processing|Stream Processing]]