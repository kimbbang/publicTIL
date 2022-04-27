# nmap

## **Scan Types**

## TCP Connect Scans (-sT)

If run without sudo permissions, Nmap defaults to the TCP Connect scan

If Nmap sends a TCP request with the SYN flag set to a **closed port**, the target server will respond with a TCP packet with the **RST (Reset) flag** set. 

If the request is sent to an **open port**, the target will respond with a TCP packet with the **SYN/ACK flags** set. 

Nmap sends a TCP SYN request, and **receives nothing back**. This indicates that the **port is being protected by a firewall** and thus the port is considered to be filtered.

??
```
iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset
```

---

## SYN "Half-open" Scans (-sS)
=  "Stealth" scans

SYN scans are the default scans used by Nmap if run with sudo permissions

(When using a SYN scan to identify closed and filtered ports, the exact same rules as with a TCP Connect scan apply)

### advantages 

SYN scans are often not logged by applications listening on open ports  
faster than a standard TCP Connect scan.

### disadvantages 

They require sudo permissions  

---

## UDP Scans (-sU)

Unlike TCP, UDP connections are stateless


the port as being open or filtered   : no response   

closed UDP port : respond with an ICMP (ping) packet containing a message that the port is unreachable


### ```--top-ports <number>```
scan the top 20 most commonly used UDP ports
```
nmap -sU --top-ports 20 <target>
```

---

## TCP Null Scans (-sN)

when the TCP request is sent with no flags set at all

As per the RFC, the target host should respond with a RST if the port is closed.


## TCP FIN Scans (-sF)

a request is sent with the FIN flag 

Nmap expects a RST if the port is closed.

## TCP Xmas Scans (-sX)

send a malformed TCP packet and expects a RST response for closed ports

sets (PSH, URG and FIN) 

---

## ICMP Network Scanning

ping sweep (-sn)  
The -sn switch tells Nmap not to scan any ports -- forcing it to rely primarily on ICMP echo packets (or ARP requests on a local network, if run with sudo or directly as the root user) to identify targets.

192.168.0.x network 
```
nmap -sn 192.168.0.1-254
    OR
nmap -sn 192.168.0.0/24
```

172.16.x.x network   
Netmask: 255.255.0.0
```
nmap -sn 172.16.0.0/16
```

---




```
root@ip-10-10-45-208:~# nmap -sC -sV -oN test -Pn 10.10.30.144

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-27 12:49 BST
Nmap scan report for ip-10-10-30-144.eu-west-1.compute.internal (10.10.30.144)
Host is up (0.00036s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE VERSION
80/tcp   open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| http-methods: 
|_  Potentially risky methods: TRACE
| http-robots.txt: 6 disallowed entries 
| /Account/*.* /search /search.aspx /error404.aspx 
|_/archive /archive.aspx
|_http-server-header: Microsoft-IIS/8.5
|_http-title: hackpark | hackpark amusements
3389/tcp open  ssl     Microsoft SChannel TLS
| fingerprint-strings: 
|   TLSSessionReq: 
|     hackpark0
|     220426114313Z
|     221026114313Z0
|     hackpark0
|     Ad72
|     k?rv
|     fk;@
|     QArl
|     $0"0
|     QZ]B9
|     Y+7]cn
|_    y-[s
| ssl-cert: Subject: commonName=hackpark
| Not valid before: 2022-04-26T11:43:13
|_Not valid after:  2022-10-26T11:43:13
|_ssl-date: 2022-04-27T11:50:11+00:00; 0s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3389-TCP:V=7.60%I=7%D=4/27%Time=62692DE8%P=x86_64-pc-linux-gnu%r(TL
SF:SSessionReq,33C,"\x16\x03\x03\x037\x02\0\0M\x03\x03bi-\xe4T\xa0\xef\xa9
SF:\xa61\x1d\x04\xefZ\xe8\x85\x15<\xbe\xb6\x02\xb2\xd1q\xe
...
```









---
---
### Course 
[TryHackMe - Nmap](https://tryhackme.com/room/furthernmap)
