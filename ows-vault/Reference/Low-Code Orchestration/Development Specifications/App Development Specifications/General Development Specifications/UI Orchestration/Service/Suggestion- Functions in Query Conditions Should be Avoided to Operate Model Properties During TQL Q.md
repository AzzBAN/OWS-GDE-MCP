---
title: "Suggestion: Functions in Query Conditions Should be Avoided to Operate Model Properties During TQL Query"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523357.html"
depth: 6
---
# Suggestion: Functions in Query Conditions Should be Avoided to Operate Model Properties During TQL Query

**Description**: The current platform does not support function indexes. If a large amount of data is queried and the model property function is used for condition filtering, the index becomes invalid and the entire table is scanned.

**Check guide**: Check whether model properties use functions in the WHERE condition in the TQL query.

**Positive example**:

select xx from table\_xx where name='_XXX_'

**Negative example**:

select xx from table\_xx where upper(name)='_XXX_'

**Exception scenario**: If the data volume of a table is small and the table is required by services, the exception scenario can be used.

**Tool supported or not**: yes

**Specification name**: General\_Service\_Disallow\_TQL\_Function\_With\_Model\_Property

**Severity**: suggestion

**Parent topic:** [[Service|Service]]