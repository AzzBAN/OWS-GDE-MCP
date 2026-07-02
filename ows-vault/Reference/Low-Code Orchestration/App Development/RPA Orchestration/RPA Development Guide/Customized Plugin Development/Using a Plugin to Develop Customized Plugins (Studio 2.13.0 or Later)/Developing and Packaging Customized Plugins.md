---
title: "Developing and Packaging Customized Plugins"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001224081801.html"
depth: 6
---
#### Procedure

1.  Develop the customized plugin file **action\_ext.py** to implement the corresponding function.
    
    1.  In PyCharm, open the **action\_ext.py** file for implementing the customized plugin function.
    2.  Develop customized plugin functions based on site requirements and save the settings.
        
        During development, keep the following rules:
        
        -   The entry method must start with **action\_**.
        -   During RPA built-in module import, only the **com.huawei.antrobot.actions.base** module can be imported.
        -   The instance properties provided by BaseAction can be inherited.
        -   The command entry receives defined parameter names. (By default, a parameter value of the character string type is obtained.) (For example, if the **add** command has the mandatory parameter **target** and default parameter **value**, the entry method uses the formal parameter to obtain the **action\_add(self, target, value="1"** parameter.)
        -   If the Python interpreter provided by Studio has been configured, use the UT to debug and verify specific functions. The Context and ActionOutParam classes are required for input and output parameters. After instantiation, values are assigned to **action.context** and **action.out\_param**.
        -   The following table lists the supported properties.
            
            **Table 1** Property list   
            | Property | Type | Description |
            | :-- | :-- | :-- |
            | self.logger | obj | logger object used to record logs. The log levels include info, error, warning, and debug. |
            | self.console\_logger | obj | console\_logger object used to print logs to the console in real time. The log levels include info, error, warning, and debug. |
            | self.ret\_value | obj | Returned value of a specified action property |
            | self.reference | obj | Name of the return object that references the previous action, which is used together with self.context.get\_reference |
            | self.command | str | Command name, which must be defined based on the Python method name |
            | self.params | dict | Used to obtain the corresponding parameter value in the XML file For example, self.params.get("target", ""). By default, the obtained parameters are of the string type. This parameter is not required when the formal parameter receiving function is used at the entry. |
            | self.out\_param | obj | The out\_param object has the following properties:
            -   out\_param\_name: corresponds to the **return** value of the action property.
            -   out\_param\_type: corresponds to the value of **return\_type**.
            -   out\_param\_value: The **ret\_value** value is assigned to this property through the save method based on **return\_type**.)
            
             |
            | self.context | obj | -   Value of the project directory **@**_{WORK\_DIR}_ obtained using the get\_project\_path() method
            -   Object returned by the action obtained using the get\_reference(self.reference) method
            
             | 2.  In PyCharm, select **WeAutomate** > **Action Builder** > **Configure**.
