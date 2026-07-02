---
title: "Rule: Sensitive Data Cannot Be Stored in localStorage"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001162959130.html"
depth: 5
---
# Rule: Sensitive Data Cannot Be Stored in localStorage

**Description**: HTML5 provides the localStorage mechanism to enable developers to retain code values when programs are running. The localStorage mechanism permanently stores data in the local PC. The data will not be deleted when you close the browser. If developers store sensitive data in localStorage, improper data disclosure may occur once the browser is hijacked.

**Check guide**: Go to the develop-state environment, select the app to be checked, check whether the code of all pages contains the keyword **localStorage**, and further check whether sensitive data is stored in the code.

**Negative example**:

var key="password";

localStorage.setItem(key,password);

**Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_Store\_In\_LocalStorage

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]