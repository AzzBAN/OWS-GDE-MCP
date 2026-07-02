---
title: "Suggestion: Reasonably Divide Apps"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001399523345.html"
depth: 6
---
# Suggestion: Reasonably Divide Apps

**Description**: App assets refer to assets that can be directly used by users. Generally, an app can be independently delivered in a specific scenario. If an app contains too much content, it can be split into multiple apps. For details about the splitting principles, see the microservice splitting principles in the industry. An app can be divided into multiple modules to facilitate maintenance.

**Check guide**:

Check whether the boundaries of orchestration elements in the project corresponding to app development are clearly defined. An app should not be too large or too small. You are advised to analyze the app from the service perspective, abstract the system, obtain a highly cohesive domain model, and then develop and design the app.

**Tool supported or not**: no

**Specification name**: General\_Basic\_Proper\_App\_Design

**Severity**: suggestion

**Parent topic:** [[Principles|Principles]]