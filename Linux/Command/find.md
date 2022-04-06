


## find
Using "find" to find a file with the name of "Reflections.java"
```
root@ip-10-10-223-7:~# pwd
/root
root@ip-10-10-223-7:~# find -name Reflections.java
./Rooms/solar/marshalsec/src/main/java/marshalsec/util/Reflections.java
```
Using "find" to find any file with the extension of ".java"
```
root@ip-10-10-223-7:~# find -name *.java
./.java
./Rooms/solar/marshalsec/src/test/java/GadgetsTest.java
./Rooms/solar/marshalsec/src/main/java/marshalsec/BlazeDSBase.java
./Rooms/solar/marshalsec/src/main/java/marshalsec/EscapeType.java
...
```
이름에 password를 포함한 파일 
```
root@ip-10-10-223-7:~# find -name *password*
./Rooms/ctf-event-2022/FindThePassword/findthepassword.pcap
./Rooms/BreachingAD/task5/passwordlist.txt
./Rooms/BreachingAD/task3/passwordsprayer.zip
```

---

[TryHackMe - Module Linux Fundamentals Part 1](https://tryhackme.com/)


