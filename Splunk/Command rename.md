# rename
1 대 1로 이름 변경 

※ 여러가지 필드를 하나의 변수로 합치고 싶을 때는 coalesce(X,...)


---

```
... | rename SESSIONID AS "The session ID"
```
```
... | rename count AS "Count of Events"
```

Rename multiple, similarly named fields
```
... | rename foo* AS bar*

```


---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)  

[docs.splunk - rename](https://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Rename) 