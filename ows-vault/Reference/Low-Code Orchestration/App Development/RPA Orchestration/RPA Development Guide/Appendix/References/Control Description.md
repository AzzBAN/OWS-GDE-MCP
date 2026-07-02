---
title: "Control Description"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001214926159.html"
depth: 6
---
#### Restrictions

-   RPA provides security protection for robots by means of prompt messages, role permission separation, and whitelist control for high-risk commands. However, due to business scenario requirements, users record any operation, develop executable scripts such as Python scripts, execute SQL statements, and run **SendKeys** to transfer function keys. Therefore, users are liable for the security risks caused by the operations, executable scripts, and function keys. In addition, users can decide not to deliver and execute this type of robots.
-   When a job is executed, the robot operates the file system and executes local programs based on orchestrated controls, which occupies the file system, CPU, and memory. You need to consider the impact on the file system and OS when orchestrating these controls.
-   If the control references or processes files, the following file types are supported:
    
    .doc, .docx, .xls, .xlsx, .xlsm, .ppt, .pptx, .json, .zip, .rar, .7z, .gz, .vsd, .gif, .png, .jpg, .jpeg, .pdf, .msg, .oft, .htm, .html, .xml, .svg, .app, .itf, .bm, .jks, .keystore, .patch, .wav, .ico, .mp4, .avi, .bmp, .tif, .tiff, .exe, .dll, .jar, .wsdl, .so, .data, .spl, .apk, .keytab, .txt, .bas, .csv, .tar, .py, .cer, .crt, .pem, .key, and .bat
    
-   In Studio 2.14.0, **UI Automation** controls, including **Java**, **web**, and **Win32** playback controls, are added to replace UI common processing controls in versions earlier than 2.14.0. The original **UI Common** is changed to **UI(deprecated)** to ensure software compatibility. In the same scenario, these two types of controls cannot be used together. Otherwise, unexpected exceptions may occur.