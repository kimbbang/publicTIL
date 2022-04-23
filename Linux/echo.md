# echo

Output any text that we provide
다음에 오는 문구를 그대로 출력한다.

---

예 1 - 잘못사용하는 예 
결과를 항상 출력하기 때문에 해당 디렉토리에 data.tt파일이 없어도 출력함 
```
bandit11@bandit:~$ echo data.tt
data.tt
bandit11@bandit:~$ echo data.txt
data.txt
```

예 2 - 제대로 사용 
```
bandit11@bandit:~$ echo "Gur cnffjbeq vf RGr8LQqetPEsPk8htqjhRK8XSP6xORHh" | tr 'N-ZA-Mn-za-m' 'A-Za-z'
The password is ETe8YDdrgCRfCx8ugdwuEX8KFC6kBEUu
```



예3 
```
tryhackme@linux1:~$ echo "Hello Friend!"
Hello Friend!

tryhackme@linux1:~$ echo Hello
Hello

$ echo "'Hello world'"
'Hello world'

$ echo '"Hello world"'
"Hello world"
```

---
---
### Course
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
[overthewire - Bandit Level 11 → Level 12](https://overthewire.org/wargames/bandit/bandit12.html)
