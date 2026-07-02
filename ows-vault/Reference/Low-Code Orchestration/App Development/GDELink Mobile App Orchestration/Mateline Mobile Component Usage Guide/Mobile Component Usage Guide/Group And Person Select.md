---
title: "Group And Person Select"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001734920318.html"
depth: 5
---
# Group And Person Select

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| GroupSearchServiceID | Used to query the services of the group that the current user belongs to. The default service is the system service get\_roles\_by\_username. The services are filtered by member\_name. |
| Label | Component label |
| Name | Component name |
| SubmitType | Whether to combine the values obtained by the getValue component. The options are separated and combined. If separated is selected, the value in the format of "select={"groups":\["Administrator","StudioDeveloper"\],"users":\["testuser8m97gk","testuserarq9mb"\]}". If combined is selected, the value is in the format of "user:200237;user:200141;group:1;group:3;". |
| UserSearchServiceID | Service for querying group members. The default value is the system service get\_role\_members\_by\_rolename, which is filtered by role\_id. |
| Required | Whether the component is mandatory | **APIs**

**getValue**

Input parameters: none

Output parameters: String

Description: Obtain the value.

C("compId").getValue();

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]