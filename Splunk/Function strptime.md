# strptime(X,Y)

human readable -> UNIX TIME

[docs.splunk - Date and Time functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/DateandTimeFunctions)  
[docs.splunk - Date and time format variables](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/Commontimeformatvariables)


---
### 예 
_time : 2022/04/01 18:20:56  
humantime : 2022/04/01 18:20:56  
unixtime : 1648804856.000000  
```
| eval humantime=strftime(_time, "%Y/%m/%d %H:%M:%S")
| eval unixtime=strptime(humantime, "%Y/%m/%d %H:%M:%S")
| table _time humantime unixtime
```

---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)