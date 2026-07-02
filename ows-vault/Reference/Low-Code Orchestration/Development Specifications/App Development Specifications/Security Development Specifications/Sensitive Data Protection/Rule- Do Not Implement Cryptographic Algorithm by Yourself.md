---
title: "Rule: Do Not Implement Cryptographic Algorithm by Yourself"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348804180.html"
depth: 5
---
# Rule: Do Not Implement Cryptographic Algorithm by Yourself

**Description**: The design and implementation of cryptographic algorithm require high theoretical and coding skills and sufficient verification. Self-design or implementation of cryptographic algorithm cannot reach the level of well-known algorithms and violates Huawei redline requirements. Therefore, cryptographic algorithms on GDE provide the algorithm capabilities as listed in the following table based on scenarios for developers to select based on site requirements.

  
| Algorithm Type | Algorithm Name | Providing Way |
| :-- | :-- | :-- |
| Symmetric encryption algorithm | AES | 
-   Translator
-   Field type of a model

 |
| Hash algorithm | SHA | -   Field type of a model

 | Developers must use the preceding algorithms to prohibit the following behavior:

-   Designing and implementing private algorithms by yourself: Private and non-standard cryptographic algorithms cannot meet professional requirements in the cryptography field. In addition, its technology has not been analyzed and verified in the industry, and there may be unknown defects. In addition, such an algorithm violates the principle that encryption algorithms should be open and transparent.
-   Implementing well-known algorithms by yourself: Generally, the algorithm technologies are provided by corresponding suppliers, such as JDK and OpenSSL. The implementation of the algorithms by suppliers has been tested, verified, and commercially used for a long time, and the risks are low. Self-implementation of algorithms cannot ensure large-scale verification and may have code defects.

**Check guide**:

Manually check whether the following situations exist in the code:

-   Undisclosed and self-designed cryptographic algorithm
-   Standard cryptographic algorithm reconstructed by yourself
-   User-defined data conversion algorithms implemented through transformation, character shift, and replacement
-   Pseudo encryption through encoding, such as Base64
-   Integrity check through error control coding, such as parity check and CRC

**Positive example**:

Developers can select algorithms provided by GDE based on scenarios.

  
| Algorithm Type | Algorithm Name | Providing Way |
| :-- | :-- | :-- |
| Symmetric encryption algorithm | AES | 
-   Translator
-   Field type of a model

 |
| Hash algorithm | SHA | -   Field type of a model

 | **Tool supported or not**: yes

**Specification name**: Security\_SensitiveData\_No\_User\_Defined\_Algorithm

**Category**: bottom-line check item

**Severity**: critical

**Orchestration scenario**: all

**Parent topic:** [[Sensitive Data Protection|Sensitive Data Protection]]