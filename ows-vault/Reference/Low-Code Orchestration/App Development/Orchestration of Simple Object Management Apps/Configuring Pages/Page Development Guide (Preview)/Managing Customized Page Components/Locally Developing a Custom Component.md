---
title: "Locally Developing a Custom Component"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_procode_page_029.html"
depth: 6
---
#### Description of the Custom Component Code Project

Use the scaffolding tool to generate a custom component code project in one-click mode. The project directory is as follows:

no-code-pkgs //Custom component name
├─.browserslistrc
├─.editorconfig
├─.eslintignore
├─.eslintrc.js
├─.lintstagedrc
├─.prettierrc
├─.stylelintrc
├─adcui.json           //Define the custom component type and the address of the third-party library on which the custom component depends.
├─babel.config.js
├─package-lock.json
├─package.json 
├─postcss.config.js
├─src                 //Main development directory
| ├ ─packages/_{Component name}_
|  ├─document         //Usage guide in develop state
|    |      |    ├─en.md      //Component usage guide in English
|    |      |    └zh\_CN.md      //Component usage guide in Chinese
|    |      ├─config
|    |      |   ├─index.js     //Configuration of open properties of the custom component in develop state
|    |      |   └locale.js      //Internationalization definition of the custom component in develop state
|    |      ├─component       
|    |      |     ├─runtime  
|    |      |     |    └index.vue  // Component definition entry in runtime state
|    |      ├─assets              //Icon used in develop state
|    |      |   └icon.png
├─node\_modules                 // 
├─example                //Sample component preset in the custom component
|    ├─example-step
|    |      ├─src
|    |      |  ├─config
|    |      |  |   ├─index.js
|    |      |  |   └locale.js
|    |      |  ├─component
|    |      |  |     ├─runtime
|    |      |  |     |    ├─index.vue
|    |      |  |     ├─designer
|    |      |  |     |    ├─property-editor
|    |      |  |     |     |    ├─custom-editor.vue  //custom-editor.vue //Vue entry file for the custom property. The file name can be customized and can be configured based on the code in the **index.js** file.
|    |      |  |     |     |    ├─custom-popover-editor.vue  //Vue file for the custom dialog box property. The file name can be customized and can be configured based on the code in the **index.js** file.
|    |      |  |     |     |    ├─index.js   //Entry file of custom property configurations
├─document               //Open document of the custom component
|    ├─1.designerAndruntime.md
|    ├─2.debuggingAndDevelopment.md
|    ├─3.componentNesting.md
|    └README.md
├─build                  //Package the compilation script.
├─adaptor                //Encapsulated component definition method and constant, which are used by compilation developers

1.  Description of the **adcui.json** file
    
    {
      "type": "nocode", //Custom component that is identified
     "javascriptLibraryDependencies":\[{"src":"xxxx"}\]  //Depended third-party component, which is associated with the third-party library provided by the UI
    }
    
2.  Configuration description of open properties of custom components in develop state (path: **src/packages/**_{Component name}_**/config/index.js**)
3.  Internationalization definition of the custom component displayed in develop state (path: **src/packages/**_{Component name}_**/config/locale.js**)
4.  Entry for defining components in runtime state (path: **src/packages/**_{Component name}_**/component/runtime/index.vue**)
    -   The scoped style is strongly recommended to avoid affecting other components.
    -   The component must support internationalization switching.
    -   Currently, the development of custom components mainly depends on the Vue custom component capability. Based on the encapsulation of custom component capabilities, the intuitive configuration and dynamic loading of custom components are provided. For details, see [Vue official website](https://v2.vuejs.org/v2/guide/components.html). The difference between the custom component and Vue custom component is that global custom components, for example, Vue.component("custom-component",componentConfig), are dynamically registered using the framework during running