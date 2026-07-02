---
title: "Configuring Template-Level Studio"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_project_052.html"
depth: 5
---
# Configuring Template-Level Studio

You can define whether to display elements of the Studio, such as the logo, menu, navigation, and help menu, in the template. For a project created based on this template, the Studio page is generated according to the setting in this template.

**Table 1** Studio configuration    
| Configuration Level | Operator | Configuration Method | Validation Range |
| :-- | :-- | :-- | :-- |
| Tenant | Tenant administrator | Menu configuration | The configuration takes effect within a tenant and takes effect only in projects created using a blank template. |
| Template | Template developer | Offline editing of the template definition file | The configuration takes effect only in projects created using this template. The priority of the template level is higher than that of the tenant level. That is, during project creation, when the display elements defined in the template are different from those configured using the tenant level configuration method, the project template definition is used. | To configure a template, you need to manually edit the **template.json** project template file. The following is an example:

{
  "scene\_name" : "custom",
  "description" : null,
  "name\_i18n" : null,
  "i18ns" : null,
  "preview\_picture\_names" : null,
  "develop\_default\_home\_page" : null,
  "develop\_welcome\_page" : null,
  "version" : "0.0.1",
  "menus" : \[
    {
        "name": "logo",
        "enabled": true
    },
    {
        "name": "left-menus",
        "enabled": true
    },
    {
        "name": "bottom-tool",
        "enabled": true,
        "children": \[
            {
                "name": "quality-monitor",
                "enabled": true
            },
            {
                "name": "project-modify-history",
                "enabled": true
            },
            {
                "name": "runtime-log",
                "enabled": true
            }
        \]
    },
    {
        "name": "project-navigation",
        "enabled": true
    },
    {
        "name": "helps",
        "enabled": true
    },
    {
        "name": "top-tool",
        "enabled": true,
        "children": \[
            {
                "name": "search-globally",
                "enabled": true
            },
            {
                "name": "go-to-runtime-state",
                "enabled": true
            },
            {
                "name": "view-resources",
                "enabled": true
            },
            {
                "name": "import-asset",
                "enabled": true,
                "children": \[
                    {
                        "name": "import-module",
                        "enabled": true
                    },
                    {
                        "name": "import-component",
                        "enabled": true
                    },
                    {
                        "name": "view-service-component",
                        "enabled": true
                    },
                    {
                        "name": "import-legacy-asset",
                        "enabled": true
                    }
                \]
            },
            {
                "name": "packing",
                "enabled": true,
                "children": \[
                    {
                        "name": "app",
                        "enabled": true
                    },
                    {
                        "name": "upgrade-package",
                        "enabled": true
                    },
                    {
                        "name": "project-package",
                        "enabled": true
                    },
                    {
                        "name": "project-template",
                        "enabled": true
                    },
                    {
                        "name": "service-component-copy",
                        "enabled": true
                    },
                    {
                        "name": "service-component-run",
                        "enabled": true
                    },
                    {
                        "name": "packing-history",
                        "enabled": true
                    }
                \]
            },
            {
                "name": "deployment",
                "enabled": true,
                "children": \[
                    {
                        "name": "one-click-deployment",
                        "enabled": true
                    },
                    {
                        "name": "customized-deployment",
                        "enabled": true
                    },
                    {
                        "name": "deployment-configuration",
                        "enabled": true
                    }
                \]
            }
        \]
    }
\]
}

**Parent topic:** [[Managing Project Templates|Managing Project Templates]]