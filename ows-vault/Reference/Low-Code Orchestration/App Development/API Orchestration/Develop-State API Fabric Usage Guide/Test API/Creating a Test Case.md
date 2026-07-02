---
title: "Creating a Test Case"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/apifabric_164.html"
depth: 5
---
#### Procedure

1.  Select the API to which the test case is to be added.
2.  Go to the API test case page and perform the API test. The following two types of test scenarios are available. You can select a test scenario based on site requirements.
    
    ![[note_3.0-en-us.png]]
    
    Test cases can be called in the following three modes: **Invoke Test Stub**, **Invoke Service Address**, and **Use the API invocation rule**. **Invoke Test Stub** and **Invoke Service Address** are the calling modes configured during case creation. **Use the API invocation rule** is the global calling mode of the API test case configured above the test case list.
    
    **Use the API invocation rule** (the calling mode selected above the test case list) is the global calling mode of all test cases in the API. The calling mode (**Invoke Test Stub** or **Invoke Service Address**) configured in the test case applies only to the test case. The calling mode is used in the following scenarios:
    
    -   When you need to call the test stub of the test service, select **Invoke the test stub**.
    -   When you need to call a test case through a specific path, select **Invoke the base path**.
    
    -   If there are real test cases, click **Import Test Case**. In the dialog box that is displayed, select local test cases and import them.
        
        You can also click **New Test Case** to manually add a case.
        
        After the configuration is completed, click the **Execute** button or return to the API page. On the API page, click ![[en-us_image_0122468842.png]] of the case.
        
        After the execution is complete, view the execution result in the response body on the case page. If the execution is successful, a success response is returned. If the execution fails, an error cause message is displayed.
        
    -   If there are no real test cases, add a test stub based on [[(Optional) Creating a Test Stub|6.2.4 (Optional) Creating a Test Stub]], and use the test stub for test.
        1.  After the test stub is configured, click the **Test Case** tab and click **New Test Case**. The page for adding a test case is displayed.
        2.  Configure test case information based on site requirements.
        3.  Click **Save** and **Execute** to execute the test case.
        4.  After the execution, if the response body is the same as that in the test stub, the test is successful.