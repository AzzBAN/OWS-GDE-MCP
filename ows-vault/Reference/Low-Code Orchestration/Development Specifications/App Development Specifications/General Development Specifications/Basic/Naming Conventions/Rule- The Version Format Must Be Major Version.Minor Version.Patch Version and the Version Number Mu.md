---
title: "Rule: The Version Format Must Be Major Version.Minor Version.Patch Version and the Version Number Must Increase in Ascending Order If an Asset Is Released Again After Modifications"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403805.html"
depth: 6
---
# Rule: The Version Format Must Be Major Version.Minor Version.Patch Version and the Version Number Must Increase in Ascending Order If an Asset Is Released Again After Modifications

**Description**: A properly defined version number facilitates feature maintenance. If no version number is defined or the version number is not clear, it is difficult to locate problems and upgrade the asset. When an asset is released again after being modified, the version number must increase in ascending order. For issue fixing, increase the minor version number; for new functions or significant function or feature changes, increase the major version number.

Recommended version format: _Major version_._Minor version_._Patch version_. Increasing rules are as follows:

It is recommended that the version number be 1.0.0 in the initial phase of a project.

Major version number: applies to the scenario where the project changes globally when you make incompatible API modifications, a major modification, or various partial modifications.

Minor version number: applies to the scenario where you add backwards compatible functions or add some functions based on the original ones.

Patch version applies to the scenario where you make backwards compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the _Major version_._Minor version_._Patch version_ format.

Reference: _Semantic Versioning_ ([https://semver.org](https://semver.org/))

**Check guide**:

Before release, check whether the version number used by the current asset meets the specifications requirements and whether the version number has been used.

**Positive example**: The version number developed in the current project is 2.0.0. After partial modification, the version is upgraded to 2.0.1. Later, major rectification is performed and the version is upgraded to 3.0.0.

**Impact**: If this rule is violated, the content between assets may be inconsistent and cannot be traced. As a result, the site upgrade fails and services are interrupted.

**Tool supported or not**: no

**Specification name**: General\_Basic\_Proper\_Asset\_Version

**Severity**: minor

**Parent topic:** [[Naming Conventions|Naming Conventions]]