---
title: "Interface Logs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_057.html"
depth: 8
---
#### Procedure

1.  Choose **API-Level Policy** > **API Log** > **Log Policy**.
2.  Set **Log Type** to **Interface Log**.
3.  Configure interface logs.
    
    Select the range of interface logs to be recorded based on site requirements. The values of **Printing Scope** and **Log Level** of the interface logs to be printed are described as follows.
    
     
    | Parameter | Description |
    | :-- | :-- |
    | Printing Scope | 
    -   **Receiver and sender** All logs generated when the API Fabric functions as the client and server are printed.
    -   **Receiver** All logs generated when the API Fabric functions as the server are printed.
    -   **Sender** All logs generated when the API Fabric functions as the client are printed.
    -   **None** No log is printed.
    
     |
    | Log Level | NOTE: If this parameter is set to INFO or ERROR, you need to configure sensitive log policies in develop state. For details, see API Log Desensitization.
    
    -   **INFO** All request and response packets are printed. The following is a log example:
        
        2023-03-21 17:03:53,989|INFO|apiaccess|DefaultSpace|1638104128372604928||1||REST|Endpoint\_WeatherService||127.0.0.1|https://127.0.0.1:8081/weather/getWeatherByCityId/undefined|get|/getWeatherByCityId/{cityId}|**200**|159|||{"**request**":{"headers":{"x-sandbox-jaggerid":"1638104128372604928","x-sandbox-dialtest":"true","accept-encoding":"gzip, x-gzip, deflate","host":"127.0.0.1:8081","connection":"keep-alive","user-agent":"APIFabric","content-length":"0","content-type":"application/json;charset=UTF-8","date":"Tuesday, March 21, 2023 09:03:53 GMT","x-forwarded-for":"127.0.0.1,127.0.0.1"},"body":}, "**response**":{"headers":{"Content-Type":"text/plain;charset=UTF-8","Keep-Alive":"timeout=60"},"body":"Sunny"}}
        
    -   **ERROR** Only the request and response packets sent when the calling fails are printed. The following is a log example:
        
        2023-03-20 16:02:09,843|ERROR|apiaccess|DefaultSpace|1637726043114569728||1||REST|Endpoint\_WeatherService||127.0.0.1|https://127.0.0.1:8081/weather/getWeatherByCityId/undefined|get|/getWeatherByCityId/{cityId}|**500**|15359|||{"**request**":{"headers":{"x-sandbox-jaggerid":"1637726043114569728","x-sandbox-dialtest":"true","accept-encoding":"gzip, x-gzip, deflate","host":"127.0.0.1:8081","connection":"keep-alive","user-agent":"APIFabric","content-length":"0","content-type":"application/json;charset=UTF-8","date":"Monday, March 20, 2023 08:01:43 GMT","authorization":"\*\*\*\*\*\* ","x-forwarded-for":"127.0.0.1,127.0.0.1","X-APP-Key":"\*\*\*\*\*\*"},"body":}, "**response**":{"headers":{},"body":"49401024991:can not make connection to service"}}
        
    -   **No packet** No packet is printed.
    
     | 4.  Click **Save**.