---
title: "Suggestion: Manage Custom Functions of the Same Tenant in a Centralized Manner"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001236944719.html"
depth: 6
---
# Suggestion: Manage Custom Functions of the Same Tenant in a Centralized Manner

**Specification name**: General\_DataFactory\_Custom\_Function\_Centralized\_Management

**Description**: You are advised to manage custom functions of the same tenant in one Java project, and use the arbitration mechanism of a version management tool (such as Maven) to resolve the version conflict of third-party JAR packages. For example, use an app to manage custom functions, and manage the app as a basic package. The app version should be stable.

-   General rule: Developers need to manually resolve conflicts among classes, function names, and third-party dependencies of different custom functions in app packages.
-   When different custom functions in the develop-state environment depend on the same dependency software:
    -   During the upload, the newly uploaded dependency software overwrites the uploaded file with the same name, but DataFactory records the complete dependency relationship.
    -   When you delete the implementation or dependency file of a custom function, only the software instance that is not depended on can be deleted. Otherwise, only the dependency relationship is deleted.
-   During compilation and packaging in the develop-state environment, if different custom functions in the same app depend on third-party JAR packages with the same name, only one of such packages is retained.
-   When apps and custom functions are installed on the engine, the newly installed third-party JAR package that different apps or custom functions depend on overwrites the existing one that has the same name.

**Check guide**:

1.  Check whether different custom functions of one tenant are implemented in the same Java project. If not, check whether the custom functions defined in different Java projects are duplicate and whether Java projects depend on different versions of the same third-party software.
2.  Check whether custom functions are centrally managed by one or a few apps.

**Positive example**: Custom functions in the _xxx_ domain are managed by the _xxx_\_Custom\_Function-1.0.0 app.

**Impact**: Scattered custom functions are difficult to manage, which may cause repeated definitions and conflicts. In addition, third-party software that custom functions depend on may have repeated dependencies or even version conflicts.

**Parent topic:** [[Management and Usage of Custom Functions|Management and Usage of Custom Functions]]