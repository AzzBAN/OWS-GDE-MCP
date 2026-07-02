---
title: "Rule: Cache Must Be Configured for Models in Which the Read/Write Ratio Is Not Less Than 10:1 and the Number of Data Records Is Not Greater Than 1000"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363453.html"
depth: 6
---
# Rule: Cache Must Be Configured for Models in Which the Read/Write Ratio Is Not Less Than 10:1 and the Number of Data Records Is Not Greater Than 1000

**Description**: Models for saving configurations and dictionaries have small amount of data and involve query operations (including service translator scenarios) and some write operations. You are advised to configure the model cache for these models. If the read operation to write operation ratio of a model is greater than 10:1, you can configure the model cache.

**Check guide**: Go to the model page from the develop-state environment, switch to the canvas, and then open the model list. Check whether the cache function is enabled for the target models and whether these models meet the preceding requirements.

As shown in the following figure, the models with the icon shown in the red box have cache function enabled while those without the icon have the cache function disabled.

![[en-us_image_0000002157015360.png]]

**Positive example**: Configure the cache function for models that have a small number of data records (usually less than 1000 records based on the specifications of model data cache), are frequently read and seldom changed.

**Negative example**: A model cache is configured for a model that is frequently written but seldom read (for example, a log model). A cache is configured for models with a large amount of data and scattered read operations. The cache hit ratio is low and the cache effect is poor.

**Exception scenario**: The model cache does not apply to multi-model joint query or model data query using the complete TQL syntax. TQL query operations of services are included. In these scenarios, the model cache cannot be used. Model data query in the view model and the view model itself cannot use the model cache.

**Tool supported or not**: no

**Specification name**: General\_Model\_Proper\_Cache\_When\_Read\_More\_Than\_Write\_Small\_Model

**Severity**: minor

**Parent topic:** [[Model|Model]]