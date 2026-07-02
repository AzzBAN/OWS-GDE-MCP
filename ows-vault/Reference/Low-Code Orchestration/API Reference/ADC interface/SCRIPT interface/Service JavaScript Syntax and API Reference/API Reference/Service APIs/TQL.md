---
title: "TQL"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_024.html"
depth: 7
---
# TQL

In JavaScript, TQL-related operations can be implemented using TQL statements.

**Table 1** TQL APIs   
| API | Description | Example |
| :-- | :-- | :-- |
| TQL.escapeString(content) | Escape the input parameters as required. The returned value can be directly concatenated to the TQL statement as a string constant. Parameter:
-   **content**: Indicates the character string to be processed, which is in string or number type.

Returned value: A converted character string, which is in string type. For details, see Quotation Mark. | var property = "category";
var author = "Tom";
var title = "You're welcome"
var tql = "select \\"" + TQL.escapeIdentifier(property) + "\\" from book where author = '" + TQL.escapeString(author) + "' and title = '" + TQL.escapeString(title) + "'";
//In this case, the value of TQL is **select "category" from book where author = 'Tom' and title = 'You\\'re welcome'**.

 |
| TQL.escapeIdentifier(content) | Escape the input parameters as required. The returned value can be directly concatenated into the TQL statement as an identifier. Parameter:

-   **string**: Indicates the character string to be processed, which is in string or number type.

Returned value: A converted character string, which is in string type. For details, see Quotation Mark. | ![[caution_3.0-en-us.png]]

-   Do not concatenate uncertain values (especially external input parameters) to TQL statements to avoid TQL injection risks.
-   String constants concatenated into TQL statements must be enclosed in single quotation marks (') and escaped using TQL.escapeString(_content_) to avoid TQL injection risks. In the TQL usage scenarios, it is recommended that the parameters be preferentially used to transfer dynamic values if possible.
-   Avoid using dynamic parameters (especially external input parameters), for example, TQL identifiers, which may lead to semantic uncertainty of TQL statements. If necessary, the identifiers concatenated into the TQL statements must be enclosed in double quotation marks (") and escaped using TQL.escapeIdentifier(_content_) to avoid TQL injection risks. In addition, you are advised to use a whitelist to restrict the identifiers that are dynamically concatenated to TQL statements.

**Parent topic:** [[Service APIs|Service APIs]]