---
title: "API for Sending Emails (EmailUtil)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_037.html"
depth: 7
---
# API for Sending Emails (EmailUtil)

**Table 1** EmailUtil   
| API | Description | Example |
| :-- | :-- | :-- |
| EmailUtil.sendEmail(emailRequest\[, config\]) | Sending of an email without attachments
-   The format of emailRequest is as follows:
    
    {
      "emailInfo": {
        "sender": {
          "email": "Sender email address.",
          "userId": "Sender ID.",
          "personal": "Sender alias, which contains a maximum of 256 characters."
        },
        "ccRecipients": {
          "emails": "User email address. This parameter is optional. The value is in the format of List<String>.",
          "userIds": "User ID. This parameter is optional. The value type is in the format of List<String>.",
          "groupIds": "User group ID. This parameter is optional. The value type is in the format of List<String>.",
          "roleIds": "Role ID. The value is in the format of List<String>. This parameter is optional and is valid only when the user source is GAM."
        },
        "bccRecipients": {
          "emails": "User email address. This parameter is optional. The value is in the format of List<String>.",
          "userIds": "User ID. This parameter is optional. The value type is in the format of List<String>.",
          "groupIds": "User group ID. This parameter is optional. The value type is in the format of List<String>.",
          "roleIds": "Role ID. The value is in the format of List<String>. This parameter is optional and is valid only when the user source is GAM."
        },
        "emails": "User email address. This parameter is optional. The value is in the format of List<String>.",
        "userIds": "User ID. This parameter is optional. The value type is in the format of List<String>.",
        "groupIds": "User group ID. This parameter is optional. The value type is in the format of List<String>.",
        "roleIds": "Role ID. The value is in the format of List<String>. This parameter is optional and is valid only when the user source is GAM."
        "agreeFlag": true,
        "subject": "Email subject, which is mandatory. The value is a string.",
        "content": "Email content, which is optional. The value is a string.",
        "userInfo": "User information, which is mandatory. The value is a string.",
        "recursionFlag": false,
        "triggerBy": "Remarks, which is optional. The value is a string.",
        "contentType": "Email content format, which is optional. The value is a string.",
        "isAsync": false
      },
      "files": \["token1", "token2"\]
    }
    
-   config format:
    
    {
        "emailServerId":"xx", 
        "emailServerName":"xx"
    }
    
-   Response format:
    
    {
        "retCode": 0,
        "retMsg": "success"
    }
    

 | var emailInfoDto  ={
    "userIds": \[1740021278000377063\], 
    "groupIds": \[\],
    "agreeFlag": true,
    "content": "This is a test message zsq",
    "emails": \["test@test.com"\],
    "ccRecipients": {
        "groupIds": \[\],
        "userIds": \[\],
        "roleIds": \[\],
        "emails": \[\]
    },
    "bccRecipients": {
        "groupIds": \[\],
        "userIds": \[\],
        "roleIds": \[\],
        "emails": \[\]
    },
    "subject": "This is a test message",
    "userInfo": "test",
    "contentType": "text/html",
    "triggerBy": "Trigger by test",
    "isAsync": "false"
};
var emailRequest = {
  "emailInfo": emailInfoDto,
  "files": \["token1", "token2", "token3"\] 
};
var config = {
    "emailServerId":"", 
    "emailServerName":""
};
var responce = EmailUtil.sendEmail(emailRequest, config);
return responce;

 | **Parent topic:** [[Service APIs|Service APIs]]