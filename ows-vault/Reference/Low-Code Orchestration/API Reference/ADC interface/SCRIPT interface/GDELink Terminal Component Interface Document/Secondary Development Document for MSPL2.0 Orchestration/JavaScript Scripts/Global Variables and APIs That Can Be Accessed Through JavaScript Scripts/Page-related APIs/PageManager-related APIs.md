---
title: "PageManager-related APIs"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001367927657.html"
depth: 9
---
#### Nf.PageManager.open(page,parameter,config)

Function of the page that is redirected to, which is used to open a page and is usually bound to the button clicking event Nf.PageManager.open.

-   **page**: Indicates the page that is redirected to. The value is of the string type in "/_projectName_/_moduleName_/_pageName_" format, for example, **/demo/test/page**.
-   **parameter**: Indicates the parameter of the page that is redirected to. The value is of the object type.
-   **config**: The value is of the object type. The configuration of the page that is redirected to is as follows:

  
| Property | Type/Value | Description |
| :-- | :-- | :-- |
| history | Number | (Optional) Whether to record the page that is redirected to in the page history and return to the page by performing the rollback action.
-   **RECORD**: The history of the page that is redirected to is recorded.
-   **REPLACE**: The page history of the current page is replaced.
-   **NO\_RECORD**: The page that is redirected to is not recorded in the page history. That is, the page is only a transition page and cannot be accessed by performing the rollback operation.

 |
| startPoint | Boolean | (Optional) Whether the page is the start page. If it is, the rollback cannot be performed.

-   **true**: The page is the start page.
-   **false**: The page is not the start page.

 |
| refresh | Boolean | (Optional) Whether to refresh the page if the opened page exists.

-   **true**: Refresh the page if the opened page exists.
-   **false**: Do not refresh the page if the opened page exists.

 | Example:

C ("button3").on ("click", function () {
// Page that is redirected to
Nf.PageManager.open ("/demo/test/PersonSelect");
});
C ("button3").on ("click", function () {
// Redirect to the page and set parameters.
Nf.PageManager.open ("/demo/test/PersonSelect", {task\_id: "001"}, {history: NO\_RECORD, startPoint: true, refresh: false});
});