# Common Directories



<img src="https://www.blackmoreops.com/wp-content/uploads/2015/06/Linux-file-system-hierarchy-v2.0-600px-blackMORE-Ops.png">

출처 : [Linux file system hierarchy v2.0](https://www.blackmoreops.com/2015/06/18/linux-file-system-hierarchy-v2-0/)


## /

Primary hierarchy root   
root directory of the entire file system hierarchy   
※ /root와 다르다 

## /etc
store system files that are used by your operating system


### /etc/passwd
show how your system stores the passwords for each user in encrypted formatting called sha512.
```
tryhackme@linux2:/$ head /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
```


## /home
Users’ home directories, containing saved files, personal settings, etc.
```
tryhackme@linux2:~$ ls /home/
tryhackme  ubuntu  user2
```


##/root
**Home** directory for the **root** user      
※ "/" 와 다르다.    
※ root 유저의 정보는 "/home/root"가 아니라 "/root"에 있다.




## /tmp
tmp : temporary   
is volatile and is used to store data that is only needed to be accessed once or twice   
once the computer is restarted, the contents of this folder are **cleared out**
is similar to how **RAM** on a computer works



## /var

var : variable data   
stores data that is frequently accessed or written by services or applications running on the system
   
For example, log files from running services and applications are written here (/var/log)
or other data that is not necessarily associated with a specific user
```
tryhackme@linux2:/$ ls /var
backups  crash  local  log   opt  snap   tmp
cache    lib    lock   mail  run  spool  www
```
---
참고 자료   
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)
[Linux file system hierarchy v2.0](https://www.blackmoreops.com/2015/06/18/linux-file-system-hierarchy-v2-0/)
