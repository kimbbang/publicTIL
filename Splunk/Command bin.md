# bin

[docs.splunk - bin](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/Bin) 
  
---

### 예1) 5분 단위로 시간 필드값 나누기 
```
 | bin _time span=5m 
 | stats avg(thruput) by _time host
 ```
결과 : 0분-5분, 5분-10분 ... 

### 예2) 5000을 단위로 revenue 필드값 나누기 
```
 | stats sum(price) as revenue by product_name
 | bin revenue span=5000
 | stats list(product_name) as product_name by revenue
 ```
결과 0-5000, 5000-1000, ....






---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)    
