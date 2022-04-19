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
### References
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)      
[geeksforgeeks - curl command in Linux with Examples](https://www.geeksforgeeks.org/curl-command-in-linux-with-examples/)  
