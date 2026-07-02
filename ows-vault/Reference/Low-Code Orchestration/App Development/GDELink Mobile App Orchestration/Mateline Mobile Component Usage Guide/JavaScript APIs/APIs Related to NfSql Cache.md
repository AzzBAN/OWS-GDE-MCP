---
title: "APIs Related to NfSql Cache"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001732219688.html"
depth: 5
---
# APIs Related to NfSql Cache

**NfSql.cache.get(param,callback)**

Used to query the cached data.

Input parameters:

**param**: JSON format

**callback**: callback function after the query result is returned

Example:

NfSql.cache.get({ key: self.cacheKey }, function(valueObject) {

if (valueObject && valueObject != null) {

parseServiceData(valueObject.value);

$scope.$apply();

}

});

Precautions:

This API is an asynchronous API. The logic that depends on the **get** result must be placed in the callback function. Otherwise, the logic processing may be abnormal. For example, the **redirectTo** redirection method depends on the returned value for different processing, and the correct script is as follows:

var type = "";
NfSql.cache.get({ key: self.cacheKey }, function(valueObject) {
if (valueObject && valueObject != null) {
var value = valueObject.value;
if (value == "submit"){
type = "Submit";
}
redirectTo(type);
}
});

The following is an example of an incorrect script:

var type = "";
NfSql.cache.get({ key: self.cacheKey }, function(valueObject) {
if (valueObject && valueObject != null) {
var value = valueObject.value;
if (value == "submit"){
type = "Submit";
}
}
});
redirectTo(type);

**NfSql.cache.save(param,callback)**

**NfSql.cache.update(param,callback)**

**Parent topic:** [[JavaScript APIs|JavaScript APIs]]