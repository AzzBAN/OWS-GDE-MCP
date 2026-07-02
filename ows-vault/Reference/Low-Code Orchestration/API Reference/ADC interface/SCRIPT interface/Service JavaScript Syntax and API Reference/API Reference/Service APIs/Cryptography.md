---
title: "Cryptography"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_029.html"
depth: 7
---
# Cryptography

**Table 1** Cryptography tool description   
| API | Description | Example |
| :-- | :-- | :-- |
| Crypto.sha256(plain) | The input parameter plain is the character string to be encrypted. The 256-bit hash value encrypted using the SHA256 algorithm is returned. | 
Crypto.sha256("String want to encrypted");

 |
| Crypto.sha384(plain) | The input parameter plain is the character string to be encrypted. The 384-bit hash value encrypted using the SHA384 algorithm is returned. |
| Crypto.sha512(plain) | The input parameter plain is the character string to be encrypted. The 512-bit hash value encrypted using the SHA512 algorithm is returned. |
| Crypto.hmacSha256(key, plain) | The input parameters key and plain indicate the key and the character string to be encrypted, respectively. The 256-bit hash value encrypted using the HmacSHA256 algorithm is returned. |
| Crypto.randomInteger() | This API does not accept input parameters and a 32-bit secure random integer is returned. | let foo = Crypto.randomInteger() |
| Crypto.randomNumber() | This API does not accept input parameters and a 64-bit secure random double-precision floating point is returned. | let foo = Crypto.randomNumber() |
| Crypto.pbkdf2(plain) | The input parameter plain is the character string to be encrypted. The ciphertext encrypted using PBKDF2 is returned. | var encrypted = Crypto.pbkdf2(plain);

 |
| Crypto.validatePbkdf2(plain, encrypted) | This API is used to check whether the plaintext matches the ciphertext. | var plain = "plain" 
var encrypted = "encrypted" 
var matched = Crypto.validatePbkdf2(plain, encrypted);

 |
| Crypto.validateSha256(plain, encrypted) | This API is used to check whether the plaintext matches the ciphertext. | var plain = "plain" 
var encrypted = "encrypted" 
var matched = Crypto.validateSha256(plain, encrypted);

 | ![[note_3.0-en-us.png]]

The AES encryption and decryption capability can be implemented using common functions in the service translator.

**Parent topic:** [[Service APIs|Service APIs]]