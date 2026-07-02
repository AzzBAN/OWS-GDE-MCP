---
title: "Setting Border Background Styles"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_ui_script_014.html"
depth: 7
---
# Setting Border Background Styles

[[Creating a CSS Script|Creating a CSS Script]] shows how to set the style of a button whose ID is **cancelBtn**.

**Changing the size**

#cancelBtn { 
height:100px; 
width:10%;}
//The height of the button changes to 100 pixels, and the width changes to 10% of the page.

**Changing the background color**

#cancelBtn {background-color:cyan;}
//The button color changes to cyan.

**Changing the border color, thickness, and style**

 #cancelBtn {  
  border: red 2px dashed;  
}
//The border of the button changes to a red dotted line with a width of two pixels. Note that setting the color property will overwrite the current color.

**Changing the border style**

 #cancelBtn {border-style: dotted doubledashed hidden;}
//The button border is changed to a dot line, double solid line, dotted line, or hidden line in the upper, right, lower, and left part, respectively.

**Changing the round corner of the border**

 #cancelBtn {border-radius:50%;}
//The border of the button changes to an ellipse.

**Parent topic:** [[Common Scenarios of Page CSS|Common Scenarios of Page CSS]]