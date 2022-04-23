# cat	
Outputting the Contents of a File (cat)

## 파일 이름이 -인 파일은 "cat -"로 열리지 않는다 
```
bandit1@bandit:~$ ls -l
total 4
-rw-r----- 1 bandit2 bandit1 33 May  7  2020 -
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

## 파일 내용 출력시 cat
echo data.txt는 "data.txt"를 반환하기 때문에 "data.txt"가 인코딩(디코딩)되었다. 

```
bandit11@bandit:~$ echo data.txt | tr  'A-Za-z' 'N-ZA-Mn-za-m'
qngn.gkg

bandit11@bandit:~$ cat data.txt | tr  'A-Za-z' 'N-ZA-Mn-za-m'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

---
---
### Course
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
[OverTheWire - Bandit Level 1 → Level 2](https://overthewire.org/wargames/bandit/bandit2.html)  
[overthewire - Bandit Level 11 → Level 12](https://overthewire.org/wargames/bandit/bandit12.html)

### References  

[tldp - Chapter 3. Special Characters](https://tldp.org/LDP/abs/html/special-chars.html)