---
title: "How Do I Open and Call APIs in a Customized Component?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_033.html"
depth: 7
---
#### Procedure

1.  To open APIs for a customized component, define the corresponding method or logic in the methods of the customized component. The following shows a configuration example.
    
    methods: {
        getDateTip() {
          const \_this = this;
          \_this.startDate = this.$t("timeRangePicker.startDate");
          \_this.endDate = this.$t("timeRangePicker.endDate");
        },
        setValue(newValue) {
          this.innerValue = newValue;
        },
        getValue() {
          return this.innerValue;
        },
        getValidation: function () {
          var validation = {
            id: this.id,
            required: this.required === true,
            type: "text",
            whenHiddenSkipCheck: this.whenHiddenSkipCheck === true,
            dataField: this
          };
          return validation;
        }
      },
    
2.  During SPL page orchestration, use the S("id").getValue() method to call the getValue method provided by the customized component.