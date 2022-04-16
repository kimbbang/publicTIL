## ps

Processes are the programs that are **running** on your machine.

They are managed by the kernel, where each process will have an ID associated with it, also known as its PID.   
The PID increments for the order In which the process starts.   

The process with an ID of 0 is a process that is started when the system boots.  
I.e. the 60th process will have a PID of 60.  

### ps : a list of the running processes as our user's session

```
root@ip-10-10-202-228:~# ps
  PID TTY          TIME CMD
 2566 pts/0    00:00:00 bash
10685 pts/0    00:00:00 ps
```

### ps aux : To see the processes run by other users and those that don't run from a session (i.e. system processes)
```
root@ip-10-10-202-228:~# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2 160396  9620 ?        Ss   05:15   0:03 /sbin/init
root         2  0.0  0.0      0     0 ?        S    05:15   0:00 [kthreadd]
rtkit     4255  0.0  0.0 183508  3056 ?        SNsl 05:37   0:00 /usr/lib/rtkit/r
```

---
### References
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
