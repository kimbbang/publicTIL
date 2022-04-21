# eventtypes.conf

## event types

데이터를 분류하고 각 레코드의 좌측에 지정한 색상을 표시  
예 ) ERROR가 있으면 빨간색, WARN이 있으면 노란색 등 

eventtype=error 로 검색 가능 

[docs.splunk - About event types](https://docs.splunk.com/Documentation/SplunkCloud/latest/Knowledge/Abouteventtypes)      

Event types are a categorization system to help you make sense of your data. Event types let you sift through huge amounts of data, find similar patterns, and create alerts and reports.

---

## eventtypes.conf 설정

[docs.splunk - Configure event types in eventtypes.conf](https://docs.splunk.com/Documentation/SplunkCloud/latest/Knowledge/Configureeventtypes)  
[docs.splunk - eventtypes.conf](https://docs.splunk.com/Documentation/Splunk/8.2.5/Admin/Eventtypesconf)

* 레코드 클릭 > Event Actions > Build Event Type   
    
* $SPLUNK_HOME/etc/system/local/eventtypes.conf

eventtypes.conf
```
[web]
search = html OR http OR https OR css OR htm OR html OR shtml OR xls OR cgi

[fatal]
search = FATAL
```
```
[web]
disabled = 1
```


---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 101](https://www.coursera.org/learn/splunk-knowledge-manager-101)    
