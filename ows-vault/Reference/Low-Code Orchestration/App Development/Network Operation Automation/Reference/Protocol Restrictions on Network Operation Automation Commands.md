---
title: "Protocol Restrictions on Network Operation Automation Commands"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/mcp_050.html"
depth: 4
---
# Protocol Restrictions on Network Operation Automation Commands

When a specified protocol is used to send commands or receive packets, the conditions of the protocol must be met.

![[notice_3.0-en-us.png]]

MML, MOSHELL, TELNET, TL1, and ONMML are insecure. You are advised to use other secure protocols.

**Table 1** Restrictions on commands of different protocol types      
| Protocol Type | Restriction on the Content of the Sent Command | Restriction on the Length of the Sent Command | Restriction on the Length of the Received Packet | Restriction on the Packet Reading Time | Restriction on the Content of the Received Packet |
| :-- | :-- | :-- | :-- | :-- | :-- |
| SSH | Within the command whitelist | Less than 100 KB | Less than 2 MB | Less than 120 seconds | The reading of page-turning packets is supported. The page turning identifiers are ("---- More", "--More""----", "----", and "--"). |
| SFTP | 
-   Within the command whitelist
-   ls or put command

 | Less than 100 KB | Less than 2 MB | Less than 120 seconds | \- |
| MOSHELL | Within the command whitelist | Less than 100 KB | Less than 2 MB | Less than 120 seconds | For details about the fields in the returned object after the packet content is received, see Table 2. |
| Telnet | -   Within the command whitelist
-   Delete redundant spaces from the command. If the number of consecutive spaces is greater than 2, replace them with less than one.

 | Less than 100 KB | Less than 2 MB | Less than 120 seconds | The reading of page-turning packets is supported. The page turning identifiers are ("---- More", "--More""----", "----", and "--"). |
| MML | -   Within the command whitelist
-   Delete redundant spaces from the command. If the number of consecutive spaces is greater than 2, replace them with less than one.

 | Less than 100 KB | Less than 2 MB | Less than 120 seconds | For details about the fields in the returned object after the packet content is received, see Table 3. |
| TL1 | Within the command whitelist | Less than 100 KB | Less than 2 MB | Less than 120 seconds | For details about the format of received packets, see Table 4. The following is an example of a received packet: IP CMD //Acknowledgement Message < HW\_10.205.254.254 2020-09-25 17:52:32 //Response Message M COMMON\_CMD\_20200925175226\_0179 COMPLD EN=0 ENDESC=Success. //Error code description total\_blocks=60 //Block Message block\_number=1 block\_records=100 LST ONU information: -------------------------------------------------------------------------------------- OLTID PONID ONUNO NAME DESC ONUTYPE IP AUTHTYPE MAC LOID PWD SWVER 10.205.9.26 NA-0-1-2 11 0870ZYHj4938198sx w15752475959 GM220-S -- LOID 43494F5411E490D0 0870ZYHj4938198sx -- V1.0.20.208 10.205.9.26 NA-0-1-4 20 0870ZYHi8457781im 87000650930 GM219-S -- LOID 43494F54072BBC70 0870ZYHi8457781im -- V1.6.11.052 10.205.9.26 NA-0-1-4 21 0870ZYHi86391768a w13648704554 G-140W-MD -- LOID 4E42454CB1CAD56E 0870ZYHi86391768a -- NSB140WV00t03 ... 10.205.9.26 NA-0-1-4 28 0870ZYHj5845043xi 87001937294 H2-3s -- LOID 434D4443DF3F2E62 0870ZYHj5845043xi -- V2.1.1.00.02 10.205.9.26 NA-0-1-4 29 0870ZYHj4841353wk w15808615684 GM220-S -- LOID 43494F54164119F0 0870ZYHj4841353wk -- V1.0.20.208 10.205.9.26 NA-0-1-4 30 0870ZYHj22644616x w15025170210 G-140W-MH -- LOID 4E42454CFBBD6B1D 0870ZYHj22644616x -- NSB140WV00t03 -------------------------------------------------------------------------------------- > |
| REST | Within the command whitelist | Less than 100 KB | Less than 2 MB | Less than 120 seconds | The response information can be decompressed in gzip or deflate format. | **Table 2** Meanings of the fields returned after packets are received through commands of the MOSHELL protocol type   
| Field | Source | Meaning |
| :-- | :-- | :-- |
| cmd | Transferred by the service | Sent command |
| retMes | Target device | Original packet content |
| retCode | Original packet | Status code If the original packet contains Stopfile=" or stopfile=", the value of this field is 0, indicating that the command is executed successfully. |
| data | Original packet | Packet information If the original packet contains Total:, information about Total: is stored in this field. | **Table 3** Meanings of the fields returned after packets are received through commands of the MML protocol type   
| Field | Source | Meaning |
| :-- | :-- | :-- |
| cmd | Transferred by the service | Sent command |
| retMes | Target device | Original packet content |
| retCode | Value of RETCODE in the original packet | Status code |
| retDesc | Description following the value of RETCODE in the original packet | Status description |
| retLine | Line where RETCODE is located in the original packet | Line where the status is located |
| tables | Table information divided by more than four hyphens (-) (for example, ----) in the original packet | Table information in the original packet |
| data | Single table in the original packet | Information about a single table in the original packet |
| dataMap | Multiple tables in the original packet | Information about multiple tables in the original packet | **Table 4** Format requirements for packets received through the TL1 commands     
| Component | Mandatory | Component Description | Supported Format | Remarks |
| :-- | :-- | :-- | :-- | :-- |
| Acknowledgement Message | No | Confirmation message | The first line starts with IP, and the second line starts with <. | \- |
| Response Message | Yes | Response message | The first line starts with \\n, and the second line starts with M. | Packet blocks are separated by >, and packets end with a semicolon (;). |
| Error code description | No | Status code description | The EN and ENDESC fields are included. | \- |
| Block Message | No | Packet block statistics | total\_blocks, blktag, and block\_number are supported. | 
-   **total\_blocks** or **blktag**: total number of blocks
-   **block\_number**: number of current blocks. The value of this field depends on the total number of blocks.

 | **Parent topic:** [[Reference|Reference]]