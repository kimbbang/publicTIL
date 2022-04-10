
# The DHCP Protocol
DHCP (Dynamic Host Configuration Protocol)     
    
When a device connects to a network, if it has not already been manually assigned an IP address,     
device > DHCP server : [DHCP Discover] request to see if any DHCP servers are on the network    
device < DHCP server : [DHCP Offer] reply with an IP address the device could use      
device > DHCP server : [DHCP Request] reply confirming it wants the offered IP Address     
device < DHCP server : [DHCP ACK] reply acknowledgement the device can start using the IP Address    


---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
