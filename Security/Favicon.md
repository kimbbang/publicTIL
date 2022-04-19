# Favicon

The favicon is a small icon displayed in the browser's address bar or tab used for branding a website.

if the website developer doesn't replace this with a custom one, this can give us a clue on <u>what framework is in use</u>

---

## 실습 

파비콘 설정을 하지 않은 경우 프레임워크 알아내기

1. 웹 브라우저에서 타겟 사이트에 방문해서 파비콘이 없는지 확인   

    예: https://static-labs.tryhackme.cloud/sites/favicon/
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Welcome to my webpage!</title>
        <link rel="shortcut icon" type="image/jpg" href="images/favicon.ico"/>
    </head>
    <body>
    Website coming soon....
    </body>
    </html>
    ```

2. 파비콘의 md5 해쉬 값 알아내기 
    ```
    root@ip-10-10-41-144:~# curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100  1406  100  1406    0     0  10732      0 --:--:-- --:--:-- --:--:-- 10732
    f276b19aabcb4ae8cda4d22625c6735f  -
    root@ip-10-10-41-144:~# 
    ```
3. 알아낸 해쉬값을 OWASP 파이콘 데이터베이스에서 검색
    ```
    ...
    09f5ea65a2d31da8976b9b9fd2bf853c:caudium (1.4.12)
    f276b19aabcb4ae8cda4d22625c6735f:cgiirc (0.5.9)   <<<
    a18421fbf34123c03fb8b3082e9d33c8:chora2 (2.0.2) 
    ...
    ```
    [OWASP favicon database](
    https://wiki.owasp.org/index.php/OWASP_favicon_database)

4. 사용하는 프레임워크 : cgiirc

---

### References
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
