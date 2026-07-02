---
title: "Common Components"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_page_js_003.html"
depth: 7
---
#### Form Panel Components

// Method for verifying the entire form
// **copyForm** is the form component ID.
// **result**: indicates the verification result. **object**: indicates the component information when the verification fails.
S("copyForm").validate(function (result, object) {
    if (result) {
         //The verification is successful.
    } else {
         //The verification fails.
    }
})
// Method for verifying a single field in the form
S("copyForm").validateSingleField("name");