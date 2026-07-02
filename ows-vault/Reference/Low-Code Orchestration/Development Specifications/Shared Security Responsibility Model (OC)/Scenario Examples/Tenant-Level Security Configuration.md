---
title: "Tenant-Level Security Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001151289465.html"
depth: 4
---
# Tenant-Level Security Configuration

1.  GDE allows the tenant administrator to manage tenant-level accounts based on the actual status of users in the organization to which the tenant belongs.

Scenario 1: An employee in the organization to which the tenant belongs is transferred, but the permission is not cleared. The employee logs in to GDE to download sensitive data one day after the transfer, leading to data leakage.

The tenant takes the responsibility. GDE has provided the account and permission control capability. The tenant administrator should revoke the permissions of the employee immediately after the employee leaves the current position (including but not limited to freezing the account, canceling the access permission, and deleting the account).

Scenario 2: The tenant administrator deletes the account of a resigned employee. One month later, a new employee (with the same name but not the same person) comes. After the administrator creates an account for the employee, the account inherits the permissions of the previous employee.

GDE takes the full responsibility for data leakage caused by account permission inheritance.

**Parent topic:** [[Scenario Examples|Scenario Examples]]