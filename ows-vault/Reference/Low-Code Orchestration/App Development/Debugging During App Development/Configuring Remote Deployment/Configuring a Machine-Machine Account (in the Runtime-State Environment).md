---
title: "Configuring a Machine-Machine Account (in the Runtime-State Environment)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_047.html"
depth: 4
---
#### Context

Remote deployment requires authorization of the runtime-state environment. Therefore, you need to configure a machine-machine account used for authentication and authorization. When multiple remote runtime-state environments are required, the machine-machine account must obtain the authentication and authorization of each environment.

A machine-machine role **adc-remote-app-manager** is preset in the system. You need to create a machine-machine account and associate it with this preset role for authenticating the environment configured with remote deployment.