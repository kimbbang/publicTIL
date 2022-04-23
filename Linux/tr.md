# tr 

tr 변경전 변경후  
"변경전" 문자 셋의 수와 "변경후" 문자 셋의 수가 같아야 한다   


---

[geeksforgeeks - tr command in Unix/Linux with examples](https://www.geeksforgeeks.org/tr-command-in-unix-linux-with-examples/)
```
$cat greekfile
WELCOME TO 
GeeksforGeeks

$cat greekfile | tr “[a-z]” “[A-Z]”
WELCOME TO
GEEKSFORGEEKS
```

---

## ROT13

출처 : [위키피디아 - ROT13](https://en.wikipedia.org/wiki/ROT13)
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/ROT13_table_with_example.svg/1280px-ROT13_table_with_example.svg.png">


A-M 은 N-Z,   
N-Z 는 A-M로 바뀐 상태 

```
bandit11@bandit:~$ echo "Hello" | tr A-MN-Za-mn-z N-ZA-Mn-za-m
Uryyb
bandit11@bandit:~$ echo "Uryyb" | tr A-MN-Za-mn-z N-ZA-Mn-za-m
Hello
```

A-MN-Z는 A-Z,   
a-mn-z는 a-z 와 같기 때문에 아래도 같은 결과가 나온다
```
bandit11@bandit:~$ echo "Hello" | tr A-Za-z N-ZA-Mn-za-m
Uryyb
```

변경전, 변경후가 1:1로 대응되기때문에  아래도 같은 결과가 나온다
```
bandit11@bandit:~$ echo "Hello" | tr N-ZA-Mn-za-m A-Za-z
Uryyb
```






---
---

### Course
[overthewire - Bandit Level 11 → Level 12](https://overthewire.org/wargames/bandit/bandit12.html)