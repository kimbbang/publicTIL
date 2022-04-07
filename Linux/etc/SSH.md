## SSH
Secure Shell   
is a protocol between devices in an **encrypted** form   
allows us to **remotely** execute commands on another device remotely.

---
TEST 
   
IP Address : 10.10.70.45   
ID : tryhackme   
PW : tryhackme   

```
ssh tryhackme@10.10.70.45
```

```
root@ip-10-10-210-47:~# ssh tryhackme@10.10.97.114
The authenticity of host '10.10.97.114 (10.10.97.114)' can't be established.
ECDSA key fingerprint is SHA256:q9mc4q3HZCYyv5JxXGUvNdnuOtKXK27QN6FfIrxvkkE.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.97.114' (ECDSA) to the list of known hosts.
tryhackme@10.10.97.114's password: 
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-1047-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Apr  7 09:23:27 UTC 2022

  System load:  0.24              Processes:             110
  Usage of /:   26.8% of 7.69GB   Users logged in:       0
  Memory usage: 23%               IPv4 address for eth0: 10.10.97.114
  Swap usage:   0%

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

tryhackme@linux2:~$ 

```
---
참고 자료   
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)


