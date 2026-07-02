---
title: "Rule: Archiving Policy Must Be Configured for Models with Increasing Rule Data Volume and Expected to Exceed 1 Million Rows"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001349283564.html"
depth: 6
---
# Rule: Archiving Policy Must Be Configured for Models with Increasing Rule Data Volume and Expected to Exceed 1 Million Rows

**Description**: As the model data volume increases, the performance of adding, deleting, modifying, and querying model data deteriorates. Therefore, a proper data clearing mechanism must be used to prevent the model data volume from being too large (controlled at a maximum of 1 million rows). You can configure proper archiving policies or use the data clearing mechanism of the service to clear data. Models that require archiving policies include tickets, alarms, and logs.

**Check guide**: Log in to the develop-state environment and go to the model details page. On the **Archive Configuration** tab page, check whether a proper archiving policy has been configured.

**Positive example**: If the data volume of a service model keeps increasing, an archiving policy is configured for the model, or the service has a data clearing mechanism to ensure that the data volume of the model is within a proper range.

**Negative example**: If the data volume of a service model keeps increasing but no model archiving policy is configured and the service does not have the corresponding data clearing mechanism, the data operation performance of the model decreases as the data volume of the model increases.

**Exception scenario**: If no archiving policy is available and the service has the corresponding data clearing mechanism, you do not need to configure an archiving policy for the model.

**Tool supported or not**: yes

**Specification name**: General\_Model\_Proper\_Archive\_Rule

**Severity**: major

**Parent topic:** [[Model|Model]]