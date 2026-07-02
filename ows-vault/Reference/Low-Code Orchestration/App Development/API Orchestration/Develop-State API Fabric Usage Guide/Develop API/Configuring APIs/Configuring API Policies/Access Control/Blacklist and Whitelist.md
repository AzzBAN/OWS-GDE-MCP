---
title: "Blacklist and Whitelist"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/api_fabric/apifabric_tool_operation_guide_051.html"
depth: 8
---
#### Restrictions

The blacklist and whitelist are used to forbid and allow access to APIs or the IP addresses of methods. You can configure the policy at the API level and method level. The priority of the method level is higher than that of the API level. A maximum of 50 records can be configured at the API level and method level respectively.

The **API-level blacklist and whitelist** policy not only can be customized, but also can reference a defined common policy.

The rules for verifying blacklists and whitelists are as follows:

1.  If multiple policies are configured with IP addresses, the system preferentially determines the IP address that is in the same network segment as the access IP address. If an IP address configured in the policy is in the same network segment as the access IP address, the system directly returns a determination result indicating whether to accept the access IP address. Otherwise, the system determines whether the access IP address is on a different network segment from the IP address configured in the policy.
2.  If the access IP address is on the same network segment as the IP address configured in the policy, the blacklist rule is preferentially used for verification. If the blacklist contains an IP address configured for the policy, the system directly returns the determination result, indicating that the access from the IP address is denied. If no IP address is in the blacklist, the rule that exists only in the whitelist is used for verification.
3.  If the access IP address is on a different network segment from the IP address configured in the policy, the whitelist rule is preferentially used for verification. If the whitelist contains an IP address configured for the policy, the system directly returns the determination result, indicating that the access from the IP address is denied. If no IP address is in the whitelist, the rule that exists only in the blacklist is used for verification.
4.  The rules for determining whether to accept an access request are as follows:
    1.  In the case that the access IP addresses are on the same network segment as the IP address configured in the policy, if the network segment is added to the blacklist, all IP addresses in the network segment are denied. If the network segment is added to the whitelist, all IP addresses in the network segment can be accessed.
    2.  In the case that the access IP addresses are on a different network segment from the IP address configured in the policy, if the IP address configured in the policy is added to the whitelist, the access to the IP address that is on a different network segment from the IP address configured in the policy is denied. If the IP address configured in the policy is added to the blacklist, the IP addresses that are on a different network segment from the IP addresses configured in the policy can be accessed.