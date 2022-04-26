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

## gobuster

directory discovery tool  
GoBuster is a tool used to brute-force URIs (directories and files), DNS subdomains and virtual host names. 

```
root@ip-10-10-25-144:~# gobuster dir --url http://10.10.211.134/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
    OR 
root@ip-10-10-25-144:~# gobuster dir -u http://10.10.211.134/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt

===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.211.134/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/19 05:21:41 Starting gobuster
===============================================================
/assets (Status: 301)
/contact (Status: 200)
/customers (Status: 302)
/development.log (Status: 200)
/monthly (Status: 200)
/news (Status: 200)
/private (Status: 301)
/robots.txt (Status: 200)
/sitemap.xml (Status: 200)
===============================================================
2022/04/19 05:21:43 Finished
===============================================================
root@ip-10-10-25-144:~# 
```



---

### References
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
