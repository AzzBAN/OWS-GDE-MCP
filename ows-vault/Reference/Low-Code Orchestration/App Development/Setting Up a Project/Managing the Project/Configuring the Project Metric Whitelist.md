---
title: "Configuring the Project Metric Whitelist"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_054.html"
depth: 4
---
#### Context

During app running, app metrics need to be developed to facilitate monitoring and maintenance of app operations. After app metrics are reported to GDE management zone, maintenance and management personnel can learn about the app running status.

Metrics of counter and gauge types can be reported. Only metrics of the gauge type can be viewed on the WebUI of the GDE management zone. Metrics of the counter type are not displayed.

To implement the metric reporting capability, you need to perform the following operations:

-   Define metrics using the Monitor method in a script. The Monitor function supports script engines of V1.5, V1.6, and the latest version. After historical assets are imported, you can define metrics based on historical assets.
    
    **Table 1** Monitor functions   
    | API | Description | Example |
    | :-- | :-- | :-- |
    | Monitor.gauge(metricName,metricValue\[,labels\]) | Used to report gauge metrics. When this function is used to report metrics, the tenant\_id and current\_app parameters are contained by default. That is, you do not need to specify the tenant and current app information.
    -   **metricName**: name of the reported metric. To avoid conflicts between metric names and existing metric names in the system, the reported metric names always start with **app\_gauge\_**, for example, **app\_gauge\_user\_counts**.
    -   **metricValue**: reported metric value. The value must be of the Double type.
    -   **labels**: Optional. The value is of the Object type. The key is the label name, and the value is the label.
    
    The return value is of the Boolean type.
    
    -   **true**: Reporting succeeded.
    -   **false**: Reporting failed.
    -   **exception**: An exception occurs.
    
     | -   Example without a label:
        
        var res =Monitor.gauge("app\_gauge\_user\_counts",12000)
        return {"result":res}
        
    -   Example with a label:
        
        var gauge\_with\_label = Monitor.gauge("app\_gauge\_test",5.1,{"a":"a","b":"b"})
        return {"gauge\_with\_label":gauge\_with\_label}
        
    
     |
    | Monitor.counter(metricName,metricValue\[,labels\]) | Used to report counter metrics. When this function is used to report metrics, the tenant\_id and current\_app parameters are contained by default. That is, you do not need to specify the tenant and current app information.
    
    -   **metricName**: name of the reported metric. To avoid conflicts between metric names and existing metric names in the system, the reported metric names always start with **app\_counter\_**, for example, **app\_counter\_user\_counts**.
    -   **metricValue**: reported metric value.
    -   **labels**: Optional. The value is of the Object type. The key is the label name, and the value is the label.
    
    The return value is of the Boolean type.
    
    -   **true**: Reporting succeeded.
    -   **false**: Reporting failed.
    -   **exception**: An exception occurs.
    
     | -   Example without a label:
        
        var res =Monitor.counter("app\_counter\_user\_counts",12000)
        return {"result":res}
        
    -   Example with a label:
        
        var counter\_with\_label = Monitor.counter("app\_counter\_test",2,{"a":"a","b":"b","c":"c"})
        return {"counter\_with\_label":counter\_with\_label}
        
    
     | -   Configure a metric whitelist. Only the metrics defined in the project metric whitelist can be reported. A maximum of 50 metrics can be configured for each project.

In addition, in the OC scenario, the **master** user can configure the metric whitelist function on the **Products and Services** > **ADC System Management** > **Component Management** > **System Parameter Configuration** page displayed under the **master** tenant. This function can be enabled only for specified tenants.

**Table 2** System parameters    
| Category | Name | Value | Default Value |
| :-- | :-- | :-- | :-- |
| adc-service | app\_monitor\_enable | Whether the metric reporting capability is enabled for all tenants
-   **true**: The project metric reporting capability is enabled for all tenants.
-   **false**: The project metric reporting capability is not enabled for all tenants.

 | true |
| adc-service | app\_monitor\_tenant\_whitelist | Whitelist of tenants for whom the metric reporting capability is enabled If app\_monitor\_enable is set to false, the function is enabled for specified tenants using a whitelist. Example: 1002,1003 | N/A |