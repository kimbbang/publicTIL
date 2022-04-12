## ls 
Listing Files in Our Current Directory (ls)
```
root@ip-10-10-250-80:~# ls
Desktop    Instructions  Postman  Scripts            Tools
Downloads  Pictures      Rooms    thinclient_drives
```

### -a 
: Show ".hiddenfolder". Files and folders with "." are **hidden** files.
```
tryhackme@linux2:~$ ls -a
.hiddenfolder folder1
```
### -l 
: 상세정보 보기 
```
tryhackme@linux2:~$ ls -l  또는 
tryhackme@linux2:~$ ll
total 40
drwxr-xr-x 4 tryhackme tryhackme 4096 Apr  7 09:23 ./
drwxr-xr-x 5 root      root      4096 May  4  2021 ../
-rw-r--r-- 1 tryhackme tryhackme  220 May  4  2021 .bash_logout
-rw-r--r-- 1 tryhackme tryhackme 3771 May  4  2021 .bashrc
```

### -h
: human-readable :  4096 -> 4.0K
```
tryhackme@linux2:~$ ls -lh 또는 
tryhackme@linux2:~$ ll -h
total 40K
drwxr-xr-x 4 tryhackme tryhackme 4.0K Apr  7 09:23 ./
drwxr-xr-x 5 root      root      4.0K May  4  2021 ../
-rw-r--r-- 1 tryhackme tryhackme  220 May  4  2021 .bash_logout
-rw-r--r-- 1 tryhackme tryhackme 3.7K May  4  2021 .bashrc
```
### -R
ls -R : 모든 하위 디렉토리 정보   
ls -R /디렉토리경로: /디렉토리경로부터 하위 디렉토리 정보

---
참고 자료   
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)


