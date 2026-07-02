---
title: "How Do I Configure a Customized Property Editor for a Property During Customized Component Development?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_035.html"
depth: 7
---
#### Procedure

1.  Declare a property as a customized property, which is similar to the configuration of the customized property. The difference is that the specified type is **INPUT\_TYPE.CUSTOM\_PROPERTY**. An example is as follows:
    
    property(
          basic({
            name: "gradeclass",
            //Specify the type of the customized property.
            type: INPUT\_TYPE.CUSTOM\_PROPERTY,
            defaultValue: "",
           //Specify the name, which must be the same as the value of **name** in the Vue file for the customized property. The customized property component is registered globally. Therefore, ensure that the name is unique.
            parameters: { name: \`${pJson.name}GradeClass\` }
          })
        )
    
2.  Develop the Vue file for customized properties. For details, see the preceding scaffolding directory description, especially the **src\\component\\designer\\property-editor** directory. The customized property component needs to be registered in the **index.js** file in the directory. The file will be loaded when the customized component is dragged to the page.
    
    **Figure 1** property-editor example  
    ![[en-us_image_0000001473820868.png]]
    
3.  For the customized property component file, specify **props** to fix the three properties to values same as those of the customized property **Editor**.
    
    **Table 1** Property description  
    | Property | Description |
    | :-- | :-- |
    | value | Current property value |
    | validation | Configurations related to the developer-defined validation |
    | parameters | Parameters defined when developers define properties | props: {
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
    
4.  When developing a customized dialog box property **Editor**, interact with the designer. By default, events are provided for interaction with the framework.
    
    -   Sending the validate event to the parent component (framework): The business side customizes the validation logic and returns the validation result to the parent component through this event. If the validation result is pass, **true** is returned. Otherwise, a validation message is returned.
    -   Sending the value-change event to the parent component (framework): This event is used to return the property value to the parent component, and then the parent component transfers the property value to the visualization area (middle canvas) for data update.
    
    Sample code:
    
    <template>
      <div class="custom-editor">
        <el-input v-model="currentVal" placeholder="" @change="handleValueChange"></el-input>
      </div>
    </template>
    
    <script>
    const pJson = require("../../../../package.json");
    export default {
      name: \`${pJson.name}CustomEditor\`,
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
          currentVal: ""
        };
      },
      watch: {
        value: {
          immediate: true,
          handler(newVal) {
            this.currentVal = newVal;
          }
        }
      },
      methods: {
        validate() {
          if (this.currentVal == "") {
            return "Mandatory";
          }
          return true;
        },
        handleValueChange() {
          let valid = this.validate();
          if (valid == true) {
            this.$emit("value-change", this.currentVal);
          } else {
            this.$emit("validate", valid);
          }
        }
      }
    };
    </script>
    <style lang="less"></style>
    
5.  After the customized property **Editor** is developed, perform the preceding steps to complete the debugging and validation.