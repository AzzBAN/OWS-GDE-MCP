---
title: "Rule: Injection Attacks Must Be Prevented When TQL Statements Are Used for Query"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001208200519.html"
depth: 5
---
# Rule: Injection Attacks Must Be Prevented When TQL Statements Are Used for Query

**Description**: GDE provides services for configuring TQL query actions and TQL query APIs that can be called in JavaScript. If the corresponding TQL query statements are not properly used, TQL injection problems may occur.

TQL is a database query language after the platform encapsulates the underlying database. The TQL service opened to the frontend can only execute the SELECT statement and provide read protection for sensitive data tables such as user and password. The front-end TQL APIs cannot be used to query the data.

**Check guide**: Check whether the TQL query service is configured or the TQL execution method is called in JavaScript, and check whether the TQL statement to be executed is correctly compiled. Pay attention to the scenario where untrusted input (such as frontend user input) is used to combine TQL statements for query.

**Service configuration scenario 1: TQL query service scenario example (It is recommended that developers use this method to perform TQL query.)**

![[en-us_image_0000001524137089.png]]

**Service configuration scenario 2: TQL query scenario example in the query service (It is recommended that developers use this method to perform extended condition query.)**

![[en-us_image_0000001524377841.png]]

**JavaScript calling scenario: example of calling TQL query services such as query-by-tql in JavaScript (It is not recommended that developers write scripts for calling, which is error-prone. The following is a negative example.)**

var property =... // The value is entered externally, for example, **prime\_cost**.
var author =... // The value is entered externally, for example, **abc**.
var title =... // The value is entered externally, for example, **1' or '1' = '1**.
var tql = "select " + property + " from book where author = '" + author + "' and title = '" + title + "'";
// The value of **tql** is **select prime\_cost from book where author = 'abc' and title = '1' or '1' = '1'**.
// The **tql** value is used to query the purchase prices of all books. The original author and title conditions (TQL injection) are bypassed, and non-public information such as the purchase price can be queried (no whitelist validation is performed).
var request = {
    "start": 0,
    "limit": 10,
    "tql": tql
};
ServiceInvoker.post("/adc-model/rest/v1/model-instances/query-by-tql", request);

Note that the backend may transfer values. You are advised to confirm all codes where values are concatenated during TQL statement obtaining. If the input data at the frontend is concatenated, TQL injection risks occur. In addition, only query-by-tql is described in the example. Other APIs exist due to historical reasons. Pay attention to the APIs during rectification.

**Positive TQL example**:

**1\. Page service precompilation mode (recommended)**: Use variables in TQL statements.

Select \* from cts\_issuetraceinfo a where a.active =$condition order by $sort

**2\. JS service precompilation mode (second choice)**: Use variables in JS TQL statements.

var author =... // The value is entered externally, for example, **Tom**.
var title =... // The value is entered externally, for example, **You're welcome**.
var tql = "select category from book where author = $author and title = $title";
// The value of **tql** is **select category from book where author = $author and title = $title**.
var request = {
    "start": 0,
    "limit": 10,
    "tql": tql,
    "parameters": {// Use parameters to transfer the values of **$author** and **$title** in TQL.
        "author": author,
        "title": title
    }
};
ServiceInvoker.post("/adc-model/rest/v1/model-instances/query-by-tql", request);

**3\. Mode of escaping JS service parameters (used only in JS scripts)**: When TQL statement query parameters in JS are concatenated, use the TQL.escapeString method to escape the parameters, and enclose the parameters in single quotation marks ('). If the parameters are not enclosed in single quotation marks ('), TQL injection risks still will occur after parameter escaping.

-   A proper API must be selected for transcoding. For example, in service JS, TQL.escapeIdentifier_(content)_ must be used to transcode identifiers, and TQL.escapeString_(content)_ must be used to transcode string constants. For details, see the APIs in the TQL application scenarios.
-   Transcoded texts can prevent injection only when they are enclosed in quotation marks (double quotation marks for identifiers and single quotation marks for character strings).

var tql = "Select \* from cts\_issuetraceinfo a where a.active ='" + TQL.escapeString(condition)+"'";

**Negative TQL example**:

1\. Quotation marks are not correctly used during transcoding.

var property =... // The value is entered externally, for example, **prime\_cost, max\_discount**.
var author =... // The value is entered externally, for example, **author**.
var title =... // The value is entered externally, for example, **title**.
var tql = "select " + TQL.escapeIdentifier(property) + ""\\" from book where author = " + TQL.escapeString(author) + " and title = " + TQL.escapeString(title) + "";
// The value of **tql** is **select prime\_cost, max\_discount from book where author = author and title = title**.
// The **tql** value is used to query the purchase prices and maximum discounts of all books. The originally specified author and title conditions are bypassed (because they are not enclosed in quotation marks. As a result, the conditions are bypassed without bypassing transcoding). In addition, the purchase price and maximum discount information can be queried (because they are not enclosed in quotation marks. As a result, multiple attributes can be queried).

2\. Variables are concatenated in TQL statements.

"Select \* from cts\_issuetraceinfo a where a.active = "+ condition +" order by "+ sort + "desc"

The situation may occur during JavaScript service call, which may cause TQL injection risks. Do not use this method.

3\. _${Parameter}_ are used to concatenate TQL statements..

var filter\_name = \_message.filter\_name // Input from external systems
var query = \_message\[\_message.filter\_name\]
let tql = \`
select 
    distinct ${filter\_name}
from "/TenThousandHorsesTool/TenThousandHorsesTool/tt\_email\_log" 
where ${filter\_name} contains $!query
 order by 1 
\`
let request = {
    "start": 0,// Start position
    "limit": 5000,// Maximum number of records. The maximum value is **5000**.
    "page\_size": 5000,// Number of records returned on each page
    "tql": tql, // TQL statement
    "query\_type": "NORMAL",
    "parameters": {
        "query": query
    },// Value of the parameter in the TQL statement
};
return ServiceInvoker.post("/adc-model/rest/v1/model-instances/query-by-tql", request);

The situation where variables are concatenated using _${Parameter}_ in TQL statements may occur during JavaScript service call, which may cause TQL injection risks. Do not use this method.

**4\. Custom function call across files in service scripts**

const COMMON\_UTIL = require("/SAQM\_Rule34\_EvilTQL\_test\_all/SAQM\_Rule34/common")
var rule\_name = \_message.rule\_name;
let tql = \`SELECT \* FROM "/SAQM\_Rule34\_EvilTQL\_test\_all/SAQM\_Rule34/saqm\_rule34\_rule\_model" WHERE rule\_name = "\` + rule\_name + \`"\`;

let response = COMMON\_UTIL.queryByTql(tql);
return {
    results: response.results
}

In a service script, when the **require** syntax is used to introduce the common function exported from other files, the function is identified as parameter injection during TQL execution. Therefore, do not use this method.

**Precautions**:

1\. In the precompilation mode, single quotation marks and double quotation marks have the same effect for the query. The mode of escaping JavaScript service parameters means to add different quotation marks based on fields.

2\. If a variable is of the numeric type, an error is reported during TQL statement execution. You do not need to enclose the variable in single quotation marks ('). However, you need to set a validator for the variable, and the validator must be of the numeric type.

3\. Table names and column names cannot be combined in precompilation mode. The whitelist is recommended to validate the combined parameters.

**Tool supported or not**: yes

**Specification name**: Security\_DataCheck\_TQLQuery\_ServiceScript\_InjectionRisk

**Category**: non-bottom-line check item

**Severity**: critical

**Orchestration scenario**: all

**Parent topic:** [[Data Verification|Data Verification]]