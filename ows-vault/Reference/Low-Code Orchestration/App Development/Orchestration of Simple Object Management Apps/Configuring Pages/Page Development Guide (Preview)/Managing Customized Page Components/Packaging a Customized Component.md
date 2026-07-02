---
title: "Packaging a Customized Component"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_012.html"
depth: 6
---
#### Procedure

1.  In the VSCode-huawei tool, choose **View** > **Terminal** on the toolbar.
2.  In the displayed window at the bottom, enter **adc run** to perform local debugging.
3.  In the displayed window at the bottom, enter **adc build** to run the packaging command. You can run the **adc build major**, **adc build minor**, or **adc build patch** command to automatically change the version of a customized component.
4.  Verify that the message "Build successfully!" is displayed, and the packaging is successful.
5.  In the local code directory, obtain the compressed package _xxxxxx_**.zip**.