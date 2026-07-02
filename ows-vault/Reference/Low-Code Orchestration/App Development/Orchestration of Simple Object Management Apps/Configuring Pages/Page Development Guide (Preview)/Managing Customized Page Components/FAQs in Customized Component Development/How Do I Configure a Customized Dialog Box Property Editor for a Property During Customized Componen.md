---
title: "How Do I Configure a Customized Dialog Box Property Editor for a Property During Customized Component Development?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_036.html"
depth: 7
---
#### Procedure

1.  Declare a property as a customized property, which is similar to the configuration of the customized property. The difference is that the specified type is **INPUT\_TYPE.CUSTOM\_POPOVER\_PROPERTY**. An example is as follows:
    
    property(
          basic({
            name: "customPopoverEditor",
            //Specify the type of the customized dialog box.
            type: INPUT\_TYPE.CUSTOM\_POPOVER\_PROPERTY,
            defaultValue: "",
            parameters: {
              name: \`${pJson.name}CustomPopoverEditor\`, //Specify the name, which must be the same as the value of **name** in the Vue file for the customized property. The customized property component is registered globally. Therefore, ensure that the name is unique.
              promptWidth: "800px",  //Width of the dialog box
              promptMaxHeight: "500px", //Maximum height of the dialog box
              showPromptButton: false //Whether to display the default button in the dialog box. This parameter is valid for the dialog box property **Editor**. The default value is **true**.
            }
          }),
          validation({ required: true, maxLength: 50, minLength: 1 })
        )
    
2.  Develop the Vue file for customized properties. For details, see the preceding scaffolding directory description, especially the **src\\component\\designer\\property-editor** directory. The customized property component needs to be registered in the **index.js** file in the directory. The file will be loaded when the customized component is dragged to the page.
    
    **Figure 1** property-editor example  
    ![[en-us_image_0000001524661521.png]]
    
3.  For the customized property component file, specify **props** to fix the three properties to values same as those of the customized property **Editor**.
4.  When developing a customized dialog box property **Editor**, interact with the designer. By default, events are provided for interaction with the framework.
    
    1.  The customized dialog box property **Editor** determines whether to use the default button (configured using **showPromptButton**) in the dialog box. If **showPromptButton** is set to **false**, the default button in the dialog box is not used. That is, the **OK** and **Cancel** buttons in the dialog box are customized by the business side who triggers the event according to the logic.
        
        -   Sending the validate event to the parent component (framework): The business side customizes the validation logic and returns the validation result to the parent component through this event. If the validation result is pass, **true** is returned. Otherwise, a validation message is returned.
        -   Sending the value-change event to the parent component (framework): This event is used to return the property value to the parent component, and then the parent component transfers the property value to the visualization area (middle canvas) for data update.
        -   Sending the close event to the parent component (framework): This event is used to close the dialog box and applies to customized dialog box properties and the scenario where the value of **showPromptButton** is **false**.
        
        Sample code:
        
        <template>
          <div class="custom-popover-editor">
            <el-form label-width="120px" :model="val">
              <el-form-item label="ID">
                <el-input v-model="val.id" placeholder=""></el-input>
              </el-form-item>
              <el-form-item label="Name">
                <el-input v-model="val.name" placeholder=""></el-input>
              </el-form-item>
            </el-form>
            <div class="btn-group">
              <el-button @click="\_onCancel">{{ $t("customPopoverEditor.cancel") }}</el-button>
              <el-button type="primary" @click="\_onSave">{{ $t("customPopoverEditor.save") }}</el-button>
            </div>
          </div>
        </template>
        
        <script>
        const pJson = require("../../../../package.json");
        export default {
          name: \`${pJson.name}CustomPopoverEditor\`,
          props: {
            value: {
              type: String,
              default: ""
            },
            validation: {
              type: Object,
              default: function () {
                return {};
              }
            },
            parameters: {
              type: Object,
              default: function () {
                return {};
              }
            }
          },
          data() {
            return {
              val: {
                id: "",
                name: ""
              }
            };
          },
          watch: {
            value: {
              immediate: true,
              handler(newVal) {
                if (newVal) {
                  this.val = JSON.parse(newVal);
                }
              }
            }
          },
          methods: {
            //Triggering method of the default dialog box button
            validate() {
              let currentVal = JSON.stringify(this.val);
              if (currentVal.length > 30) {
                return "The maximum length is 30 characters."
              }
              return true;
            },
            getValue() {
              return JSON.stringify(this.val);
            },
            //Triggering method of a customized property button
            \_onSave() {
              let valid = this.validate();
              if (valid == true) {
                this.$emit("value-change", JSON.stringify(this.val));
              } else {
                this.$emit("validate", valid);
              }
            },
            \_onCancel() {
              this.$emit("close");
            }
          }
        };
        </script>
        <style lang="less"></style>
        <i18n>
        {
          "en-US": {
            "customPopoverEditor": {
              "save": "Save",
              "cancel": "Cancel"
            }
          },
          "en\_US": {
            "customPopoverEditor": {
              "save": "Save",
              "cancel": "Cancel"
            }
          }
        }
        </i18n>
        
    2.  The customized dialog box property **E****ditor** determines whether to use the default button (configured using **showPromptButton**) in the dialog box. If **showPromptButton** is set to **true**, the default button in the dialog box is used. In this case, the business side does not need to trigger any event. Only the **validate** and **getValue** methods need to be provided. The implementation of the **validate** method is the same as that of the validate event. The **getValue** method is used to return all property values in the dialog box in JSON string format. The two methods are automatically called by the parent component.
        
         validate() {
              let currentVal = JSON.stringify(this.val);
              if (currentVal.length > 30) {
                return "The maximum length is 30 characters."
              }
              return true;
            },
            getValue() {
              return JSON.stringify(this.val);
            },
        
    
5.  After the customized property **Editor** is developed, perform the preceding steps to complete the debugging and validation.