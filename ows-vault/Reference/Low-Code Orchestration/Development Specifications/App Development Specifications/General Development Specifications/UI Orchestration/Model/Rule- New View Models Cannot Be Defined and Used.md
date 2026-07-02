---
title: "Rule: New View Models Cannot Be Defined and Used"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804032.html"
depth: 6
---
# Rule: New View Models Cannot Be Defined and Used

**Description**: The view model is a legacy feature and can be used only in existing assets. Newly developed assets should not define new view models or use view models. The view model depends on the views of the database. The view capabilities and syntax of different databases are different. If views are used, the portability is available. The view model itself is a package of other models. When the view model is used, it is difficult to directly view the details of the model (for example, whether there is a proper index).

**Check guide**: Analyze whether the existing views can be replaced by the TQL query operation in the service or the API for querying model data through TQL. The definition of a view model cannot be directly viewed on the develop-state page. You need to export the asset package (app or project package) from the develop-state page and view the JSON file in the asset package. For details about the TQL syntax and capability scope, see _TQL Syntax and Programming Guide_.

**Tool supported or not**: no

**Specification name**: General\_Model\_Forbidden\_Use\_of\_View\_Models

**Severity**: minor

**Parent topic:** [[Model|Model]]