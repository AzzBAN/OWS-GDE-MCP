---
title: "Packets with the multiRef Tag Cannot Be Parsed"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001662324764.html"
depth: 6
---
#### Examples

The following is an example of a packet segment with the **multiRef** tag:

<?xml version='1.0' encoding='utf-8'?>
<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Header/>
    <soapenv:Body>
        <ns1:vRBTAddCallerGroupMemResponse
            xmlns:ns1="http://impl.prbt.cmcc.com" soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
            <vRBTAddCallerGroupMemReturn
                xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" soapenc:root="0" soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xsi:type="ns2:VRBTAddCallerGroupMemResp">
                <memberResult soapenc:arrayType="ns2:MemberResult\[1\]" xsi:type="soapenc:Array">
                    <MemberResult soapenc:root="0" soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xsi:type="ns3:MemberResult">
                        <MSISDN xsi:type="soapenc:string">135XXXXXXXX</MSISDN>
                        <description xsi:type="soapenc:string">1111111</description>
                        <result xsi:type="soapenc:string">000000</result>
                    </MemberResult>
                </memberResult>
                <description xsi:type="soapenc:string">111111</description>
                <returnCode xsi:type="soapenc:string">000000</returnCode>
            </vRBTAddCallerGroupMemReturn>
        </ns1:vRBTAddCallerGroupMemResponse>
       ** <multiRef**
            xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
            xmlns:ns2="http://schemas.prbt.cmcc.com"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="id0" soapenc:root="0" soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xsi:type="ns2:VRBTAddCallerGroupMemResp">
            <memberResult soapenc:arrayType="ns2:MemberResult\[1\]" xsi:type="soapenc:Array">
                <memberResult href="#id1"/></memberResult>
            <description xsi:type="soapenc:string">111111</description>
            <returnCode xsi:type="soapenc:string">000000</returnCode>
        **</multiRef>**
    </soapenv:Body>
</soapenv:Envelope>