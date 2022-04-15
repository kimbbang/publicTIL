# VPN

Virtual Private Network

is a technology that allows devices on separate networks to communicate securely by creating a dedicated path between each other over the Internet (known as a tunnel).   
Devices connected within this tunnel form their own private network.   

VPN technology uses encryption to protect data.

---
## VPN Technology

### PPP
**encrypts** & provides the **authentication** of data

is used by PPTP (explained below) to allow for authentication and provide encryption of data.     
VPNs work by using a private key and public certificate (similar to SSH).     
A private key & certificate must match for you to connect.    

This technology is not capable of leaving a network by itself (non-routable).    

### PPTP
**Point-to-Point Tunneling Protocol**    
allows the data from PPP to travel and leave a network.    

is very easy to set up and is supported by most devices.     
It is, however, **weakly encrypted** in comparison to alternatives.    

### IPSec
**Internet Protocol Security**
**encrypts** data using the existing **Internet Protocol (IP) framework.**    
IPSec is difficult to set up in comparison to alternatives;    
however, if successful, it boasts strong encryption and is also supported on many devices.   




---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)    
