---
title: "GDE's Security Responsibilities"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001104348628.html"
depth: 4
---
# GDE's Security Responsibilities

GDE securely operates the infrastructure provided by HEC. GDE is responsible for the security configuration, security policies, security event handling, and security hardening of the infrastructure.

GDE is responsible for the security of platforms and services built on the HEC infrastructure. In addition, for HEC products (such as ECS, VPC, and OBS) used by GDE, their security configurations and tasks must be assured by GDE. GDE manages guest OSs (including upgrades and security patches), application software or programs installed on instances, and firewall (security group) configurations provided by HEC on each instance.

For web applications provided by GDE, their security must be assured by GDE. For web applications developed by tenants using existing resources or microservices, their security must be assured by tenants. GDE provides the security review mechanism and capability.

For data protection, the tenant is the data controller, and GDE is the data processor. GDE is responsible for security control and protection of data on GDE. In addition, GDE isolates data between tenants.

GDE provides security capabilities such as account permission minimization and data isolation, provides security regulation enablement, and implements security audit to ensure the security of accounts and permissions. The tenant must ensure the security of their own accounts and data.

**Parent topic:** [[Security Responsibilities|Security Responsibilities]]