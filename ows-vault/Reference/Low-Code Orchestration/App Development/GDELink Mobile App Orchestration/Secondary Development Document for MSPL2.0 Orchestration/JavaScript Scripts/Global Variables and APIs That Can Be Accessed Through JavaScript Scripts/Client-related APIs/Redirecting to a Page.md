---
title: "Redirecting to a Page"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406637624.html"
depth: 7
---
#### U.startIntent(scheme, page, paramJson)

Used to open a plugin or third-party app.

![[notice_3.0-en-us.png]]

Only the Android version is supported.

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| scheme | String | Plugin or third-party app package name |
| page | String | Plugin or third-party app startup class |
| paramJson | Object | Plugin or third-party app startup parameter | Example:

U.startIntent("xxx.xxx.gdelink","xxx.xxx.gdelink.activity.home.StartPageActivity", {"gdelinkType": "plugin"})