---
title: "How Do I Obtain the Service Certificate and CRL?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001207597477.html"
depth: 7
---
#### Procedure

The following uses Google Chrome as an example to describe how to obtain the digital certificate and CRL of the server.

1.  Use a browser to open the web page of the server.
2.  Click ![[en-us_image_0000001211925971.png]] on the left of the URL and select **Certificate (Valid)**.
3.  Export the service certificate.
    
    1.  Click the **Details** tab, and click **Copy to File**.
        
        ![[en-us_image_0000001166328294.png]]
        
    2.  Click **Next**.
    3.  In the displayed **Export File Format** dialog box, select **DER encoded binary X.509 (.CER)**, and click **Next**.
        
        ![[en-us_image_0000001166009788.png]]
        
    4.  Click **Browse** on the right of **File Name**, select the directory where the file to be imported is located and enter the file name, and click **Next**.
        
        ![[en-us_image_0000001211609721.png]]
        
    5.  Check details about the exported certificate, and click **Finish**.
        
        ![[en-us_image_0000001166168350.png]]
        
    6.  In the displayed **Certificate Export Wizard** dialog box, click **OK** to save the service certificate to the specified directory.
    
4.  Export the CRL.
    
    1.  Click the **Details** tab, and click **CRL Distribution Points** in the **Field** column.
        
        ![[en-us_image_0000001211690095.png]]
        
    2.  In the content display box in the lower part, copy the URL information.
    3.  Enter the copied URL in the address box of the browser to download the CRL to your local PC.