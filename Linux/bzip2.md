# bzip2 

## decompression 
```
$ bzip2 -d input.txt.bz2
```
```
bandit12@bandit:/tmp/test$ file test
test: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/test$ bzip2 -d test
bzip2: Can't guess original name for test -- using test.out

bandit12@bandit:/tmp/test$ ls
data.txt  test.out

bandit12@bandit:/tmp/test$ head test.out                                       P▒^data4.bin▒▒=H▒▒�F:t0E▒D4)rgri▒KPZ▒RNp▒H3($q   ▒▒▒Ej▒LRl▒▒▒t▒M5▒▒▒=+ةZ▒▒Y▒▒▒y▒▒▒▒▒▒▒~▒▒(▒▒{S▒z▒u▒z|▒▒hחBQUk(dE܃▒X<▒e▒▒u▒▒#▒k▒▒{▒▒▒▒▒▒ο▒▒▒C▒+ܨ▒▒▒T▒.bb▒r▒0▒▒▒▒▒h$▒▒3▒▒"▒|▒j▒jTȢY▒Ŕ▒▒Q▒▒▒a▒▒▒▒▒▒#▒▒|▒Q▒Q▒9+綜3a񼯲▒rU*▒#%▒▒▒▒q3▒$▒▒▒
%▒U▒y~,tz▒xS▒04▒6ߥ▒kBC▒▒=▒me▒"▒▒kGdEo?n▒,mo▒▒O▒Sz6▒8▒▒T▒[▒▒\fҐ~▒c.▒Ӵ▒*▒:Ӿo▒▒Ċm▒k▒▒▒,▒▒
▒
 ▒Pbandit12@bandit:/tmp/test$ PuTTYPuTTYPuTTYPuTTY^C

bandit12@bandit:/tmp/test$ file test.out
test.out: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

---
---
### Course 
[OverTheWire - Bandit Level 12 → Level 13](https://overthewire.org/wargames/bandit/bandit13.html)

### References  
[geeksforgeeks - bzip2 command in Linux with Examples](https://www.geeksforgeeks.org/bzip2-command-in-linux-with-examples/)