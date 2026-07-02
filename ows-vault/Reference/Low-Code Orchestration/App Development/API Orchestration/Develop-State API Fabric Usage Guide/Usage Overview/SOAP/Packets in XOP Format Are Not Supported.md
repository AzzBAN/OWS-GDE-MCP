---
title: "Packets in XOP Format Are Not Supported"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001710244673.html"
depth: 6
---
#### Examples

The following is an example of a packet in XOP format:

POST /test HTTP/1.0
Content-Type: Multipart/Related; boundary=MIME\_boundary; type=text/xml
Content-Length: XXXX
SOAPAction: http://www.soapattach.com/test
 
--MIME\_boundary
 
Content-Type: text/xml; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
<?xml version='1.0'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
 <soap:Body>
 <Car name="myCar">
<Picture>
< xbinc:Include href = "cid:\*\*\*\*\*\*\*"/>
</Picture>
 </Car>
 </soap:Body>
</soap:Envelope>
 
--MIME\_boundary
Content-Type: image/jpeg
Content-Transfer-Encoding: binary
Content-ID: <\*\*\*\*\*\*\*>
...1010100010101011011101010100101110101001001010101010101011...
--MIME\_boundary—