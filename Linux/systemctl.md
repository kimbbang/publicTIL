## systemctl

allows us to interact with the systemd process/daemon

(Where ps only lists processes which are running,)  
systemctl lists which services are known, which can be managed by systemd and whether services are enabled.

#### options

* Start  
* Stop  
* Enable : to start the same service on the **boot-up** of the system  
* Disable  
```
systemctl [option] [service]
systemctl start apache2
systemctl stop apache2
```
```
tryhackme@linux3:~$ ps aux | grep myservice
tryhack+    1204  0.0  0.0   8160   740 pts/0    S+   06:29   0:00 grep --color=auto myservice
tryhackme@linux3:~$ systemctl stop myservice
```



---
### References
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)    
[What is Systemctl? An In-Depth Overview](https://www.liquidweb.com/kb/what-is-systemctl-an-in-depth-overview/#:~:text=The%20systemctl%20command%20is%20a,the%20System%20V%20init%20daemon.)

