
## Subnetting

Subnet mask is represented as a number of four bytes (32 bits), ranging from 0 to 255 (0-255).   
Subnetting is the term given to **splitting up a network into smaller**, miniature networks within itself.   
---
## Subnets use IP addresses in three different ways:   

### the network address (192.168.1.0)   
: identifies the **start** of the actual network and is used to identify a network's existence.   
For example, a device with the IP address of 192.168.1.100 will be on the network identified by 192.168.1.0   

### the host address (192.168.1.100)   
identify devices within a network(=identify a device on the subnet)   
For example, a device will have the network address of 192.168.1.1   

### the default gateway (192.168.1.254)   
is a special address assigned to a device on the network that is capable of **sending information to another network**    
Any data that needs to go to a device that isn't on the same network (i.e. isn't on 192.168.1.0) will be sent to this device.        
These devices can use any host address but usually use either the first or last host address in a network (.1 or .254)   

---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
