---
title: "MultiPart"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_040.html"
depth: 7
---
# MultiPart

**Table 1** MultiPart   
| API | Description | Example |
| :-- | :-- | :-- |
| MultiPart.post() | Submits the file stream to the file operation interface through a form. | 
var url = "cse://adc-file/rest/v1/file-token/upload?file\_token={file\_token}";  
//request body
var requestBody = {
    "file":xxx
}
// filetoken keys
var  fileTokenKeys = \["file"\]
//request param
var urlVariables = {
    "file\_token":yyy
}
// function call
var res = MultiPart.post(url,requestBody,fileTokenKeys,urlVariables)
return res;

 | **Parent topic:** [[Service APIs|Service APIs]]