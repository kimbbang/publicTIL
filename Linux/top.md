## top

### top : real-time statistics about the processes running on your system

These statistics will refresh every 10 seconds

```
root@ip-10-10-202-228:~# top

top - 07:09:29 up  1:53,  0 users,  load average: 0.01, 0.04, 0.00
Tasks: 190 total,   1 running, 145 sleeping,   0 stopped,   0 zombie
%Cpu(s):  3.4 us,  0.3 sy,  0.0 ni, 96.0 id,  0.0 wa,  0.0 hi,  0.2 si,  0.2 st
KiB Mem :  4037452 total,   932384 free,   632624 used,  2472444 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  3087308 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND      
1131 root      20   0  253032  95468  28856 S   6.0  2.4   3:14.27 Xvnc         
10567 root      20   0  188472  27992   7404 S   1.7  0.7   0:04.87 python
```

---
### References
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
