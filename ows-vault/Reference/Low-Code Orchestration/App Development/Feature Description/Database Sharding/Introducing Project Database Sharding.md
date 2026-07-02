---
title: "Introducing Project Database Sharding"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_sharding_001.html"
depth: 4
---
#### Introduction to Database Sharding

Sharding is a method for distributing a single dataset across multiple databases, which can then be stored on multiple machines. This allows for larger datasets to be split in smaller chunks and stored in multiple data nodes, increasing the total storage capacity of the system. By default, the system supports app database sharding. Developers need to configure the service domain of a project and create data sources for the service domain to implement database sharding.

**Figure 1** Database sharding diagram  
![[en-us_image_0000001190596101.png]]