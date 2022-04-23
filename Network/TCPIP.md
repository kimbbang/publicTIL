# TCP/IP

[인터넷 프로토콜 스위트](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%EB%84%B7_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_%EC%8A%A4%EC%9C%84%ED%8A%B8)

※ **Network architecture(=Internet Protocol Suite)** is the design of a computer network. It is a framework for the specification of a network's physical components and their functional organization and configuration, its operational principles and procedures, as well as communication protocols used.
TCP/IP, OSI Model ..

---



<img src="https://www.slashroot.in/sites/default/files/PDU%20traveling%20through%20layers.png">

출처 : [Difference Between Segments, Packets and Frames](https://www.slashroot.in/difference-between-segments-packets-and-frames)

## Application 
protocol: HTTP, SMTP, POP3, IMAP4, 보조 - DHCP, DNS     

**사람이 인식**하고 응용 계층 아래의 표현 계층과 상호 작용할 수 있는 데이터와 그림을 사용자에게 보여주는 역할을 맡는다    

[응용 계층](https://ko.wikipedia.org/wiki/%EC%9D%91%EC%9A%A9_%EA%B3%84%EC%B8%B5)

---


## Transport 
protocol: TCP, UDP    
data name : Segments(TCP), datagram(UDP)  
각각의 애플리케이션에 데이터를 배분  

[전송 계층](https://ko.wikipedia.org/wiki/%EC%A0%84%EC%86%A1_%EA%B3%84%EC%B8%B5)

---


## Internet   
protocol: MAIN - IP, 보조 - ICMP, ARP  
data name : Packets, datagram  
네트워크 **간** 연결 (**traceroute**로 확인)  
기기: router, layer 3 switch

---

## Network Interface 
protocol : Ethernet, LAN, PPP    
data name : Frames  
물리적 연결    
**같은** 네트워크 안에서 데이터 전송   
Network Interface층 만은 프로토콜이 달라도 데이터를 주고 받을 수 있다.   
예 - 이더넷과 와이파이   
기기: layer 2 switch



---
---

### Course
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)  
[TryHackMe -  Network Exploitation Basics](https://tryhackme.com/module/intro-to-networking)