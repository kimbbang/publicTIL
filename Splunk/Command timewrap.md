# timewrap

timechart 쓸 때 1주일전, 24시간 전 그래프 등을 겹쳐서 보여주고 싶을 때 

[docs.splunk - timewrap](https://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Timewrap) 

Displays, or wraps, the output of the timechart command so that every period of time is a different series.

You can use the timewrap command to compare data over specific time period, such as day-over-day or month-over-month
  
---

예 
```
| timechart span=1d count as Failures
| timewrap 1w
```
검색 기간이 2주면(earliest=-14d@d) 
Failures_1week_before, Failures_latest_week 선 두개  
검색 기간이 2주면(earliest=-20d@d) 
Failures_2week_before, Failures_1week_before, Failures_latest_week 선 세개


---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)    
