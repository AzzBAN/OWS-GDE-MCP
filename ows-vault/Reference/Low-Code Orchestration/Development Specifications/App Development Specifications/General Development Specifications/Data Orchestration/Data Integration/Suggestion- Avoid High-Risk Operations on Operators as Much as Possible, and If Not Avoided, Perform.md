---
title: "Suggestion: Avoid High-Risk Operations on Operators as Much as Possible, and If Not Avoided, Perform Them After Confirming that There Are No Risks"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001653873197.html"
depth: 6
---
# Suggestion: Avoid High-Risk Operations on Operators as Much as Possible, and If Not Avoided, Perform Them After Confirming that There Are No Risks

**Specification name**: General\_DataFactory\_AIP\_Avoiding\_Risk\_Operation

**Description**: Avoid high-risk operations on operators as much as possible. If high-risk operations are necessary, perform the operations after confirming that there are no risks.

**Check guide**:

-   Do not use the Database operator to perform operations on sensitive data tables, such as permission tables and user information tables. The operations include but are not limited to data insertion, deletion, and update.
-   When using the Database operator to perform operations on table data, do not perform operations on the entire table without adding conditions, such as using **delete from tablename;**
-   Do not use high-risk shell commands, such as kill, su, sudo, reboot, chown, and export, during the configuration of the SSH operator.
-   Do not select the **Change HDFS file or path permission**, **Delete directory**, and **Delete file** operations during the configuration of the HDFS operator.
-   Do not select the **Delete** operation for remote files during the configuration of the SFTP operator.

**Parent topic:** [[Data Integration|Data Integration]]