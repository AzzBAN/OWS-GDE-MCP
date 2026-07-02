---
title: "Lock"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/runscript_js_025.html"
depth: 7
---
# Lock

In JavaScript, Lock can be used to implement the lock operation so that a script can be mutually exclusive when it is executed concurrently.

**Table 1** Lock API description   
| API | Description | Example |
| :-- | :-- | :-- |
| Lock.acquire(lockName, ttl) | Attempt to add a lock. If the lock with the same name has been occupied by a node or thread, the lock fails to be added. After the lock is added, release the lock in a timely manner after being used. Parameters:
-   **lockName**: Lock name, which is a string. The lock name must be unique in the running app of the current tenant.
-   **ttl**: Number type, in seconds. The value is an integer. The maximum value is 120 seconds.

Return value: It is in boolean type. true indicates that the lock is successfully obtained. Otherwise, the operation fails. | var lockName = "lockIpModel";
var locked = false;
try {
    locked = Lock.acquire(lockName, 60);
    if (!locked) {
        do\_without\_lock();
    } else {
        do\_with\_lock();
    }
} finally {
    if (locked) {
        Lock.release(lockName);
    }
}

 |
| Lock.release(lockName) | Used to release a lock. When you release a lock that does not exist or has been released, no effect is achieved and no error occurs. Parameter:

-   **lockName**: Lock name, which is a string.

Returned value: None | ![[note_3.0-en-us.png]]

After a lock is added, the validity period of the lock lasts until the script execution is complete. If a lock is not explicitly released in JavaScript, the lock can be used across scripts and the added lock cannot be used by a script for multiple times.

**Parent topic:** [[Service APIs|Service APIs]]