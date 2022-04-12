# the OSI Model
Open Systems Interconnection Model   

## Layer 7 - Application

FileZilla : file server browsing software who provides a friendly, Graphical User Interface (GUI)   
DNS (Domain Name System): how website addresses are translated into IP addresses.   

## Layer 6 - Presentation
acts as a **translator** for data to and from the application layer (layer 7)   
**format** data   
in which standardisation starts to take place   
Security features such as data encryption (like HTTPS when visiting a secure site) occur at this layer   

## Layer 5 - Session
will begin to **create a connection** to the other computer that the data is destined for. (session)   
synchronises the two computers to ensure that they are on the same page before data is sent and received   
**divide up the data** sent into smaller chunks of data and begin to send these chunks (**packets**) one at a time   

## Layer 4 - Transport
transmitting data across a network
  
* TCP
* UDP   

## Layer 3 - Network

packets

routing & re-assembly of data   
everything is dealt with via **IP addresses**   
routing simply determines the most **optimal** path    
OSPF (Open Shortest Path First)    
RIP (Routing Information Protocol)   

## Layer 2 - Data Link

frames   

focuses on the physical addressing of the transmission   
adds in the physical **MAC (Media Access Control) address** of the receiving endpoint   
   
※ Inside every network-enabled computer is a **Network Interface Card (NIC)** which comes with a unique MAC address to identify it   


## Layer 1 - Physical
references the physical components of the hardware used in networking    
use electrical signals   
binary numbering system (1's and 0's)   
ethernet cables   


---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
