---
title: "Rule: U.escapeHtml() Must Be Used to Encode Code Concatenated to Pages to Prevent XSS Injection Attacks"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208599061.html"
depth: 5
---
# Rule: U.escapeHtml() Must Be Used to Encode Code Concatenated to Pages to Prevent XSS Injection Attacks

**Description**: The validator and translator provided by GDE cannot cover the character string concatenation in the JS component of the page. If developers use input data of untrusted sources (for example, data entered by users on the page) as the page content and directly display it in HTML format, XSS injection may occur.

**Check guide**: Log in to the develop-state system and select the asset to be checked.

1\. Check the JS script in the page script one by one to check whether there is code that is concatenated and displayed in HTML format.

2\. Check the page scripts one by one. If the htmlPanel and cardgrid components are used, check whether the value assignment of the components is encoded.

**Positive example**: The text value obtained from the input is encoded using the U.escapeHtml() method and then is assigned with a value and then displayed on the page as HTML content. Not all value assignment modes are included. The principle is that encoding is required when parameters are directly read from the page or parameter values are assigned at the back end and then displayed on the page, as described in the following example:

var sampleHtml = $("#content").val();

Encoding mode:

var escapeHtml = U.escapeHtml(sampleHtml);

The following is an example of the scenario where encoding output is required:

$("#sampleDisplay").html(escapeHtml);

$("#sampleDisplay ").val(escapeHtml);

$("# sampleDisplay ").attr("value", escapeHtml);

document.getElementById('sampleDisplay').innerText='Assign a value to an HTML page.';

document.getElementById('sampleDisplay').innerHTML='Assign a value to an HTML page.';

**Negative example**:

var sampleHtml = $("#content").val();

$("#sampleDisplay").html(sampleHtml);

**Noe:** The preceding example does not list all page element operation methods and is for reference only. This rule focuses on whether to use frontend input to display a page.

**Tool supported or not**: yes

**Specification name**: Security\_DataCheck\_Page\_JavaScript\_NoEncode

**Category**: non-bottom-line check item

**Severity**: major

**Orchestration scenario**: UI orchestration

**Parent topic:** [[Data Verification|Data Verification]]