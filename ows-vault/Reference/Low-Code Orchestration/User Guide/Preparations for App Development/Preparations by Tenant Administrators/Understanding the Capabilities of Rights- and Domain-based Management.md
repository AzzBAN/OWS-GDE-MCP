---
title: "Understanding the Capabilities of Rights- and Domain-based Management"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_dev_overview_009.html"
depth: 4
---
# Understanding the Capabilities of Rights- and Domain-based Management

ADC supports rights- and domain-based management. Projects are managed by their open levels such as personal, team, and whether the project is public, implementing hierarchical permission control.

-   **Personal**: Only the project creator and specified users have the permission to view the project. Other users under the tenant cannot view the project. You can manage members of a personal project and add other members to edit and develop the project.
-   **Team**: Only members in a specified team can access the project. Non-team members do not have the permission to view the project.
-   **Public**: The project can be accessed by all users under a tenant.

**Table 1** Rights- and domain-based management description   
| Project Open Level | Permission Description | Member Permission |
| :-- | :-- | :-- |
| Personal | Only the project creator and specified members can access the project. Other personnel of the tenant do not have the permission to view the project. | Member roles of a personal project:
-   **Project Developer**: performs orchestration and development only in the project. NOTE: This role provides all capabilities in an AI orchestration project, except Review Labeling Task, View Labeling Task, and Create Labeling Task in the dataset.
-   **Project Maintainer**: modifies a project and adds, deletes, and changes the personnel who can access the project. NOTE: This role provides all capabilities in an AI orchestration project.

 |
| Team | Only members in a specified team can access the project. Non-team members do not have the permission to view the project. | Team member roles:

-   Team administrator: adds maintenance team members and orchestrates projects in the team.
-   Team developer: orchestrates team projects. The role cannot add maintenance team members.

 |
| Public | All users in the tenant can use the project. | Member management is not required. | ![[notice_3.0-en-us.png]]

The **Develop Asset Management** permission is preset in the system. In addition to other necessary orchestration permissions, this permission allows users to perform operations such as project, team, and member management on personal- and team-level projects. That is, the **Develop Asset Management** permission is beyond the rights- and domain-based management permission.

By default, only the administrator has the **Develop Asset Management** permission. If the administrator assigns this permission to another role, users of this role share this permission. Therefore, exercise caution when performing this operation.

**Figure 1** Asset development and management permissions  
![[en-us_image_0000001579185004.png]]

After a project is created, only the following users can modify the project sharing scope and asset sharing scope:

-   Users who have the **Develop Asset Management** permission
-   Personal project creator
-   Personal project manager
-   Team creator of a team project
-   Team manager of a team project
-   Creator of a public project

**Parent topic:** [[Preparations by Tenant Administrators|Preparations by Tenant Administrators]]