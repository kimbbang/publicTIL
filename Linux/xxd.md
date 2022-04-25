# xxd 

xxd - make a hexdump or do the reverse.

---

## ```xxd -r <inputFile> <outputFile>```
convert a hex dump back to its original BINARY form

```
bandit12@bandit:/tmp/test$ head data.txt
00000000: 1f8b 0808 0650 b45e 0203 6461 7461 322e  .....P.^..data2.
00000010: 6269 6e00 013d 02c2 fd42 5a68 3931 4159  bin..=...BZh91AY
00000020: 2653 598e 4f1c c800 001e 7fff fbf9 7fda  &SY.O...........
00000030: 9e7f 4f76 9fcf fe7d 3fff f67d abde 5e9f  ..Ov...}?..}..^.
00000040: f3fe 9fbf f6f1 feee bfdf a3ff b001 3b1b  ..............;.
00000050: 5481 a1a0 1ea0 1a34 d0d0 001a 68d3 4683  T......4....h.F.
00000060: 4680 0680 0034 1918 4c4d 190c 4000 0001  F....4..LM..@...
00000070: a000 c87a 81a3 464d a8d3 43c5 1068 0346  ...z..FM..C..h.F
00000080: 8343 40d0 3400 0340 66a6 8068 0cd4 f500  .C@.4..@f..h....
00000090: 69ea 6800 0f50 68f2 4d00 680d 06ca 0190  i.h..Ph.M.h.....

bandit12@bandit:/tmp/test$ file data.txt
data.txt: ASCII text

bandit12@bandit:/tmp/test$ xxd -r data.txt test
bandit12@bandit:/tmp/test$ ls
data.txt  test

bandit12@bandit:/tmp/test$ head test                                           P▒^data2.bin=▒▒BZh91AY&SY▒O▒▒Ov▒▒▒}?▒▒}▒▒^▒▒▒▒▒▒▒▒▒ߣ▒▒;▒▒▒▒4▒▒h▒F▒F▒▒4LM
@▒▒z▒▒FM▒▒C▒hF▒C@▒4@f▒▒h
4hh▒=C%▒>X,▒k▒▒▒1▒▒GY▒▒
▒J▒쌑Oϊ▒▒{RBp▒Qix▒Y▒Z!d▒▒j▒(▒搿ݳ▒▒/▒▒A▒#▒A▒▒0P▒▒v▒▒`▒"3▒

▒▒d▒bX?▒▒z▒▒2▒▒<▒▒A ▒n}
5(3A▒▒
wO▒R▒▒▒▒6▒XS{▒
▒▒9?L▒P▒yB▒▒=z▒m?▒L▒Nt*▒7{qP▒▒̜▒%"▒w9▒qm4▒ N3▒6▒▒▒K▒▒H䋑[▒▒}!
                                                            d▒▒3A4$▒M~▒\ɠJ▒C▒kUƦ\▒▒▒\▒FSN▒▒&=▒[▒▒q      \)▒$:▒▒H▒t&/▒(▒▒▒▒]▒▒BB9<s ▒▒h=bandit12@bandit:/tmp/test$ PuTTY^C

bandit12@bandit:/tmp/test$ file test
test: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```







---
---
### Course 
[OverTheWire - Bandit Level 12 → Level 13](https://overthewire.org/wargames/bandit/bandit13.html)

### References  
[linux.die - Linux man page](https://linux.die.net/man/1/xxd)