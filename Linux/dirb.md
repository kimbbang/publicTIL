# Automated Discovery 

the process of using tools to discover content rather than doing it manually

---


## dirb
```
root@ip-10-10-25-144:~# dirb http://10.10.211.134/user/share/wordlists/SecLists/Discovery/Web-content/common.txt

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Tue Apr 19 05:19:15 2022
URL_BASE: http://10.10.211.134/user/share/wordlists/SecLists/Discovery/Web-content/common.txt/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.10.211.134/user/share/wordlists/SecLists/Discovery/Web-content/common.txt/ ----
                                                                               ontent/common.txt/zt 
-----------------
END_TIME: Tue Apr 19 05:19:20 2022
DOWNLOADED: 4612 - FOUND: 0
root@ip-10-10-25-144:~# 
```

---

### References
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
