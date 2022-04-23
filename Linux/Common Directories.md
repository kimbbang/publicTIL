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

### /etc/profile

controls system-wide default variables, such as Export variables, File creation mask (umask), Terminal types, Mail messages to indicate when new mail has arrived



### /etc/shadow

contains information about the system's users' passwords


### /etc/issue

contains a message or system identification to be printed before the login prompt.

---

## /home
Users’ home directories, containing saved files, personal settings, etc.
```
tryhackme@linux2:~$ ls /home/
tryhackme  ubuntu  user2
```

---


### /proc/version

specifies the version of the Linux kernel

---

## /root
**Home** directory for the **root** user      
※ "/" 와 다르다.    
※ root 유저의 정보는 "/home/root"가 아니라 "/root"에 있다.


### /root/.bash_history
contains the history commands for root user


### /root/.ssh/id_rsa

Private SSH keys for a root or any known valid user on the server


---

## /tmp
tmp : temporary   
is volatile and is used to store data that is only needed to be accessed once or twice   
once the computer is restarted, the contents of this folder are **cleared out**
is similar to how **RAM** on a computer works


---

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

### /var/log
fail2ban.log : is used to monitor attempted brute forces
ufw.log : is used as a firewall

```
ryhackme@linux3:/var/log$ ls
alternatives.log    btmp.1                 dmesg.3.gz  lastlog
alternatives.log.1  cloud-init-output.log  dmesg.4.gz  private
amazon              cloud-init.log         dpkg.log    syslog
apache2             dist-upgrade           dpkg.log.1  syslog.1
apt                 dmesg                  journal     unattended-upgrades
auth.log            dmesg.0                kern.log    wtmp
auth.log.1          dmesg.1.gz             kern.log.1
btmp                dmesg.2.gz             landscape
tryhackme@linux3:/var/log$ 
```

### /var/log/apache2
apache2 : Apache2 web server
```
tryhackme@linux3:/var/log/apache2$ ls
access.log  access.log.1  error.log  error.log.1  other_vhosts_access.log

tryhackme@linux3:/var/log/apache2$ cat access.log.1
10.9.232.111 - - [04/May/2021:18:18:16 +0000] "GET /catsanddogs.jpg HTTP/1.1" 200 51395 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
```

### /var/log/apache2/access.log

the accessed requests for Apache  webserver


### /var/log/dmessage

contains global system messages, including the messages that are logged during system startup


### /var/mail/root

all emails for root user



---
---

### Course
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)

### References
[Linux file system hierarchy v2.0](https://www.blackmoreops.com/2015/06/18/linux-file-system-hierarchy-v2-0/)
