---
title: "Configuring Interworking Between Network Nodes (in the Develop-State Environment)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_049.html"
depth: 4
---
# Configuring Interworking Between Network Nodes (in the Develop-State Environment)

![[note_3.0-en-us.png]]

The operations described in this section need to be performed by delivery personnel or O&M personnel.

If the network between the docker node (adc-studio-project-mgt) where the develop-state project is managed and the docker node where the LB of the runtime-state environment is deployed is disconnected, remote deployment cannot be performed. In this case, you need to configure the network interworking.

Determine the network connection mode based on the actual network conditions.

-   Method 1: Bind the docker node where the project is managed to the host machine with a public IP address, for example, the maccrt01 node. This operation must be performed at the IaaS layer. Contact the IaaS administrator to perform this operation or perform this operation by referring to the IaaS guide. This method is preferred. If this method cannot be used, use method 2.
-   Method 2: If the LB nodes in the develop-state environment and runtime-state environment can communicate with each other, configure the reverse proxy on the LB node in the develop-state environment. You do not need to manually configure this item. When you set the runtime-state environment information, enable the reverse proxy function. For details, see [[Managing the Runtime-State Environment Information (in the Develop-State Environment)|Managing the Runtime-State Environment Information (in the Develop-State Environment)]].
-   Method 3: In the public and private network scenarios, if the address of the deployment environment is a public network address, perform the following steps:
    1.  On the **Environment Management** page, turn on the **Enable the reverse proxy** switch. For details, see [[Managing the Runtime-State Environment Information (in the Develop-State Environment)|Managing the Runtime-State Environment Information (in the Develop-State Environment)]].
    2.  Log in to the lb-service node and run the following command to access the docker container where the lb-service node is deployed:
        
        Run the following command to check the container ID:
        
        **docker ps | grep lb-service**
        
        Run the following command to access the container:
        
        **docker exec -it** _Container ID_ **bash**
        
        ![[en-us_image_0000001509933422.png]]
        
    3.  Modify the environment configuration file.
        
        **vi /usr/local/NSP/etc/nginx/vhosts/route\_adc\_**_{Tenant ID}_**\_env.config**
        
        Replace _{Tenant ID}_ with the actual tenant ID, for example, **1002**.
        
        In the opened file, edit the configuration file and save it.
        
         location /adc-remote-install/tenant\_1002/**_{env\_name}_**/ {
            rewrite /adc-remote-install/tenant\_1002/**_{env\_name}_**/(.\*) /$1 break;
            proxy\_pass **_{lb\_external\_ip}_**;
        }
        
        **_{env\_name}_** indicates the environment name configured in [[Managing the Runtime-State Environment Information (in the Develop-State Environment)|Managing the Runtime-State Environment Information (in the Develop-State Environment)]].
        
        Set **_{lb\_external\_ip}_** to the value of **lb\_external\_url** in the **lb-cfg-configmap** configuration item, as shown in the following figure.
        
        ![[en-us_image_0000002175010261.png]]
        

**Parent topic:** [[Configuring Remote Deployment|Configuring Remote Deployment]]