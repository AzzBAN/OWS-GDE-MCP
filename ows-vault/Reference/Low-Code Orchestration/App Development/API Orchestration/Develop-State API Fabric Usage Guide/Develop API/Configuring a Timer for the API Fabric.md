---
title: "Configuring a Timer for the API Fabric"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_146.html"
depth: 5
---
#### Procedure

1.  Select **Inbound API** or **Outbound API** as required and click **Develop API**.
2.  On the **Develop API** page, choose **More** > **Timer Management**.
    
    ![[en-us_image_0000001573331850.png]]
    
3.  On the **Timer Management** page, click **Create**. Set parameters based on site requirements. The following table describes the parameters.
    
    **Table 1** Parameters for configuring a timer  
    | Parameter | Description |
    | :-- | :-- |
    | Name | User-defined timer name. |
    | Type | Timer type. Currently, only repeat is supported. |
    | Execution period | Execution period of the timer. For example, if Execution period is set to 1000 and Duration Unit is set to Milliseconds, the timer is executed for the second time 1000 ms after the first execution ends, and so on until the number of repetition times is met. |
    | Repetition Times | Number of repetition times of the timer. For example, if this parameter is set to 4, after the first execution is complete, the timer is executed for the second time 1000 ms later, and so on. When the timer is executed for four times, the timer stops triggering the third-party orchestration process. NOTE: If this parameter is set to 0, the timer triggers the third-party orchestration process for unlimited times until you manually cancel the release of the timer. |
    | Description | Description of a user-defined timer. | 4.  Click **Confirm**.
5.  On the **Timer** page, click the timer name. The timer process orchestration page is displayed.
    
    For details about process orchestration, see [[Orchestration|Orchestration]]. The timer process orchestration is different from the API process orchestration. For example, when a user clicks a diagram element, only the service to be called can be configured, and no request parameter is required.
    
    The timer process is orchestrated by a third party and is configured by users. The message returned during calling is also processed by users.
    
6.  After the orchestration is complete, click **Save**.
    
    You can modify or delete a configured timer on the **Timer** page.
    
7.  After the timer is configured, select the timer to be exported and click **Export**.