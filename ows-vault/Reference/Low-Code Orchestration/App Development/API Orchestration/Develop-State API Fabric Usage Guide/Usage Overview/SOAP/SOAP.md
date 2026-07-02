---
title: "SOAP"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001710364673.html"
depth: 5
children: ["mustUnderstand Subelement Is Not Verified", "Packets with the multiRef Tag Cannot Be Parsed", "Packets in XOP Format Are Not Supported", "Attachments Cannot Be Transferred", "Prefix of the Packet Namespace Cannot Be Modified", "any Element Cannot Be Defined in the XSD File", "duration Data Type Cannot Be Defined in the XSD File of the Southbound Service", "Namespace Defined in the WSDL File Cannot End with type", "Header Format in a Northbound Request Must Be the Same As That Defined in the WSDL File", "Fault Element Can Be Returned to the Northbound Client", "HTML Entities in the CDATA Section Can Be Restored", "Values Can Be Assigned to Element Attributes in Packets During Flow Orchestration"]
---
# SOAP

This section describes the special usage and restrictions of the SOAP protocol in the API Fabric.

-   **[[mustUnderstand Subelement Is Not Verified|mustUnderstand Subelement Is Not Verified]]**  
    The API Fabric does not verify the **mustUnderstand** subelement contained in the SOAP header and processes the subelement as a normal packet.
-   **[[Packets with the multiRef Tag Cannot Be Parsed|Packets with the multiRef Tag Cannot Be Parsed]]**  
    The API Fabric uses Axis2, and **multiRef** is the tag of Axis1. Therefore, the tag cannot be parsed.
-   **[[Packets in XOP Format Are Not Supported|Packets in XOP Format Are Not Supported]]**  
    The southbound and northbound services do not support packets in XML-binary Optimized Packaging (XOP) format. Do not use packets in XOP format to call APIs.
-   **[[Attachments Cannot Be Transferred|Attachments Cannot Be Transferred]]**  
    Attachments cannot be transferred in the southbound and northbound services during API calling.
-   **[[Prefix of the Packet Namespace Cannot Be Modified|Prefix of the Packet Namespace Cannot Be Modified]]**  
    For northbound response and southbound request packets, the namespace prefix in the packets cannot be modified.
-   **[[any Element Cannot Be Defined in the XSD File|any Element Cannot Be Defined in the XSD File]]**  
    If the **any** element is defined in the XSD file, the element will be lost after being parsed by the API Fabric.
-   **[[duration Data Type Cannot Be Defined in the XSD File of the Southbound Service|duration Data Type Cannot Be Defined in the XSD File of the Southbound Service]]**  
    If the XSD file of the southbound service contains the definition of the **duration** data type, data will be lost when data is sent back to the northbound service through the API Fabric.
-   **[[Namespace Defined in the WSDL File Cannot End with type|Namespace Defined in the WSDL File Cannot End with type]]**  
    For the SOAP protocol, the namespace defined in the WSDL file cannot end with **type**. Otherwise, the compilation fails.
-   **[[Header Format in a Northbound Request Must Be the Same As That Defined in the WSDL File|Header Format in a Northbound Request Must Be the Same As That Defined in the WSDL File]]**  
    When a northbound request of the SOAP protocol is sent to the API Fabric, the node names and node quantity of the SOAP header in the request must be the same as those defined in the WSDL file.
-   **[[Fault Element Can Be Returned to the Northbound Client|Fault Element Can Be Returned to the Northbound Client]]**  
    The API Fabric cannot properly parse the value of **Fault** returned by the southbound service. You can customize a JavaScript script in the exception diagram element to return the value of **Fault** in the SOAP packet to the northbound client.
-   **[[HTML Entities in the CDATA Section Can Be Restored|HTML Entities in the CDATA Section Can Be Restored]]**  
    HTML entities in southbound requests can be restored by adding JavaScript to the diagram element script executed at any time during flow orchestration.
-   **[[Values Can Be Assigned to Element Attributes in Packets During Flow Orchestration|Values Can Be Assigned to Element Attributes in Packets During Flow Orchestration]]**  
    If you want to assign values to element attributes in northbound responses or southbound requests during flow orchestration, you can use mapping during flow orchestration.

**Parent topic:** [[Usage Overview|Usage Overview]]

## Sub-topics

- [[mustUnderstand Subelement Is Not Verified]]
- [[Packets with the multiRef Tag Cannot Be Parsed]]
- [[Packets in XOP Format Are Not Supported]]
- [[Attachments Cannot Be Transferred]]
- [[Prefix of the Packet Namespace Cannot Be Modified]]
- [[any Element Cannot Be Defined in the XSD File]]
- [[duration Data Type Cannot Be Defined in the XSD File of the Southbound Service]]
- [[Namespace Defined in the WSDL File Cannot End with type]]
- [[Header Format in a Northbound Request Must Be the Same As That Defined in the WSDL File]]
- [[Fault Element Can Be Returned to the Northbound Client]]
- [[HTML Entities in the CDATA Section Can Be Restored]]
- [[Values Can Be Assigned to Element Attributes in Packets During Flow Orchestration]]
