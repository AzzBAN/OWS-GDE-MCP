---
title: "Anonymizing the Log Information"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001757439893.html"
depth: 7
---
#### U.mask(message, maskRule) ⇒ String

  
| Parameter | Type | Description |
| :-- | :-- | :-- |
| message | String | Log information |
| maskRule | Object | Anonymization rule configuration items | Anonymization Rule Configuration Items (maskRule)

  
| Parameter | Description | Example Value |
| :-- | :-- | :-- |
| type | Anonymization rules. There are several built-in anonymization rules available. | phone |
| start | The first several digits of log information are not anonymized. | 3 |
| end | The last several digits of log information are not anonymized. | 3 |
| format | Customized anonymization rule. Sample information with the same length must be provided. Anonymized digits are marked with asterisks (\*). | 138\*00\*\*00\*\* | Example:

// By default, characters in the even position are anonymized.
U.mask("13800000000"); // 1\*8\*0\*0\*0\*0  

// Name. If there is only one character, it is anonymized. Otherwise, all characters except the first one are anonymized.
U.mask("Zhang San", { type: "name" }); // Zhang \*

// Birthday. If the birthday contains less than or equal to four digits, all digits are anonymized. Otherwise, the digits following the first four digits are anonymized.
U.mask("1900-01-01", { type: "birthday" }); // 1900-\*\*-\*\*  

//Bank account. If the length is less than or equal to 10, all characters except the first and last ones are anonymized. If the length exceeds 12, the first six digits and the last four digits are retained.
U.mask("6200000000000000000", { type: "bankAccount" }); //620000\*\*\*\*\*\*\*\*\*0000  

// Email address. Both the emailbox name and address are anonymized.
U.mask("zhangsan@huawei.com", { type: "email" }); // \*\*\*\*\*\*\*\*@\*\*\*\*\*\*.com  

// Phone number. Characters except the first three digits and last four digits are anonymized.
U.mask("13800000000", { type: "phone" }); // 138\*\*\*\*0000  

// IPv4 address. The last segment is anonymized.
U.mask("127.0.0.1", { type: "ipv4" }); // 127.0.0.\*  

// IPv6 address. The last 88 bits are anonymized.
U.mask("fe80:0000:0000:0000:0000:0000:0000:0000", { type: "ipv6" }); // fe80:0000:00\*\*:\*:\*:\*\*\*:\*\*\*\*:\*\*\*\*  

// ID card number. The last 12 characters are anonymized.
U.mask("320000000000000000", { type: "id" }); // 320000\*\*\*\*\*\*\*\*\*\*\*\*  

// MAC address. The last four digits are anonymized.
U.mask("12-23-56-78-9A-7B-33", { type: "mac" }); // 12-23-56-78-9A-\*\*-\*\*  

// IMEI/IMSI. The last four digits are anonymized.
U.mask("869169030071234", { type: "imeiImsi" }); // 86916903007\*\*\*\*  

// Common account. If the length is less than or equal to 1, all characters are anonymized. If the length is less than 8, only the last character is retained. If the length is greater than or equal to 8, the last four characters are retained and other characters are anonymized.
U.mask("defaultAdmin", { type: "accountId" }); // \*\*\*\*\*\*\*\*dmin  

// If the length is less than or equal to the sum of the values of **start** and **end**, all characters except the first and last ones are anonymized. Otherwise, characters at the first **start** positions and last **end** positions are retained.
U.mask("13800000000", { start: 4, end: 3 }); // 1380\*\*\*\*000  

// Characters are anonymized according to the value of **format**.
U.mask("13800000000", { format: "0\*\*0\*00\*000" }); // 1\*\*0\*00\*000