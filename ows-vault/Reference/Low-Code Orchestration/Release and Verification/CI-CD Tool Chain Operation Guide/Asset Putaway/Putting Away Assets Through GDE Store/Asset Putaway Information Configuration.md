---
title: "Asset Putaway Information Configuration"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001829194741.html"
depth: 5
---
# Asset Putaway Information Configuration

1.  Choose **GDE Store** > **Putaway** and configure the asset putaway information on the displayed page.
    
    **Figure 1** Basic information and asset putaway information  
    ![[en-us_image_0000001829074893.png]]
    
    **Table 1** Parameters in the Basic Info and Putaway Info areas  
    | Parameter | Description |
    | :-- | :-- |
    | Asset Name | Name displayed on GDE Store, which can be modified only when the asset is put away for the first time. |
    | Putaway Version | Version of the asset that is successfully packaged. |
    | Technical Support | Set this parameter based on the actual service content. A maximum of five lines are allowed, and each line contains a maximum of 300 characters. An example is as follows: Service time: 9:00-18:00 Service content: hotline support, remote services, on-site maintenance, and training services Service hotline: 12345678 Service email: xx@xx.com |
    | Developer Type | This parameter is displayed by default and cannot be modified. |
    | Developer Info | This parameter is displayed by default and cannot be modified. |
    | Asset Type | Asset category. You can select only one option. |
    | Business Domain | There are sub-business domains under the business domain. You can select only one option. |
    | Deployment Mode | Asset delivery type. You can select only one option.
    -   **SaaS**: online app software deployed on cloud-based infrastructure resources
    -   **License**: app software or BuildingBlock that can be used only after being downloaded and deployed
    -   **API**: API service of the software system deployed on cloud-based infrastructure resources
    
     |
    | Custom Label | List of asset labels added by a developer. Multiple labels are separated with commas (,). Each label contains a maximum of 64 characters. A maximum of 16 labels are supported. | **Figure 2** Asset description  
    ![[en-us_image_0000001829194941.png]]
    
    **Table 2** Parameters in the Asset Introduction area  
    | Parameter | Description |
    | :-- | :-- |
    | LOGO | Asset icon. Only one image in JPG, PNG, or JPEG format is supported. The size of a single image must be less than 50 KB, and the recommended size is 64 px x 64 px to 90 px x 90 px. |
    | background Image | Only one image in JPG, PNG, or JPEG format is supported. The size of a single image must be less than 200 KB and the recommended size is 310 px x 120 px. |
    | Homepage Image | Only one image in JPG, PNG, or JPEG format is supported. The size of a single image must be less than 500 KB and the recommended size is 660 px x 430 px. |
    | Introduction | A maximum of 100 characters are supported. This parameter is mandatory. |
    | Asset Description | Asset description. |
    | Dev Tutorial | Asset development tutorial. |
    | Sample | Asset sample description. |
    | Help Document | Only one ZIP file can be uploaded. The total file size cannot exceed 100 MB. |
    | Open Source Software Statement | You need to truthfully state the open source software usage of the asset in Open Source Software Statement. If no open source software is used, select N/A. The .zip format is supported, and the size cannot exceed 20 MB. | **Figure 3** Offering information  
    ![[en-us_image_0000001782515154.png]]
    
    **Table 3** Parameters in the Offering Information area  
    | Parameter | Description |
    | :-- | :-- |
    | Main Image | Images in JPG, PNG, JPEG, or GIF format are supported. A maximum of five files can be uploaded. The size of each file must be less than 5 MB. The recommended size is 800 px x 600 px. This parameter is mandatory. |
    | Highlight | Offering highlight. Each highlight occupies a line. A maximum of five highlights can be added. Each highlight can contain a maximum of 100 characters. |
    | Customer Case | Successful customer cases of the released version. If a success case is provided, describe it in detail rather than fill in only one success case name. |
    | Content Agreement | Product service agreement, which contains a maximum of 200,000 characters. This parameter is mandatory. |
    | Copyright | Only one ZIP file can be uploaded. The total file size cannot exceed 100 MB. | **Figure 4** Version update  
    ![[en-us_image_0000001782355490.png]]
    
    **Table 4** Parameters in the Explanation of version update area  
    | Parameter | Description |
    | :-- | :-- |
    | Putaway Description | Asset putaway description. |
    | Add Images | A maximum of five files in JPG, PNG, or JPEG format can be uploaded, and the size of each file cannot exceed 500 KB. | 2.  Click **Preview** to preview the parameter settings.
3.  Click **Confirm** to go to the putaway process.

**Parent topic:** [[Putting Away Assets Through GDE Store|Putting Away Assets Through GDE Store]]