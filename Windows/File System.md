# Windows

## File System

* **NTFS** : New Technology File System   
is known as a **journaling** file system : In case of a failure, the file system can **automatically repair** the folders/files on disk using information stored in a log file   


* Set specific **permissions** on folders and files   
Check permissions : Properties > Security > Group or user names    
[File and Folder Permissions](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727008(v=technet.10)?redirectedfrom=MSDN)   
   

* Alternate Data Streams (**ADS**).   
are a file attribute only found on the NTFS file system.   
Every file has at least one data stream ($DATA), and ADS allows files to contain more than one stream of data.   
[Introduction to Alternate Data Streams](https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/)   


* Supports files larger than 4GB   
Folder and file compression   
Encryption (Encryption File System or EFS)   
※Before NTFS, there was **FAT16/FAT32** (File Allocation Table) and **HPFS** (High Performance File System).    
FAT partitions in USB devices, MicroSD cards, etc   
[Overview of FAT, HPFS, and NTFS File Systems](https://docs.microsoft.com/en-us/troubleshoot/windows-client/backup-and-storage/fat-hpfs-and-ntfs-file-systems)   

---

## Windows\System32 Folders

#### C:\Windows 
: contains the Windows operating system.    

#### C:\Windows\System32 
: holds the important files that are critical for the operating system.   
[What is the System32 Directory?](https://www.howtogeek.com/346997/what-is-the-system32-directory-and-why-you-shouldnt-delete-it/)   


#### **%windir%** 
: the system  environment variable for the Windows directory   

Environment variables store information about the operating system environment.   
[Environment variables](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.1)   

---

### C:\boot.ini

contains the boot options for computers with BIOS firmware


---
---

### Course
[TryHackMe - Windows Fundamentals](https://tryhackme.com/module/windows-fundamentals)  
[TryHackMe - Introduction to Web Hacking](https://tryhackme.com/module/intro-to-web-hacking)    
