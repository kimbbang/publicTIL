


# file

## python 


메시지
```
file = open(경로생략)
PermissionError: [Errno 13] Permission denied:
```
디렉토리만 지정해서 파일을 열거나 쓰려고 할 때 발생  
아래 코드처럼 파일명이 있는지 확인할 것   
파일 여는 곳, 저장하는 곳 둘 다 확인할 것 
```
# Program to read the entire file (absolute path) using read() function
file = open("C:\\Projects\\Python\\Docs\python.txt", "r")
content = file.read()
print(content)
file.close()
```
[코드출처](https://itsmycode.com/python-permissionerror-errno-13-permission-denied/)
