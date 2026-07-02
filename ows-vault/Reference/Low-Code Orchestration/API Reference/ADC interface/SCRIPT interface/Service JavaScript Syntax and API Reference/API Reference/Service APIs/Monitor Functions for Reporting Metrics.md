---
title: "Monitor Functions for Reporting Metrics"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_034.html"
depth: 7
---
# Monitor Functions for Reporting Metrics

To report a metric, you need to define the metric in the script and add the metric to the metric whitelist in the project.

The Monitor functions support script engines of 1.5, 1.6, and the latest version. After historical assets are imported, you can define metrics based on those historical assets.

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
    

 | **Parent topic:** [[Service APIs|Service APIs]]