# ffuf

## Automated Discovery 

the process of using tools to discover content rather than doing it manually

---


## -w 
switch to specify the wordlist we are going to use

```
root@ip-10-10-25-144:~# ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.211.134/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.211.134/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

assets                  [Status: 301, Size: 178, Words: 6, Lines: 8]
contact                 [Status: 200, Size: 3108, Words: 747, Lines: 65]
customers               [Status: 302, Size: 0, Words: 1, Lines: 1]
development.log         [Status: 200, Size: 27, Words: 5, Lines: 1]
monthly                 [Status: 200, Size: 28, Words: 4, Lines: 1]
news                    [Status: 200, Size: 2538, Words: 518, Lines: 51]
private                 [Status: 301, Size: 178, Words: 6, Lines: 8]
robots.txt              [Status: 200, Size: 46, Words: 4, Lines: 3]
sitemap.xml             [Status: 200, Size: 1391, Words: 260, Lines: 43]
:: Progress: [4655/4655] :: Job [1/1] :: 4481 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
root@ip-10-10-25-144:~# 
```

## -H 
switch adds/edits a header (in this instance, the Host header)
```
user@machine$ ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.75.9

```

## -fs 
지정한 사이즈의 결과를 제외할 때   
적용 전 : 사이즈 2395가 너무 많다 

```
user@machine$ ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.75.9 

...
x-ray                   [Status: 200, Size: 2395, Words: 503, Lines: 52]
wingate                 [Status: 200, Size: 2395, Words: 503, Lines: 52]
zulu                    [Status: 200, Size: 2395, Words: 503, Lines: 52]
x                       [Status: 200, Size: 2395, Words: 503, Lines: 52]
...
```

사이즈 2395인 데이터를 제외하고 출력된다
```
root@ip-10-10-249-198:~# ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host:FUZZ.acmeitsupport.thm" -u http://10.10.75.9 -fs 2395

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.75.9
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt
 :: Header           : Host: FUZZ.acmeitsupport.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 2395
________________________________________________

delta                   [Status: 200, Size: 51, Words: 7, Lines: 1]
yellow                  [Status: 200, Size: 56, Words: 8, Lines: 1]
:: Progress: [1907/1907] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```


---

### References
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
