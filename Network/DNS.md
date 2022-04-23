# DNS
Domain Name System

provides a simple way for us to communicate with devices on the internet without remembering complex numbers

every computer on the internet has its own unique address to communicate with it called an IP address


---

## Domain Hierarchy

length must be kept to 253 characters or less

### TLD (Top-Level Domain)
A TLD is the most righthand part of a domain name
    
for example, the tryhackme.com TLD is .com
    
* #### gTLD (Generic Top Level)   
    : tell the user the domain name's purpose

    **.com** would be for commercial purposes   
    **.org** for an organisation   
    **.edu** for education  
    **.gov** for government

* #### ccTLD (Country Code Top Level Domain)  
    : was used for geographical purposes  
    **.ca** for sites based in Canada    
    **.co.uk** for sites based in the United Kingdom

[tlds-alpha-by-domain](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)

### Second-Level Domain

**tryhackme**.com as an example, tryhackme is the Second Level Domain


### Subdomain

A subdomain sits on the left-hand side of the Second-Level Domain using a period to separate it

**admin**.tryhackme.com the admin part is the subdomain

limited to 63 characters and can only use a-z 0-9 and hyphens


---

## What happens when you make a DNS request

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210706213210/DNS2.png">

출처 : [Details on DNS](https://www.geeksforgeeks.org/details-on-dns/)

### ① local device(local cache) >   

### ② Recursive DNS Server >   
Many Internet Service Providers (ISPs) maintain their own recursive servers,   
but companies such as Google and OpenDNS also control recursive servers  

### ③ root DNS server + TLD(Top-Level Domain) server >   
if you were searching for tryhackme.com your request would be redirected to a TLD server that handled .com domains.   
If you were searching for bbc.co.uk your request would be redirected to a TLD server that handles .co.uk domains  

### ④ authoritative DNS server >>>   

### ② Recursive DNS Server  

---

## DNS Record Types


### A Record

resolve to **IPv4** addresses, for example 10.10.10.10

```
user@thm:~$ nslookup --type=A www.website.thm
Server: 127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
Name: www.website.thm
Address: 10.10.10.10
```
'10.10.10.10' is the IP address for the A record of www.website.thm

### AAAA Record

resolve to **IPv6** addresses, for example 2606:4700:20::681a:be5

### CNAME Record

resolve to another domain name

shop.website.thm > shops.myshopify.com

```
user@thm:~$ nslookup --type=CNAME shop.website.thm
Server: 127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
shop.website.thm canonical name = shops.myshopify.com
```


### MX Record

These records resolve to the address of the servers that handle the **email** for the domain you are querying

```
user@thm:~$ nslookup --type=MX website.thm
Server: 127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
website.thm mail exchanger = 30 alt4.aspmx.l.google.com
```
'30' is the numerical priority value for the MX record




### TXT Record

TXT records are free text fields where any text-based data can be stored. 

---

## fields

### TTL 

Time To Live  
specifies how long a DNS record should be cached for




---
---

### Course
[TryHackMe - How The Web Works](https://tryhackme.com/module/how-the-web-works)     
[TryHackMe - Network Exploitation Basics](https://tryhackme.com/module/intro-to-networking)    

### References
[Details on DNS](https://www.geeksforgeeks.org/details-on-dns/)