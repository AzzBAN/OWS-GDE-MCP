---
title: "Context Language Environment Setting"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_038.html"
depth: 7
---
# Context Language Environment Setting

**Table 1** LocaleUtil   
| API | Description | Example |
| :-- | :-- | :-- |
| 
-   For the API of the latest version, which is version 2.0 or later, the engine version displayed on the GUI is **Latest**. LocaleUtil.setLocale(locale, \_runtime);
-   For the API of version 1.6, the engine version displayed on the GUI is **V 1.6**. LocaleUtil.setLocale(locale, \_CONTEXT);
-   For the API of version 1.5 or earlier, the engine version displayed on the GUI is **V 1.5**. LocaleUtil.setLocale(locale, message);

 | Used to set the context language environment. locale: language code, for example, "zh\_CN" (Chinese) or "en\_US" (English). | // For the API of the latest version, which is version 2.0 or later, the engine version displayed on the GUI is Latest.

LocaleUtil.setLocale("zh\_CN", \_runtime);

// For the API of version 1.6, the engine version displayed on the GUI is V 1.6.

LocaleUtil.setLocale("zh\_CN", \_CONTEXT);

// For the API of version 1.5 or earlier, the engine version displayed on the GUI is V 1.5.

LocaleUtil.setLocale("zh\_CN", message);

 | **Parent topic:** [[Service APIs|Service APIs]]