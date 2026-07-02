---
title: "Suggestion: Limit the Size, Maximum Number of Files, and Maximum Number of Operators in the Asset Package for Data Orchestration Assets"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399403977.html"
depth: 5
---
# Suggestion: Limit the Size, Maximum Number of Files, and Maximum Number of Operators in the Asset Package for Data Orchestration Assets

**Description**: The size of the asset source code package, the number of files in the asset installation package, and the maximum number of operators in a single process must be limited, avoiding import timeout, loading timeout, and attack risks.

**Check guide**:

1.  Export the installation package after the compilation to check the file size.
2.  Export the asset source package on the project management page to view the file size.
3.  Export the asset source package on the project management page to view the number of files.
4.  Open the orchestration file to collect statistics on the number of operators.

**Positive example**:

-   The size of the installation package cannot exceed 2 GB.
-   The size of the source code package cannot exceed 2 GB.
-   The total number of files cannot exceed 1000.
-   The number of operators cannot exceed 100.

**Exception scenarios**: historical app import

**Tool supported or not**: yes

**Specification name**: Security\_DOS\_DataCube\_LimitAPPSize

**Category**: non-bottom-line check item

**Severity**: suggestion

**Orchestration scenario**: data orchestration

**Parent topic:** [[Anti-DoS|Anti-DoS]]