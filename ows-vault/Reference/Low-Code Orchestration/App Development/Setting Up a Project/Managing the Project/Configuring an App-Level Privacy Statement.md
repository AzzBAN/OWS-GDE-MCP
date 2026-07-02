---
title: "Configuring an App-Level Privacy Statement"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_053.html"
depth: 4
---
#### Context

When an app needs to collect end users' privacy data, a privacy statement needs to be provided to declare the user information to be collected, information usage, and protection measures for user information. The app can be used only after users' consent is obtained.

For example, the member information management system needs to collect member information, the book borrowing registration system needs to collect reader information, and the business trip reimbursement system needs to collect the bank account information and business trip schedule of the reimbursement personnel. Such apps can be used only after the privacy statement is displayed to the user and the user's consent is obtained.

ADC allows developers to configure privacy statements on the develop-state environment and displays privacy statements to end users on the runtime-state environment.

-   The privacy statement can be configured on the web client to adapt to the scenario where users use apps on PC web pages.
-   The privacy statement can be configured on the mobile client to adapt to the scenario where users use apps through GDELink.

![[note_3.0-en-us.png]]

-   If both the web client and mobile client are used, you need to configure privacy statements for the two types of clients separately.
-   The privacy statement configured in a project is a part of the tenant privacy statement. Configure the privacy statement only when the project involves user privacy data operations. The privacy statement must accurately describe the types, purposes, handling methods, time limits, and rights of data subjects of all the personal data. Ensure that the privacy statement complies with local laws and regulations and has been reviewed by legal affairs personnel.