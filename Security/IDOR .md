# IDOR 

Insecure Direct Object Reference  
a type of access control vulnerability

---

IDOR vulnerability의 예 
```
http://online-service.thm/profile?user_id=1000
http://online-service.thm/profile?user_id=1305
```
등으로 다른 유저의 정보를 볼 수 있는 경우 

---

### 확인 방법  

동일 사이트에 아이디를 두개 만들어서 
A아이디 유저만 볼 수 있는 페이지에서 A아이디를 로그아웃하고 B아이디로 로그인했을 때 A아이디 유저만 볼 수 있는 페이지가 그대로 볼 수 있는지 확인 


---
---

### Course
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
