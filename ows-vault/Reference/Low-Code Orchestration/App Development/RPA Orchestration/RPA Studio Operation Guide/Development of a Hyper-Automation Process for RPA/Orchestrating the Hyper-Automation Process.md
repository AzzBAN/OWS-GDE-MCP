---
title: "Orchestrating the Hyper-Automation Process"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_studio_dev_rpa_0009.html"
depth: 5
---
#### Procedure

1.  On the project list page, click the created **HyperAutoProcess** project.
2.  Create a hyper-automation process.
    
    1.  In the navigation pane, choose **Business Process**.
    2.  On the displayed **Business Process** tab page, click ![[en-us_image_0000001599803686.png]] in the upper right corner.
    3.  Set the parameters related to the hyper-automation process.
        
        ![[en-us_image_0000002210407360.png]]
        
        The parameters are described as follows:
        
        -   **Process Type**: Set this parameter to **Non-auto process**.
        -   **Business type**: Set this parameter to **Hyperautomation**.
        -   **Process Template**: Select **Basic Process Template for Quick Start**.
        -   Set other parameters based on site requirements.
    4.  Click **Submit**.
    
3.  Adjust the nodes of the hyper-automation process based on the service scenario requirements.
    
    1.  Go to the process canvas page and click **Enter Editing Mode**.
    2.  Click the **Calculating prime** node and click ![[en-us_image_0000001599781522.png]] on the toolbar of the canvas to delete unnecessary process nodes.
    3.  Click the **Displaying results** node and click ![[en-us_image_0000001649144153.png]] on the toolbar of the canvas to delete unnecessary process nodes.
    4.  In the component list under **Components** > **Activity** on the left, drag **RPA Task** to the canvas and connect it to the **Enter query scope** and **End Event** nodes.
        
        ![[en-us_image_0000001649061085.png]]
        
    
4.  Configure the form page for the manual task node.
    
    1.  Click the **Enter query scope** node. On the **Primary Property** tab page on the right, configure the node properties.
        
        ![[en-us_image_0000002210410740.png]]
        
    2.  Click the **Input City and Days** node again and choose **User Task** > **Form** to access the process form page designer.
        
        ![[en-us_image_0000002245492297.png]]
        
    3.  In the page designer, right-click the **Please enter the starting number** component and select **Delete** from the shortcut menu to delete unnecessary page component.
    4.  In the component list under **Components** > **Data Field** on the left, drag **Text Input** to the canvas and place it above the **Please enter an end value** component.
        
        ![[en-us_image_0000002210590498.png]]
        
    5.  Click the **Text Input** component. On the **Properties** tab page on the right, configure information about the component based on the actual service scenario.
        
        ![[en-us_image_0000001649281821.png]]
        
    6.  Click the **Please enter an end value** component. On the **Properties** tab page on the right, configure information about the component based on the actual service scenario.
        
        ![[en-us_image_0000002041367125.png]]
        
    7.  Click ![[en-us_image_0000001649264213.png]] in the upper part of the canvas to save the configuration of the hyper-automation process form page.
    
5.  Configure the RPA task node.
    
    1.  Return to the process canvas page and click the **RPA Task** node.
    2.  On the **Primary Property** tab page on the right, click **RPA Task Parameters**.
    3.  In the **RPA Task Parameters** dialog box, configure the basic information and parameters of the task.
        
        ![[en-us_image_0000002210436794.png]]
        
        **Table 1** Parameter description   
        | Parameter | Description | Configuration Example |
        | :-- | :-- | :-- |
        | Basic Info |
        | Script | Robot script used during robot task execution | Weather information collection robot |
        | Procedure Version Match Type | Mode of matching robot scripts during robot task execution
        -   **Specified Version**: Only the robot scripts of the specified version are executed in the robot task.
        -   **Always Latest**: Only the robot scripts of the latest version are executed in the robot task.
        
         | Specified Version |
        | Script Version | Version of the robot scripts used during robot task execution This parameter is displayed only when Procedure Version Match Type is set to Specified Version. | 1.0.6 |
        | Running Mode | Available client types that are found by the system during robot task execution
        
        -   **Executor**: An available executor is used in a robot task to execute the robot scripts. Rules for determining the executor availability are as follows: whether the executor is public, whether the OS of the executor matches that of the system that the script applies to, and whether the executor is online.
        -   **Cluster**: An available cluster is used in a robot task to execute the robot scripts. Rules for determining the cluster availability are as follows: whether the cluster is public, whether the OS of the cluster matches that of the system that the script applies to, and whether an available executor exists in the cluster.
        
         | Executor |
        | Preferential Search | Name of the agent that is preferentially searched for during robot task execution
        
        -   **Running Mode** is set to **Executor**: When searching for available executors, the system preferentially selects the executor whose name matches the value of this parameter.
        -   **Running Mode** is set to **Cluster**: When searching for available clusters, the system preferentially selects the cluster whose name matches the value of this parameter.
        
        To reference a parameter in the process form, click and select the parameter. If the required parameter cannot be selected, enter the JSON path of the parameter to be referenced and enclose the path with $(). | test |
        | Timeout (min) | Timeout interval for executing a robot job. The default value is 120. If the timeout interval is not limited, set this parameter to -1. To reference a parameter in the process form, click and select the parameter. If the required parameter cannot be selected, enter the JSON path of the parameter to be referenced and enclose the path with $(). | 120 |
        | Longest Waiting Time (min) | Maximum waiting time during the robot task execution. The default value is 30. If the maximum waiting time is not limited, set this parameter to -1. If the task execution wait time exceeds the value of this parameter, the task execution times out and fails. To reference a parameter in the process form, click and select the parameter. If the required parameter cannot be selected, enter the JSON path of the parameter to be referenced and enclose the path with $(). | 30 |
        | Parameter Settings |
        | Name | Name of the parameter required for executing a robot task | City |
        | Type | Type of the parameter required for executing a robot task
        
        -   **Reference**: The parameters required by the task reference other parameters in the context.
        -   Other types except **Reference**: Actual data type of the parameter required by the task.
        
         | Reference |
        | Value | Value of the parameter required for executing a robot task
        
        -   When **Type** is set to **Reference**, you can set this parameter based on site requirements.
            -   To directly reference parameters such as **City** and **Days**, click ![[en-us_image_0000001650560857.png]] and select the parameter to be referenced.
            -   To reference sub-parameters of the **City** or **Days** parameter, enter the JSON path of the referenced parameter in the "$()" format, for example, **$(\_context.weather\_city.nanjing)**.NOTICE: When the ProcessTask and ConfirmTask phases have the same parameter A, because the context parameter will be overwritten during process running, the RPA Task node actually obtains the value of parameter A in the ConfirmTask phase even if the referenced parameter is parameter A in the ProcessTask phase.
        -   If **Type** is set to a value other than **Reference**, enter the parameter value.
        
         | $(\_context.weather\_city) | 4.  Click **Submit** to complete the robot task parameter configuration.
    5.  On the **Primary Property** and **More Properties** tab pages, configure other properties of the **RPA Task** node.
        
        ![[en-us_image_0000002210439246.png]]
        
    6.  Click ![[en-us_image_0000001649161605.png]] in the upper part of the canvas to save the configuration of the hyper-automation process.