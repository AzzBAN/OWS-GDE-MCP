---
title: "Image"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001782387993.html"
depth: 5
---
# Image

**Properties**

 
| Property Name | Description |
| :-- | :-- |
| badger | Image mark (After the configuration, a red mark is displayed in the upper right corner of the image.) |
| description | Image description |
| itemShowState | Image display status. false indicates that the image is not displayed. |
| label | Image label |
| linkParameters | Parameters carried when a user clicks an image to go to another page |
| location | Redirection location when an image is clicked |
| name | Component name |
| template | Custom image template |
| url | Image address. Example: /app/images/Tenant ID/Image directory/Image name?is\_mobile=true. The image referenced by the component must be in the same module as the page. |
| visible | Component visibility condition |
| compStyle | Component style |
| imageStyle | Image style | **APIs**

**getValue()**

Input parameters: none

Output parameters: String

Description: Obtain the image URL.

Example:

C("t").getValue();

**Events**

**click**

Description: click event

Example:

C("id").on("click",function(json){

//do something

})

**Parent topic:** [[Mobile Component Usage Guide|Mobile Component Usage Guide]]