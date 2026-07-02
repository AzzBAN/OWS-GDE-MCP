---
title: "Debugging a Custom Component"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_030.html"
depth: 6
---
#### Procedure

1.  Debugging a local custom component depends on the online environment. You can log in to the online develop-state environment first.
2.  The developed custom component needs to be debugged locally. You need to modify the **envs.js** file. The code path is **/build/wepack/envs.js**. The following is an example:
    
    module.exports = {
      serverAddr: "https://10.10.10.100:38443/",
      auth: "",
      cookies: "locale=zh\_CN;MATEINFO\_SESSION\_ID=de1be14a-6a45-4fbb-adea-906a7f3d1e20;tenant\_id=2000;"
    };
    
    The fields are described as follows. If you log out of the online environment and log in again, you need to update the configuration file in **env.js**.
    
    **Table 1** Field description  
    | Name | Description |
    | :-- | :-- |
    | serverAddr | Online environment address, including the IP address and port number, for example, https://10.10.10.100:38443/ Copy the address from the obtained online environment address according to the format. |
    | cookies | Construct cookies for verification, including language settings. Generally, you do not need to change the language. MATEINFO\_SESSION\_ID: indicates the session ID in cookies in the develop-state environment. Obtain the cookies for directly accessing the online environment. For details about how to obtain the cookies, see the following figure. Figure 1 Obtaining cookies | 3.  Run the **adc run** command to perform online debugging.