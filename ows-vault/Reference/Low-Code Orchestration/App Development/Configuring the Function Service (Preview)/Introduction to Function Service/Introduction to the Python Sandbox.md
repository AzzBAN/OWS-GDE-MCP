---
title: "Introduction to the Python Sandbox"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_faas_017.html"
depth: 4
---
#### Python 3.8

The sandbox is implemented in Python 3.8 using the blacklist mode. Some subclasses or functions that cannot be used by third-party software are list in [Table 1](#EN-US_TOPIC_0000001487387094__table1763191285017).

**Table 1** Blacklist in Python 3.8   
| No. | Third-Party Software Name | Forbidden Subclass or Function |
| :-- | :-- | :-- |
| 1 | httplib2 | Http.request |
| 2 | multiprocessing | Process, and Pool |
| 3 | os | renames, system, fork, and popen |
| 4 | pycurl | Curl |
| 5 | requests | request, get, options, post, head, put, patch, and delete |
| 6 | subprocess | run, check\_call, getstatusoutput, getoutput, Popen, and call |
| 7 | threading | Thread.start |
| 8 | urllib | request.urlopen |
| 9 | urllib3 | PoolManager.urlopen |