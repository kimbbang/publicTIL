# Automated Discovery 

the process of using tools to discover content rather than doing it manually

---

# gobuster

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