3.  Configure the basic information about the customized plugin and click **Next**.
    
    ![[en-us_image_0000001224390661.png]]
    
    **Table 2** Parameter description  
    | Name | Description |
    | :-- | :-- |
    | Plugin Name | Name of a customized plugin |
    | Version | Version number of a customized plugin |
    | Developer | Developer of a customized plugin |
    | Home Page | Home page of a customized plugin |
    | Description | Description of a customized plugin | 4.  Configure the registration information about the customized plugin and click **Next**.
    
    ![[en-us_image_0000001224152153.png]]
    
    **Table 3** Parameter description  
    | Name | Description |
    | :-- | :-- |
    | Package Name | Name of a customized plugin package |
    | File Where Control Is Located | Directory for storing the customized plugin file action\_ex.py |
    | Class Name | Class name of a customized plugin. Select a value based on site requirements. |
    | Select Control | In the list of available controls, select the required controls and click > to move them to the list of selected controls. | 5.  Configure the description and help information about the customized plugin and click **Next**.
    
    1.  In the navigation pane, choose **Extension**.
    2.  The customized plugin group information is displayed in the customized plugin list of Studio, including the Chinese name, English name, Chinese description, and English description.
        
        ![[en-us_image_0000001178596122.png]]
        
    3.  In the navigation pane, select a developed control.
    4.  Click the **Chinese Configuration** tab and configure the basic information such as parameters, input, output, and instance information of a control.
        
        ![[en-us_image_0000001224153421.png]]
        
        **Table 4** Parameter description   
        | Category | Name | Description |
        | :-- | :-- | :-- |
        | Basic Info | Display Name | Control name displayed in Studio |
        | Control Help | Detailed help information of a control |
        | Parameter | Parameter | Name of a parameter in the control |
        | Type | Type of a parameter in the control, which is display in Studio
        -   **number**: The value is displayed in a text box in Studio and can contain only digits.
        -   **string**: The value is displayed as a text box in Studio. There is no restriction on the input.
        -   **password**: The password is displayed in the password text box in Studio to mask the input information.
        -   **list**: This parameter is displayed in the drop-down list box in Studio. It is often used together with the **Value Range** parameter to check whether the input value is within the value range.
        -   **file**: The value is displayed as a file selection box in Studio.
        -   **dir**: The value is displayed as a folder selection box in Studio.
        
         |
        | Display Name | Display name of a parameter You can view the display name of a parameter next to the parameter name only when Parameter Name Is Visible is enabled on the Settings page of Studio. The actual effect is as follows: |
        | Mandatory | Whether a parameter is mandatory
        
        -   **true**: Yes
        -   **false**: No
        
         |
        | Default Value | Default value of a parameter |
        | Value Range | Value range of a parameter Multiple values are separated by vertical bars (|), for example, 123|456|789. |
        | Description | Description of a parameter |
        | Validation expression | Expression for verifying parameters Multiple expressions are separated by commas (,). Select a parameter and click to set it. The following verification expressions are supported:
        
        -   **ip**: IP address, for example, ip
        -   **min/max**: Value range For example, min=1,max=7200
        -   **min\_len/max\_len**: Length range of the character string. The default maximum length is 65535. For example, min\_len=4.
        -   **host**: Domain name, for example, host
        -   **excludes**: Special characters that cannot be contained. For example, excludes=\*\\/? \*\[\]\*
        -   **email\_address**: Email address, for example, email\_address
        -   **file\_suffix**: Supported file name extension, for example, file\_suffix=xlsx|xlsm|xls|xlsb
        -   **int**: Integer, for example, int
        
         |
        | Dependency Parameter | Dependency parameter of a parameter It is used by Studio to display dependency parameters. For example, the pid parameter of killProcess is available only when option is set to pid. In this case, you need to set the dependency parameter option==...pid for pid. |
        | Input | Parameter | Input parameter name of a control |
        | Display Name | Display name of the input parameter of a control |
        | Description | Description of the input parameter of a control |
        | Output | Parameter | Output parameter name of a control |
        | Type | Output parameter type of a control |
        | Display Name | Display name of the output parameter of a control |
        | Default Value | Default value of the output parameter of a control |
        | Description | Description of the output parameter of a control |
        | Instance | Description | Description of a control instance |
        | Sample Code | Sample code of a control instance | 5.  Click the **English Configuration** tab and configure the basic information such as parameters, input, output, and instance information of a control.
    6.  In the navigation pane, select other developed controls and repeat [5.d](#EN-US_TOPIC_0000001224081801__li219174325711) to [5.e](#EN-US_TOPIC_0000001224081801__li1355058205814) to configure the basic information such as parameters, input, output, and instances of a control.
    
6.  Configure the dependency information of the customized plugin and click **Save**.
    
    1.  Go to the directory where the _pip.ini_ file is located.
    2.  Modify **trusted-host** and **index-url** in the **pip.ini** file to specify the image source address for downloading dependent third-party components and save the settings.
        
        \[global\]
        trusted-host=cmc-cd-mirror.rnd.huawei.com
        index-url=http://cmc-cd-mirror.rnd.huawei.com/pypi/simple/
        
    3.  Go back to PyCharm, and configure the dependency information of the customized plugin.
        
        ![[en-us_image_0000001224249363.png]]
        
        **Table 5** Parameter description  
        | Name | Description |
        | :-- | :-- |
        | Dependency Management Mode | Management mode of a Python third-party component on which the customized plugin depends
        -   Generate the dependency list only: Generate only the **requirements.txt** file in the project directory. You need to create the **lib** directory in the project directory and place the dependent third-party .whl package in the **lib** directory based on **requirements.txt**.
        -   Automatically archive dependencies to **pylib**: Automatically download the dependent third-party files based on the configured **pip.ini** file and package the files into the project package.
        
         |
        | Clear the existing dependencies in pylib. | Whether to clear the existing dependency files in the pylib directory before automatic archiving |
        | Dependency List | List of third-party components on which customized plugin depends Click + on the right and enter the dependency package name and version. | 7.  Package the customized plugin project file.
    
    1.  On the **Dependency Settings** page of **WeAutomate Action Builder**, click **Export**.
    2.  In the displayed dialog box, select the following files to be exported and click **OK**.
        
        ![[en-us_image_0000001224411303.png]]
        
    3.  Select a directory for storing customized plugin project packages and click **OK**.