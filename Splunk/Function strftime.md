# strftime(X,Y)

[docs.splunk - Date and Time functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/DateandTimeFunctions)  
[docs.splunk - Date and time format variables](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/Commontimeformatvariables)


---
### 예 1 
_time : 2018-08-10 11:48:23  
hour_min : 11:48
```
...| eval hour_min=strftime(_time, "%H:%M")
```

### 예 2
StartTimeStamp : 1521467703049000000  
_time : 2018-08-10 09:04:00  
starttime : 2018-03-19T06:55:03.049  
```
| makeresults 
| eval StartTimestamp="1521467703049000000"
| eval starttime=strftime(StartTimestamp/pow(10,9),"%Y-%m-%dT%H:%M:%S.%Q")
```





---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)