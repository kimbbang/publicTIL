# the OSI Model
Open Systems Interconnection Model   

---

## Layer 7 - Application
data

FileZilla : file server browsing software who provides a friendly, Graphical User Interface (GUI)   
DNS (Domain Name System): how website addresses are translated into IP addresses.   

---

## Layer 6 - Presentation
data

acts as a **translator** for data to and from the application layer (layer 7)   
**format** data     
**encrypts, compresses, or otherwise transforms** the initial data to give it a **standardised format**


---


## Layer 5 - Session
data

will begin to **create a connection** to the other computer that the data is destined for. (session)   
synchronises the two computers to ensure that they are on the same page before data is sent and received   
**divide up the data** sent into smaller chunks of data and begin to send these chunks (**packets**) one at a time     
This is what allows you to **make multiple requests to different endpoints simultaneously** without all the data getting mixed up (think about opening two tabs in a web browser at the same time)!  
**tracks communications** between the host and receiving computers

---

## Layer 4 - Transport
TCP segments, UDP datagrams

transmitting data across a network
TCP, UDP   

Its first purpose is to choose the protocol over which the data is to be transmitted.   
With a protocol selected, the transport layer then **divides** the transmission up into bite-sized pieces


---

## Layer 3 - Network
packets  

is responsible for locating the destination of your request  
routing & re-assembly of data   
everything is dealt with via **IP addresses(logical** addressing)   
routing simply determines the most **optimal** path    
OSPF (Open Shortest Path First)    
RIP (Routing Information Protocol)   

---

## Layer 2 - Data Link
frames   

only **add a trailer during encapsulation**  
focuses on the physical addressing of the transmission   
data would be formatted in preparation for transmission  
adds in the physical **MAC (Media Access Control) address** of the receiving endpoint   
   
※ Inside every network-enabled computer is a **Network Interface Card (NIC)** which comes with a unique MAC address to identify it   

**checks received packets** to make sure that they haven't been corrupted

---


## Layer 1 - Physical
data (stream bits)

references the physical components of the hardware used in networking    
use electrical signals(pulses)   
binary numbering system (1's and 0's)   
ethernet cables   


---
---

### Course


[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)   
[TryHackMe -  Network Exploitation Basics](https://tryhackme.com/module/intro-to-networking)


### References
[인터넷 프로토콜 스위트](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%EB%84%B7_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_%EC%8A%A4%EC%9C%84%ED%8A%B8)
