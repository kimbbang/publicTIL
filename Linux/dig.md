# dig

Dig allows us to manually query recursive DNS servers of our choice for information about domains

---

## ```dig <domain> @<dns-server-ip>```
```
root@ip-10-10-230-195:~# dig google.com @1.1.1.1

; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> google.com @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10771
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		89	IN	A	74.125.193.100
google.com.		89	IN	A	74.125.193.113
google.com.		89	IN	A	74.125.193.138
google.com.		89	IN	A	74.125.193.101
google.com.		89	IN	A	74.125.193.139
google.com.		89	IN	A	74.125.193.102

;; Query time: 1 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Sat Apr 23 04:05:25 BST 2022
;; MSG SIZE  rcvd: 135
```
ANSWER SECTION: is telling us that we sent it one query and successfully 
```
google.com.		89	IN	A	74.125.193.100
```
TTL (Time To Live) of the queried DNS record is 89 **seconds**

---
---

### Course

[TryHackMe - Network Exploitation Basics](https://tryhackme.com/module/intro-to-networking)