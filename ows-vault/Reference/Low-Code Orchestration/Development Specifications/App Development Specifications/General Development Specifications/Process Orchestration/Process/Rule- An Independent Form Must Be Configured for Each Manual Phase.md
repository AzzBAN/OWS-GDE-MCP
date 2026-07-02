---
title: "Rule: An Independent Form Must Be Configured for Each Manual Phase"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399363517.html"
depth: 6
---
# Rule: An Independent Form Must Be Configured for Each Manual Phase

**Description**:

1\. A form (PC or mobile form page) must be configured for each manual phase. Otherwise, a ticket cannot be submitted because no information can be entered when the ticket is transferred to a manual phase.

2\. An independent form must be configured for each manual phase. To prevent interference or conflicts, different phases cannot reference the same form page.

**Check guide**:

1\. Select a phase in the process diagram and select **Form** from the shortcut menu to open the form page.

![[en-us_image_0000002194366441.png]]

2\. On the displayed form page, check whether fields are configured in the middle form.

The following pages are for reference only. Configure the required fields and components based on site requirements.

![[en-us_image_0000001520451257.png]]

3\. Check whether the same form page is referenced by other phases based on the page name to prevent interference or conflicts.

**Positive example**:

A form is configured for a manual phase in the process and can be used only by the manual phase.

**Negative example**:

No form is configured for a manual phase in the process, or the same form page is used by multiple phases or processes.

**Tool supported or not**: no

**Specification name**: General\_Process\_Config\_Independent\_Form\_For\_Manual\_Phase

**Severity**: major

**Parent topic:** [[Process|Process]]