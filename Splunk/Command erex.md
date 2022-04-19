# erex

정규식을 사용하지 **않고** 데이터에서 필드 추출   
(검색하려는 필드가 **없는** 경우)

---

1. 검색
    ```
    sourcetype=secure* port "failed password" | erex port examples="port 3351, port 3768"
    ```
2. port 필드가 생긴 것 확인   
    port 3351, port 3768 이외에도 동일 패턴의 데이터가 port 필드로 지정됨 
    (punct 필드("____::__[]:________...___" 등)에서 해당 데이터가 있는 위치를 추출해서 필드화하는 듯)   

3. 검색 완료후 > job > 「Successfully learned regex. Consider using: | rex "(?i)^(?:[^\.]*\.){3}\d+\s+(?P<port>\w+\s+\d+)" 」등의 메시지 확인 > 아래 SPL로 수정해서 검색하는게 성능이 좋다.

    ```
    sourcetype=secure* port "failed password" | rex "(?i)^(?:[^\.]*\.){3}\d+\s+(?P<port>\w+\s+\d+)"
    ```
---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)  

[docs.splunk - erex](http://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Erex) 