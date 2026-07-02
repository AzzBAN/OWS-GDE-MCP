---
title: "Decompress(unzip)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000002521400632.html"
depth: 7
---
# Decompress(unzip)

**unzip**

**Description:**

Decompress files.

Note:

1\. The .7z/.zip/.rar/.tar/.gz files can be decompressed.

2\. You need to decompress the .gz file twice.

3\. Decompression restriction: The size of a single package cannot exceed 32 MB, the total size of the package cannot exceed 512 MB, the total size of the decompressed files cannot exceed 512 MB, and the number of files in the package cannot exceed 1000.

**Input: none**

**Parameters:**

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400632__table63239mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"> <col style="width:1700%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400632__row63248mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">name</td><td class="cellrowborder" valign="top" width="16.666666666666664%">type</td><td class="cellrowborder" valign="top" width="16.666666666666664%">is_required</td><td class="cellrowborder" valign="top" width="16.666666666666664%">default</td><td class="cellrowborder" valign="top" width="16.666666666666664%">range</td><td class="cellrowborder" valign="top" width="16.666666666666664%">help</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63267mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">target</td><td class="cellrowborder" valign="top" width="16.666666666666664%">dir</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Directory where the target compressed package is decompressed and the name of the decompressed folder.</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63281mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">value</td><td class="cellrowborder" valign="top" width="16.666666666666664%">file</td><td class="cellrowborder" valign="top" width="16.666666666666664%">True</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">7z|zip|rar|tar|gz</td><td class="cellrowborder" valign="top" width="16.666666666666664%">The package to be decompressed. The format must be specified. Otherwise, the package will be defined as not exist.</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63295mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">password</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Password of the file to be decompressed</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63309mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">timeout</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Timeout interval(ms). After the execution of an atomic command fails, if the execution time does not exceed the set timeout period, the atomic command is retried until the set timeout period is exceeded.</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63323mcpsimp"><td class="cellrowborder" valign="top" width="16.666666666666664%">delay</td><td class="cellrowborder" valign="top" width="16.666666666666664%">number</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">-</td><td class="cellrowborder" valign="top" width="16.666666666666664%">Delay from the previous operation</td></tr></tbody></table>

**Output: none**

**Samples**

Run the following commands to decompress the D:\\pro\\test.zip package to the D:\\pro\\test directory:

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400632__table63342mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400632__row63347mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63354mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">D:\pro\test</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63360mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">D:\pro\test.zip</td></tr></tbody></table>

Run the following commands to decompress the D:\\pro\\test.tar.gz package to the D:\\pro\\test directory:

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400632__table63367mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400632__row63372mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63379mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">D:\pro\test</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63385mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">D:\pro\test.tar.gz</td></tr></tbody></table>

Run the following commands to decompress the D:\\pro\\test.tar package to the D:\\pro\\test directory:

<table cellpadding="4" cellspacing="0" summary="" id="EN-US_TOPIC_0000002521400632__table63392mcpsimp" frame="border" border="1" rules="all"><colgroup><col style="width:5000%"> <col style="width:5000%"></colgroup><tbody><tr id="EN-US_TOPIC_0000002521400632__row63397mcpsimp"><td class="cellrowborder" valign="top" width="50%">Param</td><td class="cellrowborder" valign="top" width="50%">Value</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63404mcpsimp"><td class="cellrowborder" valign="top" width="50%">target</td><td class="cellrowborder" valign="top" width="50%">D:\pro\test</td></tr><tr id="EN-US_TOPIC_0000002521400632__row63410mcpsimp"><td class="cellrowborder" valign="top" width="50%">value</td><td class="cellrowborder" valign="top" width="50%">D:\pro\test\test.tar</td></tr></tbody></table>

The usage example is as follows:

![[en-us_image_0000002521560956.png]]

**Parent topic:** [[File|File]]