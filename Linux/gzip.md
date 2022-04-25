# gzip

## Compressing 
```
gzip filename
```

---

## Decompressing 
```
gzip -d filename.gz
    OR
gunzip filename.gz
```

```
bandit12@bandit:/tmp/test$ file test
test: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix

bandit12@bandit:/tmp/test$ gunzip test
gzip: test: unknown suffix -- ignored

bandit12@bandit:/tmp/test$ mv test test.gz
bandit12@bandit:/tmp/test$ gunzip test.gz
bandit12@bandit:/tmp/test$ ls
data.txt  test

bandit12@bandit:/tmp/test$ file test
test: bzip2 compressed data, block size = 900k
```

---
---
### Course 
[OverTheWire - Bandit Level 12 → Level 13](https://overthewire.org/wargames/bandit/bandit13.html)

### References 
[linuxize - Gzip Command in Linux](https://linuxize.com/post/gzip-command-in-linux/)