---
title: "Configuring the Element Translator"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/service_016.html"
depth: 4
children: ["Introduction to Element Translator Capabilities", "Common Functions", "Date Time Converter", "Merging Information", "Simple Data Mapping", "Searching for Related Models", "UI Component Display Value Translation", "Internationalization Translator", "File Permission Translator", "Run Script Translator", "Attachment Translator"]
---
# Configuring the Element Translator

The element translator provides a mechanism to convert the input and output elements of a service to store or return the converted elements.

-   **[[Introduction to Element Translator Capabilities|Introduction to Element Translator Capabilities]]**  
    
-   **[[Common Functions|Common Functions]]**  
    The **Common functions** translator provides common translation functions.
-   **[[Date Time Converter|Date Time Converter]]**  
    The **Date Time Converter** translator is used to convert the time in the character string format based on the time zone.
-   **[[Merging Information|Merging Information]]**  
    The **Merging Information** translator provides a mechanism for combining data of multiple elements.
-   **[[Simple Data Mapping|Simple Data Mapping]]**  
    The **Simple data mapping** translator provides the simple data mapping function to map the source value to a translated value.
-   **[[Searching for Related Models|Searching for Related Models]]**  
    The **Searching for Related Models** translator translates elements from related data models.
-   **[[UI Component Display Value Translation|UI Component Display Value Translation]]**  
    The **Radio box**, **Check box**, **Datetime**, and **Select person** components contain two parts: values stored in the system and values displayed on the GUI. The value returned by a service is used as values stored in the system of the component. When the component assigns values using values stored in the system, a query request is sent to obtain values displayed on the GUI. This deteriorates page performance. The **UI Component Display Value Translation** translator is used to translate the values returned by the service to two parts: values stored in the system and JSON object of the values displayed on the GUI.
-   **[[Internationalization Translator|Internationalization Translator]]**  
    **i18n translator** allows a service to display its contents in the language the same as the browser language. In the output parameter configuration of the service, a field returned by the service is an internationalization key value, which is then translated into the corresponding language by the internationalization translator.
-   **[[File Permission Translator|File Permission Translator]]**  
    
-   **[[Run Script Translator|Run Script Translator]]**  
    
-   **[[Attachment Translator|Attachment Translator]]**  
    

**Parent topic:** [[Configuring Services|Configuring Services]]

## Sub-topics

- [[Introduction to Element Translator Capabilities]]
- [[Common Functions]]
- [[Date Time Converter]]
- [[Merging Information]]
- [[Simple Data Mapping]]
- [[Searching for Related Models]]
- [[UI Component Display Value Translation]]
- [[Internationalization Translator]]
- [[File Permission Translator]]
- [[Run Script Translator]]
- [[Attachment Translator]]
