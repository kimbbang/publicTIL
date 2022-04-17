# Firewall

a device **within** a network responsible for **determining** what traffic is allowed to enter and exit.

performs packet inspection to determine

firewalls operate at layer 3, layer 2 of the OSI model



---
### How to open

#### Firewall & network protection

Settings > Update & Security > Windows Security > Firewall & network protection


#### Windows Defender Firewall

* Settings > Update & Security > Windows Security > Firewall & network protection > Advanced settings 
* run > WF.msc

[Best practices for configuring Windows Defender Firewall](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/best-practices-configuring)

---

## Firewall Category

### Stateful
모든 트래픽 감시   
This type of firewall uses the **entire information from a connection**;      

This firewall type **consumes many resources** in comparison to stateless firewalls as the decision making is dynamic.   
For example, a firewall could allow the first parts of a TCP handshake that would later fail.  

If a connection from a host is bad, it will block the entire device.  

### Stateless
미리 지정한 규칙에 따라 개별(지정한) 트래픽만 감시  
This firewall type uses **a static set of rules** to determine whether **individual packets** are acceptable or not.      
For example, a device sending a bad packet will **not** necessarily mean that the entire device is then blocked.  

If a rule is not exactly matched, it is effectively useless.  

---






### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)    
[TryHackMe - Windows Fundamentals](https://tryhackme.com/module/windows-fundamentals)
