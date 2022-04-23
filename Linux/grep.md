# grep
Using "grep" to find any entries with the IP address of "81.143.211.90" in "access.log"

---
예 
```
tryhackme@linux1:~$ grep "81.143.211.90" access.log
81.143.211.90 - - [25/Mar/2021:11:17 + 0000] "GET / HTTP/1.1" 200 417 "-" "Mozilla/5.0 (Linux; Android 7.0; Moto G(4))"
tryhackme@linux1:~$
```

---

## 두 패턴 이상 

### A 또는 B
[phoenixnap - How to Grep for Multiple Strings, Patterns or Words](https://phoenixnap.com/kb/grep-multiple-strings)

```
grep 'pattern1\|pattern2' fileName_or_filePath
```
```
bandit6@bandit:/$ ls -lRa ./ | grep 'bandit6\|bandit7'
```
```
dr-xr-xr-x 2 bandit6 bandit6 0 Apr 22 16:00 attr
-rw-r----- 1 bandit7 bandit6      33 May  7  2020 bandit7.password
```



### A와 B 모두 포함하기 
[stackoverflow - How to grep for two words existing on the same line?](https://stackoverflow.com/questions/6480687/how-to-grep-for-two-words-existing-on-the-same-line)
```
bandit6@bandit:/$ ls -lRa ./ | grep -E 'bandit6.*bandit7|bandit7.*bandit6'
```

---

## 키워드가 있는 문장의 위/아래 문장 포함해서 보여주기 
[stackoverflow - How can I make grep print the lines below and above each matching line?](https://stackoverflow.com/questions/1072643/how-can-i-make-grep-print-the-lines-below-and-above-each-matching-line)

윗 문장 포함 : grep -B 라인수  
아래 문장 포함 : grep -A 라인수
```
root@ip-10-10-74-103:~# nmap -h | grep format
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  
root@ip-10-10-74-103:~# nmap -h | grep -B 1 format
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
```


---
---

### Course
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
[OverTheWire - Bandit Level 6 → Level 7](https://overthewire.org/wargames/bandit/bandit7.html)
