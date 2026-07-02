---
title: "Context Variables"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_020.html"
depth: 8
---
#### \_runtime

The variable value of \_runtime is an object that stores common information about the runtime-state environment. Members of this object are read-only.

**Table 1** Members of the \_runtime object   
| Member | Type | Description |
| :-- | :-- | :-- |
| tenantId | String | Current tenant ID. |
| userName | String | Current user name (account name). |
| userId | String | Current user ID. |
| timeZone | String | Current time zone. Only the tenant time zone is returned. |
| language | String | Current language. For example, en\_US. |
| trackerId | String | Trace ID. |
| clientIp | string | IP address of the caller. |