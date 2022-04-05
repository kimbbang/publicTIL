

### !=와 NOT의 차이

status 필드가 존재하는 이벤트중에 status가 200이 아닌 필드
 
 ```
 ... status != 200
 ```
 
status 필드가 존재하는 이벤트중에 status가 200이 아닌 필드 + **status 필드가 존재하지 않는 이벤트**

```
... NOT status = 200
```

---

### erex
[erex](http://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Erex) : 정규식을 사용하지 않고 데이터에서 필드 추출 (검색하려는 필드가 **없는** 경우)

 ```
 sourcetype=secure* port "failed password" | erex port examples="port 3351, port 3768"
 ```
   
port 필드가 생긴 것 확인   
port 3351, port 3768 이외에도 동일 패턴의 데이터가 port 필드로 지정됨   
(punct 필드("____::__[]:________...___" 등)에서 해당 데이터가 있는 위치를 추출해서 필드화하는 듯)   
검색 완료후 > job > Successfully learned regex. Consider using: | rex "(?i)^(?:[^\.]*\.){3}\d+\s+(?P<port>\w+\s+\d+)" 등의 메시지 확인 > 아래 SPL로 검색하는게 성능이 좋다.

```
sourcetype=secure* port "failed password" | rex "(?i)^(?:[^\.]*\.){3}\d+\s+(?P<port>\w+\s+\d+)"

```
  
---
### rex
[rex](http://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Rex) : 정규식을 사용해서 데이터에서 필드 추출 (검색하려는 필드가 없는 경우)

```
| rex field=savedsearch_id "(?<user>\w+);(?<app>\w+);(?<SavedSearchName>\w+)"
```
savedsearch_id 필드에서 지정한 정규표현식의 패턴으로 user, app, SavedSearchName 필드 생성

 
---
 출처: [코세라 Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)
