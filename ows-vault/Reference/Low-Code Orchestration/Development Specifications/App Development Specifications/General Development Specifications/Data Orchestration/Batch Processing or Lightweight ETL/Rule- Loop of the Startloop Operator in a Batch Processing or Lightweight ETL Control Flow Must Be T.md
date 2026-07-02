---
title: "Rule: Loop of the Startloop Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Terminable"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001192464718.html"
depth: 6
---
# Rule: Loop of the Startloop Operator in a Batch Processing or Lightweight ETL Control Flow Must Be Terminable

**Specification name**: General\_DataFactory\_Batch\_LightETL\_StartLoop\_Loop\_Must\_End

**Description**:

-   At least one node in the loop is configured with a loop exit. The expression configured on the line between the node and the loop exit must be valid in some cases.
-   If two or more nodes are connected to the loop entrance, ensure that lines between these nodes and the loop entrance are configured with mutually exclusive judgment conditions.

**Positive example**:

When the value of the output **flow.var** of the Calculate operator is greater than 10, the Calculate and Empty operators are executed; when the value is 10, the Indicator Audit operator is executed.

-   The expression on the line between Startloop and Indicator Audit is **#flow.var#<=10**.
-   The expression on the line between Startloop and Calculate is **#flow.var#>10**.

**Check guide**: Check the expression on the line connected to the out port of the Startloop operator in the loop. The expression must be valid in some cases.

**Impact**: If the loop of the Startloop operator in the batch processing and lightweight ETL control flow cannot be ended, the program will enter an infinite loop, causing serious issues, such as program execution errors and system resource exhaustion.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]