---
title: "Modifying a Data Model"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/datamodel_004.html"
depth: 5
---
#### Context

After a model is created in the develop-state environment, you can modify the model on the develop-state page. For example, the property display name of a model can be modified after the model is created, but the property name of a model cannot be modified after the model is created.

After a model is created in the runtime state, you can modify the model in the runtime state through upgrade after the application is deployed.

The constraints in the develop-state environment are different from those in the runtime-state environment. When the modification in the develop-state environment is not allowed in the runtime-state environment, the app upgrade may fail in the runtime-state environment.

In the development and debugging phase, the modification in the develop-state environment is allowed. After the modification in the develop-state environment is made, the apps in the runtime-state environment can be uninstalled and then deployed and debugged.

**Table 1** Constraints on modifying basic information about model properties   
| Field Name | Whether Modification Is Allowed in the Develop-State Environment | Whether Modification Is Allowed in the Runtime-State Environment |
| :-- | :-- | :-- |
| Property Name | Forbid | Forbid |
| Display Name | Allow | Allow |
| Default Value | Allow | Allow |
| Description | Allow | Allow |
| Primary Key | Forbid | Forbid |
| Type | Allow | The constraints vary depending on different property types that can be modified. For details, see Table 2. |
| Mandatory | Allow | Allow: Yes -> No Allow: No -> Yes; add a property; with the default value. Not allow: without the default value |
| Property constraints (other property information) | Allow | For details about restrictions on model property modification, see Table 3. | **Table 2** Runtime-state property types that can be modified  
| Source Property Type | Type That Can Be Modified to |
| :-- | :-- |
| Sequence | Text Constraints: Modification is supported when Max. Length of the modified text type is greater than or equal to 250. |
| Integer | None |
| Decimal | None |
| Date | Text Constraints: Modification is supported when Max. Length of the modified text type is greater than or equal to 250. |
| Time | Text Constraints: Modification is supported when Max. Length of the modified text type is greater than or equal to 250. |
| Date and Time | None |
| Timestamp | Integer |
| Reference | Text |
| File | None |
| User | None |
| User Group | None |
| Password | None |
| Enumeration | Text Constraints: Modification is supported when Max. Length of the modified text type is greater than or equal to 250. |
| Boolean | None | **Table 3** Restrictions on modifying properties of a model in the runtime state      
| Property Type | Property Constraint (Other Property Information) | Description | Mandatory | Value | Modification Constraint |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Sequence | Sequence | Sequence Type | Y | date time sequence, UUID, distributed time sequence | DUTS/UUID/DAIS Modification is not allowed. |
| Sequence format | Serialization format | Y | Format example: {YYYY}-{MM}-{DD}-{0000} | Format example: {YYYY}-{MM}-{DD}-{0000} Modification is not allowed. |
| Text | Max. Length | Maximum length | Y | Value range: \[1,4000\]. The default value of Max. Length is 250. You can change the value. If an index has been configured, the value of Max. Length cannot exceed 250. | The length can be changed to a larger value, but cannot be changed to a smaller value. |
| Special character | Special characters are not allowed. | N | Special character | Modification is allowed. |
| Integer | None | \- | \- | \- | \- |
| Decimal | None | \- | \- | \- | \- |
| Date | None | \- | \- | \- | \- |
| Time | None | \- | \- | \- | \- |
| Date and Time | None | \- | \- | \- | \- |
| Timestamp | Timestamp | Timestamp precision | Y | s, ms | Modification is not allowed. |
| Reference | Reference Model | Associated model | Y | Input constraint: Reference Model | Modification is not allowed. |
| Reference Operation | Associated action | Y | Forbid Delete, Clean Field, Cascading Delete | Modification is allowed. |
| File | File Type | File type | N | \- | Modification is allowed. |
| Max. File Size (KB) | File size limit | N | \- | Modification is allowed. |
| User | None | \- | \- | \- | \- |
| User Group | None | \- | \- | \- | \- |
| Password | Password format | Password policy | Y | AES/SHA256 | Modification is not allowed. |
| Enumeration | None | \- | \- | \- | \- |
| Boolean | None | \- | \- | \- | \- |