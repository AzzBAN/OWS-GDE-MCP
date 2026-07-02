---
title: "Rule: Query Performance Must Be Fully Evaluated and Tested When the Associated Query Is Used for a Large Number of Models (More Than 100,000)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208200313.html"
depth: 6
---
# Rule: Query Performance Must Be Fully Evaluated and Tested When the Associated Query Is Used for a Large Number of Models (More Than 100,000)

**Description**: When the associated query is performed on a model with a large amount of data, the number of records in the result set increases sharply if the associated conditions or query conditions are not properly designed because the data base is large (for example, 100,000). In this way, the performance is greatly affected. For multi-model association query or single-model self-association query, the performance of a specific query must be fully evaluated and tested. Evaluate the number of associated models and the model data volume at least. It is recommended that the data volume of a single model be less than 100,000 when two models are associated and less than 10,000 when three models are associated.

Note that in addition to APIs such as TQL query operations of services and TQL query provided by models, view models can also use the association query. Therefore, this rule must be kept when association query is used in these scenarios.

**Check guide**: On the develop-state page, check the TQL query operations of the service and the model data TQL query script called in each execution script. If multi-model association query is involved and the model data volume is large, perform necessary analysis and test based on the preceding description. The definition of a view model cannot be directly viewed on the develop-state page. You need to export the asset package (app or project package) from the develop-state page and view the JSON file in the asset package.

**Negative example**: The performance of the multi-model associated query scenario with a large amount of data is not evaluated or tested.

**Tool supported or not**: no

**Specification name**: General\_Model\_Full\_Test\_When\_Query\_Within\_Huge\_Models

**Severity**: major

**Parent topic:** [[Model|Model]]