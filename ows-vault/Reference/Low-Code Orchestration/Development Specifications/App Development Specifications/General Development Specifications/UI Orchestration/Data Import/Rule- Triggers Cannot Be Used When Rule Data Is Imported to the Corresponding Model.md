---
title: "Rule: Triggers Cannot Be Used When Rule Data Is Imported to the Corresponding Model"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403841.html"
depth: 6
---
# Rule: Triggers Cannot Be Used When Rule Data Is Imported to the Corresponding Model

**Description**: If a trigger is enabled for the target model during data import, the following performance problems may occur:

1.  The import duration increases significantly, affecting user experience. If the trigger contains time-consuming operations, the import duration is further prolonged.
2.  When the trigger is configured to be executed asynchronously, the following problems may occur:
    -   The asynchronous execution thread is blocked.
    -   Service functions are abnormal.

**Check guide**: Check whether a trigger is configured for the model corresponding to the service associated with data import.

**Tool supported or not**: no

**Specification name**: General\_Import\_Forbidden\_Trigger\_Used\_in\_The\_Model

**Severity**: minor

**Parent topic:** [[Data Import|Data Import]]