---
title: "Chart Components"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_echart_001.html"
depth: 5
---
# Chart Components

-   In addition to common page configuration capabilities, the system provides chart components for you to configure various charts.
    
    **Figure 1** Chart components  
    ![[en-us_image_0000001166930524.png]]
    
    **Table 1** Component properties  
    | Name | Description |
    | :-- | :-- |
    | Id | Component ID, which can be internationalized. |
    | Sub Type | Component subtype. You can set different subtypes for different components. This parameter may not be displayed because some components do not need to be configured with subtypes. |
    | Configuration | ECharts configuration. |
    | Interface Input Parameter | The chart component can use static simulation data or service data. | -   When using chart components, you need to set the ECharts parameter. After dragging a chart component to the canvas, you need to open the configuration window in the property configuration area on the right to configure the chart component.
    
    ![[en-us_image_0000001166612038.png]]
    
-   The root nodes of ECharts are dataSources, jsLibs, options, Listeners, and autoRefresh. For details about how to configure these nodes, see the following sections.
-   On the **Script** tab page of the ECharts chart, you can configure data and styles using scripts to implement higher-level and more flexible chart configuration. For example, you can configure a gauge chart using the following scripts.
    
    ![[en-us_image_0000002491112476.png]]
    
    this.echarts.options.series\[0\].axisLine.lineStyle.color = \[\[2, "#efefef"\]\];
    this.on("beforeInit", function (params) {
        params.widget.echarts.options.series\[0\].progress = {
            javaClass: "com.huawei.ows.visualscript.dsl.echarts.options.series.gauge.Progress",
            show: true,
            overlap: false,
            roundCap: true,
            clip: false,
            itemStyle: {
                borderWidth: 1,
                borderColor: "#464646"
            }
        }
        params.widget.echarts.options.series\[0\].data = \[{
            value: 120,
            name: "Example1",
           title: {
               fontSize: 12,
                offsetCenter: \["-80%", "120%"\]
            },
            detail: {
                offsetCenter: \["-115%", "120%"\]
            }
        },
        {
            value: 90,
            name: "Example2",
            title: {
                fontSize: 12,
                offsetCenter: \["0%", "120%"\]
            },
            detail: {
                offsetCenter: \["-35%", "120%"\]
     }
        },
        {
            value: 46,
            name: "Example3",
            title: {
                fontSize: 12,
                offsetCenter: \["80%", "120%"\]
            },
            detail: {
                offsetCenter: \["45%", "120%"\]
            }
        }
        \]
        params.widget.echarts.options.series\[0\].detail = {
            width:-6,
            fontSize: 0,
            height:4,
            backgroundColor: "auto",
            color: "auto",
            borderRadius: 9
        }
        var length = params.widget.echarts.options.series\[0\].data.length;
        var sum = 0;
        for (var j = 0; j < length; j++) {
            sum += params.widget.echarts.options.series\[0\].data\[j\].value
        }
        params.widget.echarts.options.series\[0\].max = sum
        params.widget.echarts.options.graphic = \[{
            type: "text",
            left: "center",
            top: "center",
            style: {
                text: sum,
                textAlign: "center",
                fill: "#010101",
                fontSize: 28,
                fontWeight: "600"
            }
        }, {
            type: "text",
            left: "center",
            top: "55%",
            style: {
                text: "Total (TB)",
                textAlign: "center",
                fill: "#010101",
                fontSize: 14
            }
        }
        \]
    });
    
-   Different chart components support different events and methods. For details, see the online help of the corresponding chart component on the page.
    
    ![[en-us_image_0000002446888085.png]]
    

**Parent topic:** [[Configuring a Chart Page|Configuring a Chart Page]]