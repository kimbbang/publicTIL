# tar

POSIX tar archive (GNU)

---

## Create 
c – Creates a new .tar archive file.  
v – Verbosely show the .tar file progress.  
f – File name type of the archive file.  
```
# tar -cvf tecmint-14-09-12.tar /home/tecmint/

/home/tecmint/
/home/tecmint/cleanfiles.sh
/home/tecmint/openvpn-2.1.4.tar.gz
/home/tecmint/tecmint-14-09-12.tar
/home/tecmint/phpmyadmin-2.11.11.3-1.el5.rf.noarch.rpm
/home/tecmint/rpmforge-release-0.5.2-2.el5.rf.i386.rpm
```

---

## Untar 
x – extract an archive file.  
v – Verbosely show the .tar file progress.    
f – File name type of the archive file.  
```
# tar -xvf public_html-14-09-12.tar

/home/public_html/videos/
/home/public_html/videos/views.php
/home/public_html/videos/index.php
/home/public_html/videos/logout.php
/home/public_html/videos/all_categories.php
/home/public_html/videos/feeds.xml
```







---
---
### Course 
[OverTheWire - Bandit Level 12 → Level 13](https://overthewire.org/wargames/bandit/bandit13.html)

### References  
[tecmint - 18 Tar Command Examples in Linux](https://www.tecmint.com/18-tar-command-examples-in-linux/#:~:text=The%20Linux%20%E2%80%9Ctar%E2%80%9D%20stands%20for,gzip%20and%20bzip%20in%20Linux.)
