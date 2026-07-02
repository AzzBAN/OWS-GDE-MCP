---
title: "Rule: Ensure That the Asset File Is Signed for Custom Assets of the Probe Type"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002309655344.html"
depth: 6
---
# Rule: Ensure That the Asset File Is Signed for Custom Assets of the Probe Type

**Description**: When asset type is set to **Probe**, probe assets can be installed. If the asset file is not signed, the probe and the entire app will fail to be deployed.

**Check guide**: Check whether the asset file contains the inner CMS signature.

**Positive example**: The inner CMS signature are as shown in the following figures.

![[en-us_image_0000001600055588.png]]

**Positive example**: Only the probe is included, and no signature file is available.

![[en-us_image_0000001649617593.png]]

**Tool supported or not**: no

**Specification name**: General\_Custom\_Forbidden\_Unsgined\_Probe\_Asset

**Severity**: major

**Parent topic:** [[Customized Asset|Customized Asset]]