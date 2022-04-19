# !=와 NOT의 차이

## !=
status 필드가 존재하는 이벤트중에 status가 200이 아닌 필드
 
 ```
 ... status != 200
 ```
 
## NOT
status 필드가 존재하는 이벤트중에 status가 200이 아닌 필드 + **status 필드가 존재하지 않는 이벤트**

```
... NOT status = 200
```
---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)  

[Difference between != and NOT](https://docs.splunk.com/Documentation/Splunk/latest/Search/NOTexpressions)