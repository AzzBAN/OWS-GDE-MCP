---
title: "Rule: deleteByTql or updateByTql Operation Cannot Be Performed on Models with a Large Amount of Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162800374.html"
depth: 6
---
# Rule: deleteByTql or updateByTql Operation Cannot Be Performed on Models with a Large Amount of Data

**Description**: If the deleteByTql and updateByTql operations are performed on models with a large amount of data, the database performance consumption is high.

**Check guide**: Check whether the RunScript script calls the deleteByTql and updateByTql services.

**Positive example**: Based on the actual scenario, specify the maximum number of data records that can be deleted or updated in the tql table each time to avoid affecting database functions. In the data clearance and archiving scenarios, configure model archiving to replace deleteByTql and updateByTql.

**Tool supported or not**: no

**Specification name**: General\_Model\_Avoid\_Delete\_Or\_Update\_By\_Tql\_on\_Large\_Data\_Volume\_Model

**Severity**: major

**Parent topic:** [[Model|Model]]