---
title: "Rule: Data Records Must Be Imported in Batches If the Quantity Exceeds 100,000"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399643345.html"
depth: 6
---
# Rule: Data Records Must Be Imported in Batches If the Quantity Exceeds 100,000

**Description**: If more than 100,000 data records need to be imported, import them in batches. Importing a single data record is to submit a transaction, which consumes time and occupies database resources for a long time.

**Check guide**: Check whether the import service uses batch submission and whether the corresponding service receives arrays for batch submission.

The service corresponding to data import can receive arrays. Generally, the model operations corresponding to the service are batch supplement or creation. Note that if the model already exists during batch creation, an error is reported. If the model already exists during supplement, the model is updated.

**Positive example**: Batch import is configured for device models in CMDB. Note that the batch import service may not be automatically generated on the model generation service and page. You need to manually create the service.

The following figure shows a data import example.

![[en-us_image_0000001520244937.png]]

**Negative example**: A single Create operation or a self-written script is used to create and update data.

**Tool supported or not**: no

**Specification name**: General\_Import\_Use\_Batch\_Import\_to\_Import\_Large\_Amount\_of\_Data

**Severity**: minor

**Parent topic:** [[Data Import|Data Import]]