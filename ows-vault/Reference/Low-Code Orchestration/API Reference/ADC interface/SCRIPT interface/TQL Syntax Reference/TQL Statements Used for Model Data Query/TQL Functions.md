---
title: "TQL Functions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_011.html"
depth: 6
---
#### Date and Time Formats

**Table 2** Date and time formats  
| Date and Time | Description |
| :-- | :-- |
| yyyy or YYYY | Four-digit year |
| yy or YY | Two-digit year, that is, the last two digits of a four-digit year |
| MM | Two-digit month, ranging from 01 to 12 |
| dd | Day in a two-digit month, ranging from 01 to 31 |
| HH | 
-   In the GaussDB scenario, two-digit hours are used, that is, 00 to 23.
-   In the MySQL database scenario, when **HH** is defined, a byte with a value of 0 is not added in the front of the most significant byte, that is, 0 to 23. When **H** is defined, a byte with a value of 0 is added in the front of the most significant byte, that is, 00 to 23.

 |
| KK | Two-digit hour, ranging from 01 to 12 |
| mm | Two-digit minute, ranging from 00 to 59 |
| ss | Two-digit second, ranging from 00 to 59 |
| a | AM or PM |