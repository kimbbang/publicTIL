## scp
Transferring Files  

Secure copy, or SCP, is just that -- a means of **securely** copying files.

Unlike the regular cp command, this command allows you to transfer files **between two computers** **using the SSH protocol** to provide both authentication and encryption.

### local > remote
```
scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt
```
important.txt : Name of the file on the **local** system  
ubuntu : User on the **remote** system  
192.168.1.30 : The IP address of the **remote** system 	  
transferred.txt : Name that we wish to store the file as on the **remote** system	  

### remote > local 
```
scp ubuntu@192.168.1.30:/home/ubuntu/documents.txt notes.txt
```
192.168.1.30 : IP address of the **remote** system  
ubuntu : User on the **remote** system  
documents.txt : Name of the file on the **remote** system  
notes.txt : Name that we wish to store the file as on our **local** system  




---
### References
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
