---
title: "Rule: Do Not Release Invalid Code or Configurations"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001163119066.html"
depth: 5
---
# Rule: Do Not Release Invalid Code or Configurations

**Description**: Developers must delete code, models, services, and pages that are invalid due to various causes during implementation. The following problems may occur if these valid code, models, services, and pages are retained:

-   Potential vulnerabilities: JavaScript, Python, and Ruby are interpretative languages. Commenting cannot delete functions permanently. Individuals with malicious purposes can modify comments, easily restore the functions, and affect product use.
-   Increasing number of attacks: Invalid services and pages increase the number of attacks of the system and are difficult to be detected because they are infrequently used.
-   Occupying resources: Models correspond to database tables. Invalid models occupy storage resources.
-   Technical debt: Developers will be trapped after the codes, models, services, and pages change. They do not understand the logic and are unwilling to delete the invalid codes, models, services, and pages due to potential risks.

**Check guide**: Go to the develop-state environment, select the app to be checked, view the models, services, pages, and code one by one, and delete them if they are invalid.

**Example scenarios:**

-   Services that are used only for debugging must be deleted before official release.
-   Pages developed only for demo presentation or unnecessary pages that are not actually called by services must be deleted before official release.
-   JavaScript code used only for function tests, which is different from the commented service code, must be deleted before official release.
-   The pages, services, JavaScript files, and models of obsolete functions must be deleted before official release.

**Tool supported or not**: yes

**Note**: Only invalid service codes can be checked. Invalid models, services, or pages cannot be checked. Checking them requires other tools with the assistance of manual check.

**Specification name**: Security\_SensitiveData\_Store\_Dead\_Code

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]