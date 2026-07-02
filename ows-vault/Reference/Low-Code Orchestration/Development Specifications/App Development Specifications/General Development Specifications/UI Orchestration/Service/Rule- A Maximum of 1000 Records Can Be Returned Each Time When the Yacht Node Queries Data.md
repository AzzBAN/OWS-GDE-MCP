---
title: "Rule: A Maximum of 1000 Records Can Be Returned Each Time When the Yacht Node Queries Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804040.html"
depth: 6
---
# Rule: A Maximum of 1000 Records Can Be Returned Each Time When the Yacht Node Queries Data

**Description**: The yacht node can connect to the big data platform to query data. Therefore, the amount of returned data needs to be limited to prevent the client from receiving a large amount of data, which occupies the memory and causes OOM.

**Check guide**: Check whether the limitation is explicitly specified in the query SQL statement to limit the amount of data to be returned.

**Positive example**: select \* from #table where name = $name and age > $age limit 1000

**Negative example**: select \* from #table where name = $name and age > $age

**Tool supported or not**: no

**Specification name**: General\_Service\_Start\_Value\_Cannot\_Exceed\_10000

**Severity**: minor

**Parent topic:** [[Service|Service]]