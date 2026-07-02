---
title: "Rule: Use Auxiliary Functions and Common Functions Provided by API Fabric Instead of Java.type(\"\")"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001615187216.html"
depth: 6
---
# Rule: Use Auxiliary Functions and Common Functions Provided by API Fabric Instead of Java.type("")

**Description**: API Fabric provides various whitelist tool classes for scripts. The tool classes in auxiliary functions and common functions provide easy-to-use alias reference classes. You are advised to use the alias tool classes provided in auxiliary functions and common functions instead of Java.type("_Full restriction name of a class_"). During version upgrade, Java.type("") may be incompatible due to security reasons. As a result, the JS may be unavailable.

**Check guide**:

Check whether the JS script contains the usage of Java.type to obtain third-party classes.

**Rectification suggestion**:

1.  If functions same as those of Java.type can be provided by auxiliary functions and common functions, the classes provided by auxiliary functions and common functions are preferred.
2.  For classes that cannot be replaced, check whether the whitelist in API Fabric contains those classes.

**Tool supported or not**: no

**Specification name**: General\_API\_Prioritize\_Using\_Auxiliary\_and\_Common \_Functions\_Provided\_by\_Fabric

**Severity**: major

**Parent topic:** [[Openness Integration|Openness Integration]]