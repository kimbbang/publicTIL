 ## Local Area Network (LAN) Topologies   
 
### Star Topology
all devices are connected with their **own cable to a central switch/hub**   
expensive   
high reliability and scalability   
 
### Bus Topology
all devices are connected to a single cable, often called the **backbone cable**   
cost-efficient   
Data is sent in both left and right directions down the backbone until the packet's destination is reached   
A major flaw in the bus topology is that it can't handle a large amount of data   
prone to becoming slow and bottlenecked if devices within the topology are simultaneously requesting data   
 
###  Ring Topology
In a ring topology, all devices are a connector to two others to create a **full circle**   
Packets of data travel from one device to the next until they have reached their destination   
less prone to bottlenecks   
One of the major flaws with a ring topology is that if a device goes down or a cable is broken, then data will no longer be passed   


---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
