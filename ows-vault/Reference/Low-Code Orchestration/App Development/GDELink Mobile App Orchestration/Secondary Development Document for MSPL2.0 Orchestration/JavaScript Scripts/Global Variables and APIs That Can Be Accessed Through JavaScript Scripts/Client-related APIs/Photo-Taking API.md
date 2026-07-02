---
title: "Photo-Taking API"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001406957408.html"
depth: 7
---
#### U.takePhoto(options, callback)

Used to switch to the native photo-taking page. You can add watermarks to the photos by configuring parameters.

![[notice_3.0-en-us.png]]

-   This function is supported on Android and HarmonyOS. The iOS version supports only simple photo taking.
-   When calling this API, you need to modify **Key** to **Value** corresponding to **camera\_permission\_detail** in internationalization resources based on site requirements to describe the application scenario and purpose of the camera. For example, you can scan the QR code to add environment configuration information and take photos to record assets. If you do not need such services, you can revoke this permission at any time. Your use of other services will not be affected.

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| options | Object | Photo-taking configuration |
| callback | Function | Successful callback | Input parameters of options

**Table 1** Photo-taking configuration       
| Parameter | Subparameter 1 | Subparameter 2 | Subparameter 3 | Subparameter 4 | Description | Example Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| preferredWidth | \- | \- | \- | \- | Width of the camera (not higher than the supported maximum width). If this parameter is not specified, the maximum width (unit: px) of the system is used by default. This parameter is optional. | 390 |
| preferredHeight | \- | \- | \- | \- | Height of the camera (not higher than the supported maximum height). If this parameter is not specified, the maximum height (unit: px) of the system is used by default. This parameter is optional. | 844 |
| devicePosition | \- | \- | \- | \- | (Optional) Initial camera orientation. The options are front (front camera) and back (rear camera). The default value is back. | back |
| flash | \- | \- | \- | \- | (Optional) Initial flash configuration. The options are on (enabled) and off (disabled). The default value is off. | off |
| total | \- | \- | \- | \- | Total number of photos. This parameter is optional, and the default value is 1. | 5 |
| preferredSize | \- | \- | \- | \- | (Optional) Photo compression size, in bytes. If this parameter is not specified, the photo is not compressed. | \- |
| preferredQuality | \- | \- | \- | \- | (Optional) Photo compression ratio, in percentage. If this parameter is not specified, the photo is not compressed. | 5 |
| waterMark | \- | \- | \- | \- | (Optional) Watermark setting. | 5 |
| width | \- | \- | \- | (Mandatory) Watermark width, in pixels. | \- |
| height | \- | \- | \- | Watermark height, in pixels. This parameter is mandatory. | \- |
| position | \- | \- | \- | Watermark position. This parameter is optional. | \- |
| horizontal | \- | \- | Horizontal position. The options are left, middle, and right. This parameter is optional, and the default value is left. | left |
| vertical | \- | \- | Vertical position. The options are top, middle, and bottom. This parameter is optional, and the default value is left. | left |
| margin | \- | \- | Outer margin, in pixels. This parameter is optional, and the default value is 10. | 10 |
| background | \- | \- | \- | Watermark background color | \- |
| color | \- | \- | Color (format: #xxxxxxxx). This parameter is optional, and the default value is null. | #dddddddd |
| image | \- | \- | Image path. The value is in the format of "images/catalogName/pictureName". You can upload an image on the Image Management page. This parameter is optional. | images/test/test.png |
| content | \- | \- | \- | Watermark content. Multiple lines are supported. | \- |
| color | \- | \- | Content background color. The value is in the format of "#xxxxxxxx". This parameter is optional, and the default value is #ffffffff. | #ffffffff |
| margin | \- | \- | (Optional) Outer margin. | \- |
| left | \- | (Optional) Left margin, in pixels. The default value is 10. | 10 |
| bottom | \- | (Optional) Bottom margin, in pixels. The default value is 10. | 10 |
| right | \- | (Optional) Right margin, in pixels. The default value is 10. | 10 |
| top | \- | (Optional) Top margin, in pixels. The default value is 10. | 10 |
| padding | \- | \- | (Optional) Inner margin, in pixels. The default value is 10. | 10 |
| textArea | \- | \- | Watermark text. The value is a JSON array. | \- |
| text | \- | (Optional) Text content. | \- |
| font | \- | (Optional) Text font. | \- |
| family | (Optional) Font name. The default value is the system font. | \- |
| size | (Optional) Font size, in pixels. The default value is the system font size. | \- |
| style | (Optional) Font style. The options are normal and bold. The default value is normal. | normal | Example:

const options = { 
 preferredWidth: 3000, 
 preferredHeight: 3000, 
 total: 3, 
 waterMark: { 
   width: 650, 
   height: 449, 
   position: { 
     horizontal: "left", 
     vertical: "bottom", 
     margin: 12, 
   }, 
   background: { 
     image: "images/test/test.png", 
   }, 
   content: { 
     margin: { 
       left: 3, 
       bottom: 3, 
       right: 3, 
       top: 270, 
     }, 
     padding: 8, 
     textArea: \[ 
       { 
text: "Beta\_20230101 test item Beta\_20230101 test item Beta\_20230101 test item",
         font: { 
           size: 25, 
           style: "bold", 
         } 
       }, 
       { 
         text: "Longitude and latitude: 34.1458 108.2266",
         font: { 
           size: 18, 
         } 
       }, 
       { 
         text: "Address: Nanjing, Jiangsu Province",
         font: { 
           size: 18, 
         } 
       }, 
       {  
        text: "Time: 2023-01-01 12:00:00",
         font: { 
           size: 18, 
         } 
       } 
     \] 
   } 
 }, 
}; 
const showResult = function(result) { 
 //result: \["file:///data/user/0/com.huawei.gdelink/files/apigw.huawei.com-api-217/1002/1686791549000301087/takePhoto/Pic\_20230701102905275.jpg"\] 
}; 
U.takePhoto(options, showResult);