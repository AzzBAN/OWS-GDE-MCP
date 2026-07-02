---
title: "ajax Is Invoked Synchronously"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002399060793.html"
depth: 3
---
# ajax Is Invoked Synchronously

**pageScriptName: appManagement**

$.ajax({
	url: NfUtil.getRootContext()+"/appIO/queryAsyncTaskStatus.action",
	type: "post",
	async: false,
	dataType: "json",
	data: params,
	success: function(data){
		//
	},
	error: function(jqXHR){
		result=true;
	}
});

**Solution:** The current jQuery is compatible. However, the page performance is affected after the verification. You are advised to perform the rectification and process the subsequent logic in the callback method.

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]