---
title: "Rule: Native JS Objects Cannot Be Used for JS Customization"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208200345.html"
depth: 6
---
# Rule: Native JS Objects Cannot Be Used for JS Customization

**Description**: In new page scenarios, non-common JavaScript objects cannot be used for JavaScript customization on front-end pages. Instead, APIs provided by the platform must be used to process the service logic. The main reasons are as follows: The internal implementation of platform components evolves continuously. If the internal native JavaScript objects are used, the compatibility is not guaranteed on the platform side.

The API document is released with the version. You can obtain the document from the online secondary development guide.

**Check guide**: Do not directly use JavaScript objects (such as jQuery, Vue, and echarts) for frontend page customization. Use the capabilities provided by the platform UI, such as Spl, S, and U. For details, see the online development guide.

To use non-common JavaScript objects, such as Vue, you need to import the corresponding third-party JavaScript class library, add a reference script on the page to be used, and use the JavaScript objects provided in the third-party JavaScript class library in the script.

**Positive example**:

Example 1

![[en-us_image_0000001149666381.png]]

Example 2

![[en-us_image_0000001773332130.png]]

![[en-us_image_0000001699300598.png]]

**Negative example**

![[en-us_image_0000001149546451.png]]

**Tool supported or not**: no

**Specification name**: General\_Page\_Forbidden\_Use\_Native\_JavaScript\_or\_Private APIs

**Severity**: major

**Parent topic:** [[Page|Page]]