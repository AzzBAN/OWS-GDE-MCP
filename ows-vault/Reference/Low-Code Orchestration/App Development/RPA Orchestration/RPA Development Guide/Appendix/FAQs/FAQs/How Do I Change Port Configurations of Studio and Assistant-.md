---
title: "How Do I Change Port Configurations of Studio and Assistant?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001181506270.html"
depth: 7
---
#### Procedure

1.  Change the port number of the Studio recording function and the communication port number between Studio and the executor.
    
    1.  Access **AppData\\Local\\HuaweiRPA\\public\\share** in the user directory, for example, **C:\\Users\\test\\AppData\\Local\\HuaweiRPA\\public\\share**.
    2.  Open the **communicate.json** file, change the values of **debug** and **webservice** or **async\_msg** under **studio**, and save the changes.
        
        {
        	"recorder": {
        		"recorder": 58809
        	},
        	"studio": {
        		**"debug": 58054,**
        		**"webservice": 57929,**
        		**"async\_msg": 58172**
        	},
        	"assistant": {
        		"playback\_web": 58697,
        		"playback\_java": 58856,
        		"webservice": 58803,
        		"websocket": 57909
        	}
        }
        
        **Table 1** Parameter description (Studio port)  
        | Name | Description |
        | :-- | :-- |
        | recorder | Communication port for recording. If the system displays a message indicating that the port is occupied when the recording function is enabled, you can change the port number. |
        | debug | Communication port for commissioning. If a message is displayed indicating that the port is occupied when the commissioning function is enabled, you can change the port number. |
        | webservice | Communication port for Studio. If the system displays a message indicating that the webservice port is occupied after Studio is started, you can change the port number. |
        | async\_msg | Communication port for Studio. If the system displays a message indicating that the async\_msg port is occupied after Studio is started, you can change the port number. | 3.  Restart Studio to make the modifications take effect.
    
2.  Modify the configurations of the communications port between Assistant and the executor.
    
    1.  Access **AppData\\Local\\HuaweiRPA\\public\\share** in the user directory, for example, **C:\\Users\\test\\AppData\\Local\\HuaweiRPA\\public\\share**.
    2.  Open the **communicate.json** file, change the values of **playback\_web**, **playback\_java**, and **webservice** or **websocket** under **assistant**, and save the changes.
        
        {
        	"recorder": {
        		"recorder": 58809
        	},
        	"studio": {
        		"debug": 58054,
        		"webservice": 57929,
        		"async\_msg": 58172
        	},
        	"assistant": {
        		**"playback\_web": 58697,**
        		**"playback\_java": 58856,**
        		**"webservice": 58803,**
        		**"websocket": 57909**
        	}
        }
        
        **Table 2** Parameter description (Assistant port)  
        | Name | Description |
        | :-- | :-- |
        | playback\_web | Web playback communication port. If a message is displayed indicating that the port is occupied when the web playback function is enabled, you can change the port number. |
        | playback\_java | Java playback communication port. If a message is displayed indicating that the port is occupied when the Java playback function is enabled, you can change the port number. |
        | webservice | Communication port for Assistant. If the system displays a message indicating that the webservice port is occupied after Studio is started, you can change the port number. |
        | websocket | Communication port for Assistant. If the system displays a message indicating that the websocket port is occupied after Studio is started, you can change the port number. | 3.  Restart Assistant to make the modifications take effect.