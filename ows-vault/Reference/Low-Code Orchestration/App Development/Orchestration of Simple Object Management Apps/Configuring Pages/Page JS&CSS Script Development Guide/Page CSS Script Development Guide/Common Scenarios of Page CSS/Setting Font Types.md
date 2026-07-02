---
title: "Setting Font Types"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_ui_script_013.html"
depth: 7
---
# Setting Font Types

[[Creating a CSS Script|Creating a CSS Script]] shows how to set the font style for the field whose ID is set to **projName**.

**Changing the font color**

#projName {color:red;}

**Changing the font style**

#projName {font-family:Fantasy;}

**Changing the indentation**

 #projName {text-indent:50px;}
//Indent the left side of the text by 50 pixels.

**Changing the alignment**

#projName {direction:rtl;}
//The start position of the text is changed to the right, and the indentation is changed to 50 pixels from right to left.

**Changing the text decoration**

#projName {text-decoration:overline;}
//A hyphen appears in the text. It can also be set to **underline** or **line-through**.

**Changing the shadow**

#projName {text-shadow:2px 2px green;}
//The text has a dark green shadow. You can adjust the position and color of the shadow.

**Changing the italic style**

#projName {font-style:italic;}
//The text is displayed in italic. However, it invalidates the font style.

**Parent topic:** [[Common Scenarios of Page CSS|Common Scenarios of Page CSS]]