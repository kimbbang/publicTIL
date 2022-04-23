# traceroute 
be used to map the path your request takes as it heads to the target machine.

 ※ windows : tracert

---



```
root@ip-10-10-230-195:~# traceroute tryhackme.com
traceroute to tryhackme.com (172.67.27.10), 30 hops max, 60 byte packets
 1  ec2-79-125-1-171.eu-west-1.compute.amazonaws.com (79.125.1.171)  7.465 ms ec2-79-125-1-179.eu-west-1.compute.amazonaws.com (79.125.1.179)  6.540 ms ec2-79-125-0-20.eu-west-1.compute.amazonaws.com (79.125.0.20)  10.216 ms
 2  100.66.8.130 (100.66.8.130)  20.276 ms 100.65.22.192 (100.65.22.192)  13.362 ms 100.66.8.248 (100.66.8.248)  18.973 ms
 3  * 100.66.10.14 (100.66.10.14)  13.644 ms 100.66.11.128 (100.66.11.128)  14.134 ms
 ```
---

## -i
specify an interface 

## -T
use TCP SYN requests



---
---

### Course


[TryHackMe - Network Exploitation Basics](https://tryhackme.com/module/intro-to-networking)    

### References
[computerhope - Linux traceroute command](https://www.computerhope.com/unix/utracero.htm)