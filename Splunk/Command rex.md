# rex
  
### rex
: 정규식을 사용해서 데이터에서 필드 추출 (검색하려는 필드가 없는 경우)

```
| rex field=savedsearch_id "(?<user>\w+);(?<app>\w+);(?<SavedSearchName>\w+)"
```
savedsearch_id 필드에서 지정한 정규표현식의 패턴으로 user, app, SavedSearchName 필드 생성

---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)  

[docs.splunk - rex](http://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Rex)  
[About Splunk regular expressions](https://docs.splunk.com/Documentation/Splunk/latest/Knowledge/Aboutsplunkregularexpressions)