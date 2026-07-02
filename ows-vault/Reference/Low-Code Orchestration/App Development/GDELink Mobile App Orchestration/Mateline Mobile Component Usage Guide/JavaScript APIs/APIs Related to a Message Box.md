---
title: "APIs Related to a Message Box"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001778643517.html"
depth: 5
---
# APIs Related to a Message Box

**Nf.promptConfirm**

This is a confirmation message box. It provides two buttons: one for confirmation and one for cancellation.

Input parameters:

**option** (object): Parameters of a message box, as listed in the following table.

  
| Property | Type | Meaning |
| :-- | :-- | :-- |
| title | String | (Optional) Title |
| message | String | Message body |
| okText | String | (Optional) Text of the confirm button (with a default value) |
| cancelText | String | (Optional) Text of the cancel button (with a default value) |
| yes | function | Callback of the confirm button |
| no | function | Callback of the cancel button | Example:

Nf.promptConfirm({
title:"prompt title",
message:"prompt message",
okText:"confirm",
cancelText:"exit",
yes:function(){
console.log("confirm is clicked");},
no:function(){
console.log("exit is clicked");
}
});

Alternatively, use the default button and omit the title.

Nf.promptConfirm({
message:"prompt message",
yes:function(){
console.log("confirm is clicked");
},
no:function(){
console.log("exit is clicked");
}
});

**Nf.promptError**

This is an error prompt message box. It provides a close button.

Input parameters:

**option** (object): Parameters of a message box, as listed in the following table.

  
| Property | Type | Meaning |
| :-- | :-- | :-- |
| title | String | (Optional) Title |
| message | String | Message body |
| okText | String | (Optional) Text of the close button (with a default value) |
| yes | function | Callback of the confirm button | Example:

Nf.promptError({
title:"Error title",
message:"prompt message",
okText:"close",
yes:function(){
console.log("confirm is clicked");
}
});

Alternatively, use the default button and omit the title.

Nf.promptError({
message:"prompt message"
});

**Nf.prompt**

This is a success prompt message box. It provides a close button.

Input parameters:

**option** (object): Parameters of a message box, as listed in the following table.

  
| Property | Type | Meaning |
| :-- | :-- | :-- |
| tile | String | (Optional) Title |
| message | String | Message body |
| okText | String | (Optional) Text of the close button (with a default value) |
| yes | function | Callback of the confirm button | Example:

Nf.prompt({
title:"success title",
message:"prompt message",
okText:"close",
yes:function(){
console.log("confirm is clicked");
}
});

Alternatively, use the default button and omit the title.

Nf.prompt({
message:"prompt message"
})

**Nf.showPopup**

This is a dialog box. It does not provide a button and it disappears in 3 seconds by default.

Input parameters:

**option** (object): Parameters of a message box, as listed in the following table.

  
| Property | Type | Meaning |
| :-- | :-- | :-- |
| message | String | Message body | Example:

Nf.showPopup({
message:"prompt message"
});

**Nf.showPopupWindow**

This is a dialog box whose content can be customized. It disappears in 3 seconds by default.

Input parameters:

**option** (object): Parameters of a message box, as listed in the following table.

  
| Property | Type | Meaning |
| :-- | :-- | :-- |
| title | String | (Optional) Title |
| message | String | Message body |
| okText | String | (Optional) Text of the confirm button (with a default value) |
| cancelText | String | (Optional) Text of the cancel button (with a default value) |
| yes | function | Callback of the confirm button |
| no | function | Callback of the cancel button | Example:

Nf.showPopupWindow({
title:'InputReason',
waittime:'100000',
message:"<input type="text">",
buttons: \[
{ text: 'CANCEL'},
{text: 'CONFIRM',
handler: function(e) {console.log('aaa');}
}\]
});

**Parent topic:** [[JavaScript APIs|JavaScript APIs]]