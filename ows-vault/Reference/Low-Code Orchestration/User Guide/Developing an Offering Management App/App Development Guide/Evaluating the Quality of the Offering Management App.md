---
title: "Evaluating the Quality of the Offering Management App"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/demo_020.html"
depth: 4
---
#### Procedure

1.  Choose **Project Management**.
2.  Open the created project and click **Quality Check** at the bottom.
3.  Expand the check box at the bottom of the page and start the check.
    
    After the check is complete, if there are element items that do not comply with the rules, you can click the value in the **Rule Name** column in the list to learn about the rules.
    
4.  Modify the quality result based on the check result. The following figure shows an example.
    
    ![[en-us_image_0000001540929910.png]]
    
    ![[en-us_image_0000001567765596.png]]
    
    1.  Click a rule name in the **Rule Name** column to view its details. This rule requires that permission items be configured if **Metadata can be accessed by the frontend** and **Data can be accessed by the frontend** are enabled for the model.
    2.  In the navigation pane, choose **Model**.
    3.  Click **Edit** for the **info\_goods** model.
    4.  The check result shows that the permission item is not configured when **Data can be accessed by the frontend** is enabled.
        
        ![[en-us_image_0000001618404937.png]]
        
    5.  According to the evaluation, you do not need to enable the two buttons for the **info\_goods** model.
        
        ![[en-us_image_0000001567766040.png]]
        
    
5.  Click **Recheck**. After the full score is displayed, click **Export** to obtain the report that passes the quality check.
    
    ![[en-us_image_0000001567925828.png]]