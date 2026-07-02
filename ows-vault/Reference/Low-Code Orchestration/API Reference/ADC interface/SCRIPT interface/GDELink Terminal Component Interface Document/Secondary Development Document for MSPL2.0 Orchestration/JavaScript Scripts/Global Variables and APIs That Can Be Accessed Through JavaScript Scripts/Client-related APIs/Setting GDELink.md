---
title: "Setting GDELink"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001457117589.html"
depth: 9
---
#### U.setViewConfig(params, callback)

Used to allow users to set the client display configuration, for example, whether to allow screenshot.

![[notice_3.0-en-us.png]]

Android and Harmony versions are supported.

 
| Parameter | Type |
| :-- | :-- |
| params | Object |
| callback | Function | 
| Parameter | Value | Description |
| :-- | :-- | :-- |
| key | allow\_screenshot | Whether screenshot is supported. This parameter applies to the current light app. |
| value | true/false | \- | Example:

U.setViewConfig({
 key: "allow\_screenshot",
 value: true
})