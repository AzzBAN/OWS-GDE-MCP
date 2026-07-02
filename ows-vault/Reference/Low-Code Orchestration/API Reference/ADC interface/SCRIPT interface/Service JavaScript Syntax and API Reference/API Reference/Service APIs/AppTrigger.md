---
title: "AppTrigger"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_031.html"
depth: 7
---
# AppTrigger

**Table 1** AppTrigger function   
| API | Description | Example |
| :-- | :-- | :-- |
| AppTrigger.beforeUninstallProgress(taskId,appName,version,progress,status,errorMsg) | This API is used to report the action execution progress before the app is uninstalled. When an app uninstallation triggering action is configured in a project, the progress of the triggering action must be reported.
-   **taskId**: indicates the UUID of the current uninstallation task, which is required when the progress is reported.
-   **appName**: indicates the name of the app to be uninstalled, which is used when the progress is reported.
-   **version**: indicates the version, which is required when the progress is reported.
-   **progress**: indicates the uninstallation progress. The value range is \[0, 100\].
-   **status**: indicates the status, which is optional. The default value is **0**. The value **0** indicates the normal status while the value **1** indicates the abnormal status.
-   **errorMsg**: indicates an error message returned when an exception occurs, which is optional. The value cannot contain Chinese characters and cannot exceed 1024 characters. If this parameter is not transferred, the default operation failure message returned by App Manager is used.

 | After the data is cleared before the uninstallation, the progress is reported.
var taskId = \_message.taskId;
var appName = \_message.appName;
var version = \_message.version;
AppTrigger.beforeUninstallProgress(taskId, appName, version, 0);
AppTrigger.beforeUninstallProgress(taskId, appName, version, 50);
AppTrigger.beforeUninstallProgress(taskId, appName, version, 100);
AppTrigger.beforeUninstallProgress(taskId, appName, version, 100, 1, "Unistall failed"); 

 | **Parent topic:** [[Service APIs|Service APIs]]