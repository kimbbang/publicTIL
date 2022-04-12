## TCP
### Transmission Control Protocol 

reserves a **constant connection** between the two devices for the amount of time    
incorporates error checking into its design > **guarantees** the accuracy of data   
Three-way handshake
slow connection   
ex) file sharing, internet browsing, email

---

### Header

#### Source Port   
is the port opened by the sender to send the TCP packet from.    
is chosen **randomly** (out of the ports from 0-65535 that aren't already in use at the time). 

#### Destination Port   
is the port number that an application or service is running on the remote host (the one receiving data);    
for example, a webserver running on port 80. Unlike the source port, this value is **not** chosen at random.

#### Source IP   
is the IP address of the device that is **sending** the packet.

#### Destination IP   
is the IP address of the device that the packet is **destined** **for**.

#### Sequence Number   
When a connection occurs, the first piece of data transmitted is given a random number. 

#### Acknowledgement Number   
After a piece of data has been given a sequence number, the number for the next piece of data will have **the sequence number + 1**. 

#### Checksum   
This value is what gives TCP **integrity**.    
A mathematical calculation is made where the output is remembered.    
When the receiving device performs the mathematical calculation, the data must be corrupt if the output is different from what was sent.

#### Data   
This header is where the data, i.e. bytes of a file that is being transmitted, is stored.

#### Flag   
This header determines **how** the packet should be **handled** by either device **during the handshake process**.   
**SYN, SYN/ACK, ACK** ... 

---

### Three-way handshake

<img src="https://www.cablefree.net/support/radio/software/images/f/fc/Image2001.gif">

출처 : [TCP session establishment and termination](https://www.cablefree.net/support/radio/software/Manual:Connection_oriented_communication_(TCP/IP))

#### Step1	SYN	: client > server    
the initial packet sent by a client during the handshake.    
This packet is used to initiate a connection and synchronise the two devices together        	

#### Step2	SYN/ACK	: client < server    
This packet is sent by the receiving device (server) to acknowledge the synchronisation attempt from the client.       	

#### Step3	ACK	: client > server    
The acknowledgement packet can be used by either the client or server to acknowledge that a series of messages/packets have been **successfully received**.       	

#### Step4	DATA : client ⇔ server    
Once a connection has been established, data (such as bytes of a file) is sent via the "DATA" message.       	

#### Step5	FIN	   	    
This packet is used to cleanly (properly) close the connection after it has been complete.       	

client > server FIN    
client < server ACK/FIN
client > server ACK    

#### Step#	RST	   	    
This packet abruptly ends all communication.    
This is the last resort and indicates there was some problem during the process.   
For example, if the service or application is not working correctly, or the system has faults such as low resources.       	


---

### ISN
#### Initial Number Sequence 

?? 

[What is the TCP sequence number? How it is used for reliable and sequence delivery?](https://www.cspsprotocol.com/tcp-sequence-number/)







---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)   
[TCP session establishment and termination](https://www.cablefree.net/support/radio/software/Manual:Connection_oriented_communication_(TCP/IP))   
[What is the TCP sequence number? How it is used for reliable and sequence delivery?](https://www.cspsprotocol.com/tcp-sequence-number/)
