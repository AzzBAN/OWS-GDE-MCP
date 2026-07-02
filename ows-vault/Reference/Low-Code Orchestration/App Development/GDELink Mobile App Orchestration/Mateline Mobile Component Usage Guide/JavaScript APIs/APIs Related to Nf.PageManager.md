---
title: "APIs Related to Nf.PageManager"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001731564074.html"
depth: 5
---
# APIs Related to Nf.PageManager

**Nf.PageManager.open**

**NfPageOpen**

A page redirection function, which is used to open a page.

Input parameters:

**page** (string): Name of the target page, which ends with **mspl**.

**parameter** (object): Parameters related to the target page

**config** (object): Configuration of the target page

  
| Property | Type/Value | Meaning |
| :-- | :-- | :-- |
| target | String | Whether the target page is an extended page of the current page or a new page. |
| \- | \_self | Extended page |
| \- | Others | \- |
| history | Number | Whether to record the history of the target page |
| \- | Nf.PageManager.History.RECORD | The history of the target page is recorded. |
| \- | Nf.PageManager.History.REPLACE | The page history of the current page is replaced. |
| \- | Nf.PageManager.History.NO\_RECORD | The history of the target page is not recorded. |
| startPoint | Boolean | Whether the page is the start page. If it is, the rollback cannot be performed. |
| \- | true | The page is a start page. |
| \- | false | The page is not a start page. |
| refresh | Boolean | Whether to refresh the page if the opened page exists. |
| \- | true | Refresh the page if the opened page exists. |
| \- | false | Do not refresh the page if the opened page exists. | Example:

Nf.PageReady(function(){
C("button").on("click",function(){
//The page history of the target page is not recorded.
Nf.PageManager.open("ignoreItemPageHistory\_2.mspl","",
{history:Nf.PageManager.History.NO\_RECORD});
});
});

**Nf.PageManager.getCurrentPage()**

**CurrentPage()**

Used to obtain the object of the current page.

Input parameters: none

Example:

var currentPage1 = CurrentPage();
var currentPage2 = Nf.PageManager.getCurrentPage();

**CurrentPage().parameters\[key\]**

Used to obtain the parameters transferred from the previous page to the current page.

Input parameters:

**key** (string): Key of a parameter

Example:

var taskId = CurrentPage().parameters\["task\_id"\];

**Global**

**backto\_page()**

Used to return to the previous page.

Input parameters: none

Example:

backto\_page()

**Parent topic:** [[JavaScript APIs|JavaScript APIs]]