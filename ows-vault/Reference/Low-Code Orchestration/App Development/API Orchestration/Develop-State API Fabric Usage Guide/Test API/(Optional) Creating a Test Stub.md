---
title: "(Optional) Creating a Test Stub"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_163.html"
depth: 5
---
#### Procedure

1.  Click the API name, click the **Test Stub** tab, and click **New Test Stub**. The page for creating a test stub is displayed.
2.  Enter the test stub information based on site requirements. The parameters are described in [Table 1](#EN-US_TOPIC_0000001569107033__en-us_topic_0122468916_table184767559345).
    
    **Table 1** Test stub parameters    
    | Category | Parameter | Description | Example |
    | :-- | :-- | :-- | :-- |
    | Basic Information | Policy Type | If multiple response packets exist, this policy is used to determine the response to be returned. You need to select a value from the drop-down list as required. | Sequential return |
    | Match Rule | \- | Add the information as required. For details about the parameters, see Table 2. | For details, see Table 2. |
    | Response Message | \- | Custom message returned by the test stub. After entering the response message name, click + in the response message area to add the content of the response body and response header. NOTE: Configure the SOAP response message structure based on site requirements. | 
    {
        "orderBaseInfo": {
            "accessChanelType": "",
            "beId": 0,
            "createDeptId": 0,
            "createOperId": 0,
            "interactionEventId": 0,
            "orderId":10,
        }
    }
    
     | **Table 2** Matching rule parameters   
    | Parameter | Description | Example |
    | :-- | :-- | :-- |
    | Match Parameter | Body: Request parameter. Header: Request header. NOTICE: A header indicates the request header configured by a user on the test case page. These values will be contained in the protocol header of a message. The header here is different from the header configured in the BES business code. | Body |
    | Match Way | Select JsonPath. If this parameter is set to JsonPath, set Match Rule to JsonPath/XPath. | JsonPath |
    | Match Rule | If the matching rule is JSONPath, set this parameter by referring to the rule for setting JSONPath. For example, if Match Parameter is set to Body, set Match Rule to a field name or path name in the method request body. | test |
    | Expected Value | Expected value. For example, if the value of test in Match Rule is 101, the test case is passed. If the value of test is not 101, the test case fails. | 101 | 3.  After configuring the test stub, click **Save**. The **Test Stub** page is displayed.
4.  Click the start-stop button to start the test stub server.
    
    After the test stub server is started, you cannot edit the information about the test stub server. You need to stop the test stub server before updating it.