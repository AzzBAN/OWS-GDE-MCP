---
title: "Appendix 1: Sensitive Data"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963872.html"
depth: 5
---
# Appendix 1: Sensitive Data

  
| Type | Example | Description |
| :-- | :-- | :-- |
| Authentication credential | Passwords, sessions, tokens (such as CSRF Token, File Token, Refresh Token, Access Token and JWT), tickets (such as TGT and ST), and OTP | As the key data, credentials are used to prove the identity of a user. |
| Key | Root keys, key encryption keys, data encryption keys, HMAC keys, certificate private keys, and pre-shared keys (such as AK/SK) | The cryptography is used to protect key data from being disclosed or tampered with. |
| Sensitive personal data | Refer to Appendix 2: Examples of Personal Data. Personal data whose risk level is L4 is sensitive personal data. | / |
| Key service data | Key service logic and core algorithms | Key service data is the data that involves intellectual property (IP) and needs to be protected during service evaluation. | **Parent topic:** [[Data Category|Data Category]]