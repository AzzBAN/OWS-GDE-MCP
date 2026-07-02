---
title: "Asynchronous Request Service Is Used in addValidation"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399060797.html"
depth: 3
---
# Asynchronous Request Service Is Used in addValidation

In the versions using VUE, you need to perform the following adaptation rectification (setTimeout is equivalent to the asynchronous request service):

C('form1').addValidation({
         id : 'digit',
         checkRule : function(value){
             return new Promise(function(resolve,reject){
                 setTimeout(function(){
                     let flag \= value\>100 ? true : false
                     if(!flag){
                         reject("<100!");
                     }else(flag){
                         resolve(true);
                     }
                 },1000)
             })
         }
     });
  })

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]