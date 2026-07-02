---
title: "What Can I Do If the Function Service Sandbox Does Not Contain the File Whitelist?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_faas_037.html"
depth: 4
---
#### Symptom

After ADC is upgraded from 24.5.6 to 24.5.9 or a later version, if the multi-thread function or rmtree method is used for changing the security sandbox, an error message is displayed due to sandbox permission restrictions. In this case, you can choose **Products and Services** > **Log Management** > **FaaS Task Run Log** in the runtime-state environment to view the log details of the corresponding function service. Information similar to the following figure is displayed in the function service log.

-   The following error is reported when the multi-thread function is used.
    -   Python 3.9:
        
        You don't have access to the file: /opt/mateinfo/python/python3.9/lib/python3.9/threading.py
        
    -   Python 3.11:
        
        You don't have access to the file: /opt/mateinfo/python/python3.11/lib/python3.11/threading.py
        

-   The following error is reported when the rmtree method is used.
    
    \[2023-11-02 01:33:57.000\]-\[6542fc7c0d8e542a\]-\[2004\]-\[INFO\]-\[FBBMalaysisIPMANFaaS\]-\[FBBMalaysisIPMANFaaS\]-\[FAAS\]-\[fbb\_malaysis\_ipman scri pt\_generation\]-\[adc\_loggerwrite:113\]-\[Function-Execution\]-\[-\[\]-\[\]-\[(ERROR\] (ed20f3e3\] You don't have access to the file: Undo Shutdown Route OL D PE1.\]