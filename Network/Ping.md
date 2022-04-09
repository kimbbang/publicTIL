
## Ping (ICMP)

Ping uses ICMP (Internet Control Message Protocol) packets to determine the performance of a connection between devices    
for example, if the connection exists or is reliable.

The time taken for ICMP packets travelling between devices is measured by ping
```
C:\>ping 8.8.8.8

Ping 8.8.8.8 32바이트 데이터 사용:
8.8.8.8의 응답: 바이트=32 시간=16ms TTL=117
8.8.8.8의 응답: 바이트=32 시간=23ms TTL=117
8.8.8.8의 응답: 바이트=32 시간=31ms TTL=117
8.8.8.8의 응답: 바이트=32 시간=49ms TTL=117

8.8.8.8에 대한 Ping 통계:
    패킷: 보냄 = 4, 받음 = 4, 손실 = 0 (0% 손실),
왕복 시간(밀리초):
    최소 = 16ms, 최대 = 49ms, 평균 = 29ms
```


---

### References
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
