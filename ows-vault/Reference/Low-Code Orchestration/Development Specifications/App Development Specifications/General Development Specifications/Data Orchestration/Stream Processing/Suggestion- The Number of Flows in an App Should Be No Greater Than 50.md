---
title: "Suggestion: The Number of Flows in an App Should Be No Greater Than 50"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001917659297.html"
depth: 6
---
# Suggestion: The Number of Flows in an App Should Be No Greater Than 50

**Specification name**: General\_DataFactory\_Stream\_Application\_Scale

**Description**: The number of flows in an app should be no greater than 50. If the logic is complex, you are advised to divide it into multiple modules (that is, multiple apps).

**Check guide**: Check the number of flows in the app.

**Impact**: If too many flows are used in an app, the app package may be too large, the installation may be slow, and data insertion may time out.

**Parent topic:** [[Stream Processing|Stream Processing]]