---
title: "Tenant Asset Security Development"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001104689482.html"
depth: 4
---
# Tenant Asset Security Development

1\. Tenant developers are responsible for the asset service security governance, and risk and compliance analysis.

Scenario 1: A tenant developer plans to roll out the newly developed asset at the EU site, but does not perform privacy impact assessment (PIA) properly or use the GDE encryption and anonymization capabilities, leading to privacy violations.

The tenant developer takes the responsibility to analyze the security of the surrounding environment related to the service and use GDE platform capabilities to follow the compliance requirements.

2\. GDE formulates asset development specifications. Tenant developers must develop assets based on the specifications.

Scenario 1: According to the asset development specifications, the verification of service input parameters is not required. The tenant developer does not verify input parameters during development. The security test team finds that the assets developed by the tenant have XSS injection issues.

GDE takes the responsibility for not verifying input parameters, which is not required in the specifications.

Scenario 2: The asset development specifications clearly require verification of service input parameters. However, the tenant developer does not verify them during development. The security test team finds that the assets developed by the tenant have XSS injection issues.

In this case, the tenant takes the responsibility for not meeting the development compliance requirements specified on GDE.

3\. Based on the asset development specifications, GDE develops quality evaluation tools and asset test tools to help developers detect security issues.

Scenario 1: The asset development specifications clearly require that service input parameters be verified and GDE provides a quality evaluation tool for scanning. The tenant developer does not verify the input parameters during development, and the scanning tool does not detect any issue. The security test team finds that the assets developed by the tenant have XSS injection issues.

In this case, the tenant takes the responsibility. The tool is only used to assist the tenant developer in detecting issues. No matter whether the tool is available or whether the tool detects issues, the tenant developer is responsible for the development according to the specifications.

4\. In the No Code/Low Code scenarios, tenant developers should not introduce open-source or third-party software.

Scenario 1: A tenant developer copies open-source software codes and pastes them to the GDE develop state page to introduce the open-source software. During penetration test, the security test team finds that the open-source software has known vulnerabilities.

In this case, the tenant takes the responsibility for the following issues caused by referencing the open-source software fragment: vulnerabilities, intellectual property rights, viruses, malware, and lifecycle management.

5\. GDE provides the orchestration capability, which can be maliciously used by some tenant developers to develop malicious codes.

Scenario 1: A tenant developer develops malicious JavaScript codes and sends the cookies of the login user to an external network. As a result, the user identity is spoofed.

The tenant takes the responsibility. The orchestration capability provided by GDE cannot be used to develop malicious codes for any purpose, including but not limited to viruses, rogue software, Trojan horses, backdoors, listening programs, and mining programs.

**Parent topic:** [[Scenario Examples|Scenario Examples]]