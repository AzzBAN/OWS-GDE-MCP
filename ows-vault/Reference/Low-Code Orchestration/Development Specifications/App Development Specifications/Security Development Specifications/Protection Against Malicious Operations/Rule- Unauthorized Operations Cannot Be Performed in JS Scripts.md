---
title: "Rule: Unauthorized Operations Cannot Be Performed in JS Scripts"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001339672257.html"
depth: 5
---
# Rule: Unauthorized Operations Cannot Be Performed in JS Scripts

**Description**: You can customize a JS script and encapsulate it into an activity in the JS activity of the technical operation orchestration service. The JS script can be used to parse and determine the command activity result. You can write only normal service logic in the JS script, and cannot execute invalid logic that is mainly targeted at attacks in the JS script.

**Check guide**: Check the JS script uploaded to the system to ensure that the JS script contains only proper and correct service processing logic.

**Positive example**: none

**Negative example**:

1.  Invalid service logic. The system CPU resources are consumed by infinite loop or invalid logic.
2.  Invalid memory operations. Excessive memory resources are requested, consuming system memory resources.
3.  Invalid file operations. For example, deleting files in the underlying running environment or generating junk files consumes the disk space.

**Exception scenarios**: none

**Examples of typical invalid JavaScript scripts**:

-   **Checking whether the script has XSS injection risks**

**Scenarios**:

1.  The eval command is used to execute variables.
2.  The property names of the assignment statement are **\*url** and **iframe\***, and the **U.escapeHtml** function is not enclosed in single or double quotation marks.
3.  Variables using HTML functions are not escaped using **escapeHtml**.
4.  The variables in the <div>...</div> tag are not enclosed in single or double quotation marks.
5.  The **prepend**, **promptConfirm**, **append**, **attr** and **before** functions use variable parameters.
6.  The **prepend** and **append** character strings do not contain **<** and **\>**.
7.  The **document.write**, **location.reload** and **window.open** functions use variable parameters.
8.  A variable or function is assigned to the right of the **innerHTML** function, and the function node does not contain **escapeHtml**.
    
    **Negative example**:
    
    if (servicetype === 'host') {
    
    txt.innerHTML = data.pa;
    
    } else {
    
    txt.innerHTML = data;
    
    }
    
9.  The div tag contains the **html\*** and **url\*** functions and the functions contain **innerHTML**.
10.  The JavaScript contains **a:\['target','href','title','class','style'\]** (the sequence of character strings can be changed).
11.  The **xssfilter** function contains **replace**, and the **replace** parameter is concatenated using vertical bars (|) and contains HTML tags.
     
     **Negative example**:
     
     function xssfilter(str){
     
     return str.replace(/(<script|<style|a)/ig, ' ').replace(/(<video|<audio|<strong>)/ig, ' ').replace(/(<h1>|<h2>|<h3>)/ig, ' ')
     
     }
     
12.  Variables or functions are assigned for **location.href** and **document.form.action**.
13.  The character string contains **href=**, and the expression following **href=** contains variables.
     
     **Negative example**:
     
     function func () {
     
     key = 'name'
     
     value = 'python'
     
     url = 'http://www.xxx.com?' + key + '=' + value
     
     return '<a href="' + url + '">'
     
     }
     
14.  The **jquery.min.js** file whose version is earlier than 3.5.0 exists.
15.  The character string **dangerouslySetInnerHTML=** exists.
16.  The value of the property variable (in the +\*+ or ${} format) in the **<div>** tag is **document.location.hash**.
     
     **Negative example**:
     
     url = document.location.hash
     
     function func () {
     
     return '<div class=' + url + '></div>'
     
     }
     

**Rectification guide**:

Check whether the code described in the preceding scenarios exists. If yes, modify the code.

-   **Checking whether the script has the risk of Trojan horses**

**Scenario**:

1.  The machine learning model detects that the script has the risk of Trojan horses.

**Rectification guide**:

Avoid code confusion. If the character string is too long, a Trojan horse alarm is generated on the web page.

-   **Checking whether the script contains suspected mining code**

**Scenario**:

1.  A mining domain name (such as **coinhive.com** and **minecrunch.co**) exists.
2.  The machine learning model detects that the script contains mining code.

**Rectification guide**:

Check whether the mining domain name exists. If yes, modify it.

**Tool supported or not**: yes

**Specification name**: Security\_MaliciousOperations\_Forbid\_JavaScipt\_DaggerCommand

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: all

**Parent topic:** [[Protection Against Malicious Operations|Protection Against Malicious Operations]]