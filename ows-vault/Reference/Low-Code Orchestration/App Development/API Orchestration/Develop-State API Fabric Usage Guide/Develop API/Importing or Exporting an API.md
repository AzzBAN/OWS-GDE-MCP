---
title: "Importing or Exporting an API"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_160.html"
depth: 5
---
#### Constraints

In GDE 26.1.0 and later versions, a signature certificate can be selected during API export.

-   You can use the API Fabric default signature certificate **GDE\_API-FABRIC\_SIGN** and the XMS default signature certificate **acm.sign.jks**. If you need to use a new self-issued certificate of the XMS, name it in the format of **GDE\_API-FABRIC\_**_\*\*\*\*_, for example, **GDE\_API-FABRIC\_custom**.
-   When importing API asset packages from the develop state environment of GDE 26.1.0 or later to the runtime state environment of a version earlier than GDE 26.1.0, select the **GDE\_API-FABRIC\_SIGN** signature certificate during the export of the API asset packages.
-   The API Fabric polls the signature certificate, signature verification certificate, and certificate revocation list every 5 minutes. In this case, the certificates displayed in the develop state environment cannot be synchronized in real time.