---
title: "Receiving Asynchronous Callback Command Results"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/zh-cn_topic_AsyncCallbackCommandApiService_receivePOST.html"
depth: 6
---
#### Function Description

It starts with GDE24.2. The results of some commands cannot be returned immediately after they are sent. Instead, the results are returned in asynchronous callback mode. A third-party system needs to call this interface to send back the command result.