---
title: "Managing Labels"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/assetmgt_002.html"
depth: 3
children: ["Managing Service Domain Labels", "Managing Asset Catalog Labels", "Associating Technical Category Label", "Selecting Assets by Category Label"]
---
#### Context

   
| Label | Customizable | Description | Applicable Scenario |
| :-- | :-- | :-- | :-- |
| Service Domain | Some labels can be customized. | Labels in the Custom directory can be customized. These labels are used to categorize customized domains for tenant asset management. | When you put away assets from the ADC pipeline to the asset management module, select labels from the Custom directory when you configure Domain. |
| Asset Type/Asset Catalog | 
-   Types of assets that have been put away cannot be customized.
-   Catalogs of local assets can be customized.

 | -   Labels of putaway assets: Asset type labels obtained from GDE Store are synchronized to the **Asset Type** directory.
-   Customizable labels in local assets: Labels in the **Custom** directory are customized categories of domains in tenant asset management and can be customized by users.

 | -   When packaging assets in the ADC develop-state environment, you can select the corresponding asset catalog. After the assets are packaged, the assets of the specified type are displayed on the **Asset Management** page.
-   When you put away assets from the ADC pipeline to the asset management module, you can select labels from the **Putaway Assets** directory when configuring **Asset Type**.

 |
| Technology Category | A category cannot be customized but can be associated with an asset catalog. | You can associate a label with a specific technology category in the Asset Catalog area. | An asset catalog can be associated with different technical categories. For example, if an asset catalog is associated only with a project package, this asset catalog can be selected only when the project package is packaged. |
| Customized Label | Customized category. | -   Customized label added during project creation.
-   Asset label added by a developer during asset putaway.

 | An asset category can be defined by users. |

## Sub-topics

- [[Managing Service Domain Labels]]
- [[Managing Asset Catalog Labels]]
- [[Associating Technical Category Label]]
- [[Selecting Assets by Category Label]]
