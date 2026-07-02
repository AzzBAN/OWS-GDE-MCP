---
title: "Reading Local Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406634132.html"
depth: 9
---
#### U.readLocalData(key) ⇒ String

Used to obtain information stored on the client.

 
| Parameter | Type |
| :-- | :-- |
| key | String | Example of the key values:

  
| key | Description | Example of the Returned Value |
| :-- | :-- | :-- |
| username | Obtained user name | default\_test1 |
| user\_id | User ID | 1614741307991024709 |
| tenant\_id | Tenant ID | 2000 |
| appBaseDir | Root path for storing apps | /storage/.../appstore |
| screenResolution | Screen resolution | 1080\*2179 |
| sdk | SDK version of the device | 29 |
| statusBarHeight | Height of the status bar | 132 |
| utc | Current UTC time | 1614995248006 |
| now | Current time | 2021-03-06 09:47:36 |
| localtime | Local time | 2021-03-06 09:47:36 |
| locale | Current internationalization | en\_US |
| timezone | Time zone | GMT+08:00 |
| authorization | Login authorization using the token | \- |
| UUID | Generated UUID | 1107bcd7b61c4ada84e2d036b37b69fe |
| home\_page | Whether the tab is on the home page | false |
| imagePath | Obtained photo path | file:///storage/.../images |
| roles | User role list | \- |
| env.url | URL for obtaining the environment configuration on the mobile phone | \- | Example:

let result = U.readLocalData("username");