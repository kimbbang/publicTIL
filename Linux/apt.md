# apt

Normally we use the apt command to install software onto our Ubuntu system.
데비안 GNU/리눅스 배포판 계열 배포판에서 소프트웨어를 설치하고 제거하는 일을 한다

[어드밴스트 패키징 툴](https://ko.wikipedia.org/wiki/%EC%96%B4%EB%93%9C%EB%B0%B4%EC%8A%A4%ED%8A%B8_%ED%8C%A8%ED%82%A4%EC%A7%95_%ED%88%B4)

-----

## /etc/apt
When developers wish to submit software to the community, they will submit it to an  "apt" repository. 
```
tryhackme@linux3:~$ ls /etc/apt
apt.conf.d   preferences.d  sources.list.d
auth.conf.d  sources.list   trusted.gpg.d
```

---

[debian manuals](https://www.debian.org/doc/manuals/apt-howto/)


## install 

1.download the GPG key and use apt-key to trust it:  
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

※ GPG (Gnu Privacy Guard) keys
When adding software, the integrity of what we download is guaranteed by the use of GPG


2.setting 

```
tryhackme@linux3:~$ cd /etc/apt/sources.list.d/

touch sublime-text.list
    # inside sublime-text.list file
    deb https://download.sublimetext.com/ apt/stable

apt update
apt install sublime-text
```

## remove
```
add-apt-repository --remove ppa:PPA_Name/ppa
    or
apt remove sublime-text
```




---
### References
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
