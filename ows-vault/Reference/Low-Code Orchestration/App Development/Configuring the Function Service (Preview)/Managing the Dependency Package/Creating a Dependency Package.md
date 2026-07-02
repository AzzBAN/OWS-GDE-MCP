---
title: "Creating a Dependency Package"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_faas_003.html"
depth: 4
---
#### Context

You can create dependency packages for open-source third-party software based on the following example for Python development. You can also create a dependency package based on the self-developed code by referring to the following example to implement code sharing and improve development efficiency in develop state.

![[note_3.0-en-us.png]]

-   Ensure that dependency packages and code packages do not contain the same directory or file. Otherwise, errors may occur due to overwriting and combination.
-   If the dependency package fails to be uploaded, check whether the dependency package contains non-Python files, such as CSV, tar.gz, PPT, and Excel files. If yes, delete them.
-   The Python dependency package uploaded by the user varies depending on the system architecture. The dependency package needs to support dual architecture or can be uploaded again at the DR site after the DR switchover.