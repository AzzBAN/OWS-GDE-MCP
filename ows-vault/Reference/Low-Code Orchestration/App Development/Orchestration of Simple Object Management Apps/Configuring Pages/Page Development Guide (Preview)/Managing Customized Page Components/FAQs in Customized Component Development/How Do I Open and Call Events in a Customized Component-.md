---
title: "How Do I Open and Call Events in a Customized Component?"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_034.html"
depth: 7
---
#### Procedure

1.  Open events for a customized component by referring to the following sample code:
    
    this.getEventBus().fireEvent(this.id, "value-change", params);
    
2.  In the SPL, use JavaScript to listen to the corresponding event. The sample code is as follows:
    
    Nf.ready(function(){
         Spl.EventBus.register("id","value-change",function(params){
             console.log(params)
       })
    })