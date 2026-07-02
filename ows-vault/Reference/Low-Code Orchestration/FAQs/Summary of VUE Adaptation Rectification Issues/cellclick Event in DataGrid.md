---
title: "cellclick Event in DataGrid"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002365500900.html"
depth: 3
---
# cellclick Event in DataGrid

You need to perform the following adaptation rectification in the versions using VUE:

//Original registration method
 S('datagrid').getGrid().on('cellclick', function(grid, rowIndex, columnIndex, e)
 //Current registration method
 Spl.EventBus.register("datagrid", "cellclick", function(id, row, column, cell, event){});

**Parent topic:** [[Summary of VUE Adaptation Rectification Issues|Summary of VUE Adaptation Rectification Issues]]