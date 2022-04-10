# The ARP Protocol

Address Resolution Protocol    
allows a device to associate its MAC address with an IP address on the network    
find the MAC address (and therefore the physical identifier) of a device for communication.    

### cache 
Each device within a network has **a ledger to store information on**    
this cache stores the identifiers of other devices on the network.    

### ARP Request, ARP Reply
When an **ARP request** is sent, a message is broadcasted to every other device found on a network by the device, asking whether or not the device's MAC address matches the requested IP address.
If the device does have the requested IP address, an **ARP reply** is returned to the initial device to acknowledge this. 
The initial device will now remember this and store it within its cache (an ARP entry). 


---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
