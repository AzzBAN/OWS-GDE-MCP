---
title: "Rule - Batch Processing and Lightweight ETL Tasks Should Not Run in the Same Queue as BFS-Spark Aggregation and Computing Tasks"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002355408981.html"
depth: 6
---
# Rule - Batch Processing and Lightweight ETL Tasks Should Not Run in the Same Queue as BFS-Spark Aggregation and Computing Tasks

**Rule name**: General\_DataFactory\_Batch\_LightETL\_Avoid\_Co-queue\_With\_Aggregation\_Calculation

**Description**:

-   The global configuration of Spark applications cannot be unified. The global configuration of Spark applications specific to batch processing and lightweight extract, transform, and load (ETL) tasks are not applicable to BFS-Spark aggregation and computing tasks. As a result, BFS-Spark aggregation and computing tasks may fail.
-   If batch processing or lightweight ETL tasks and BFS-Spark aggregation and computing tasks co-exist in the environment, dedicated queues need to be planned and run separately.
-   Product teams need to contact the frontline Technical Management Office (TMO) or product marketing personnel to calculate the resource ratio of each queue by using the configurator.

**Check guide**: Check whether the queue used by batch processing/lightweight ETL tasks is the same as that used by BFS-Spark aggregation and computing tasks. If yes, replan queues, reconfigure the queues in the develop-state environment by referring to [Data Flow](../nottoctopics/en-us_topic_0000001299792210.html), and create the corresponding queues in the runtime-state environment. For details about how to create queues in scenarios where the cloud native storage and compute engine is deployed, see [Creating a Storage and Computing Resource Logical Queue](../nottoctopics/en-us_topic_0000001885914877.html). For details about how to create queue in other scenarios, see [Multi-Resource YARN Queue Configuration](../nottoctopics/en-us_topic_0000001189962059.html).

**Impact**: If this rule is violated, tasks may not run properly.

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]