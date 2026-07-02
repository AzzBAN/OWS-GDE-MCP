---
title: "Suggestion: Frontend Access to Metadata and Data Are Prohibited for Orchestration Models"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963832.html"
depth: 5
---
# Suggestion: Frontend Access to Metadata and Data Are Prohibited for Orchestration Models

**Description**: The GDE develop-state environment provides the function of whether to allow frontend access for orchestration models. Developers can determine whether to open the metadata and data access capabilities of related orchestration models to the frontend through configuration.

Metadata is the definition of a model. The corresponding frontend access capability allows frontend page controls, for example, TQL controls, to select this model.

Data refers to the storage data of a model. The corresponding frontend access capability allows frontend page controls to access data of the model. For example, the drop-down list component can obtain data from the model.

**Check guide**:

1.  Log in to the develop-state environment, select a desired project, choose **Model** from the menu on the left, select an existing model, and click **Edit** in the **Operation** column.
2.  In the displayed dialog box, check whether **Metadata can be accessed by the frontend** and **Data can be accessed by the frontend** are disabled. They are disabled by default.
    
    ![[en-us_image_0000001521810381.png]]
    

**Positive example**:

During model creation, **Metadata can be accessed by the frontend** and **Data can be accessed by the frontend** are disabled.

![[en-us_image_0000001522006157.png]]

**Tool supported or not**: yes

**Specification name**: Security\_AccessControl\_Data\_Frontend

**Category**: non-bottom-line check item

**Severity**: suggestion

**Orchestration scenario**: general job orchestration

**Parent topic:** [[Access Control|Access Control]]