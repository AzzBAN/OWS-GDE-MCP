---
title: "Rule: Ansible, MML, or SSH Cannot Be Used to Run Risky Commands That May Affect the Normal Running of the Target Network"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001348963864.html"
depth: 5
---
# Rule: Ansible, MML, or SSH Cannot Be Used to Run Risky Commands That May Affect the Normal Running of the Target Network

**Description**: You can use Ansible, MML, or SSH to orchestrate and execute maintenance commands for the target network. The execution of some maintenance commands may cause running exceptions on the target network, such as configuration deletion and modification, hardware device restart, and software link reset and blocking.

**Check guide**: Check whether the Ansible playbook and command activities contain commands that may affect the normal running of devices on the target network by referring to the product manuals of related devices on the target network, and evaluate the risks caused by the execution of the commands. For example:

1.  Check whether Linux service operations include risky operation commands such as **reboot**, **shutdown**, **halt**, **poweroff**, and **rm \***.
2.  Check whether operations on IP routers and switches include risky commands such as **shutdown**, **undo**, and **reboot**.
3.  Check whether operations on core network and wireless network devices include risky operation commands, such as **RST BRD**, **RMV** _\*\*\*_, and **DEA** _\*\*\*_.

**Positive example**: You run the **display health** command through the SSH command activity to query the router health status.

<HUAWEI> **display health**

\----------------------------------------------------------------

Slot CPU Usage Memory Usage(Used/Total)

\----------------------------------------------------------------

9 MPU(Master) 4% 21% 438MB/1995MB

7 LPU 5% 34% 1147MB/3324MB

11 SFU 9% 11% 27MB/244MB

12 SFU 6% 11% 27MB/244MB

10 MPU(Slave) 2% 17% 347MB/1995MB

\----------------------------------------------------------------

**Negative example**: Run the **board slot** command through the SSH command to restart the board.

<HUAWEI> reset slot 1

Caution!!! Confirm to reset slot 1! Continue? \[Y/N\]:y

Warning: Board 1 is being reset.

**Exception scenarios**: In the following special scenarios, risky commands may need to be executed. After you fully evaluate the risks, configure a command whitelist to execute risky commands.

1.  The device is not officially brought online. During initial commissioning, risky commands, such as configuration deletion and restart commands, are executed.
2.  Risky commands, such as configuration deletion and modification commands, are executed on devices during the cutover.

**Tool supported or not**: yes

**Specification name**: Security\_MaliciousOperations\_Forbid\_NetworkDaggerCommand

**Category**: non-bottom-line check item

**Severity**: minor

**Orchestration scenario**: network automation orchestration

**Parent topic:** [[Protection Against Malicious Operations|Protection Against Malicious Operations]]