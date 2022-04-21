# savedsearches.conf

[docs.splunk - Create and edit reports](https://docs.splunk.com/Documentation/Splunk/8.2.5/Report/Createandeditreports)    
[docs.splunk - savedsearches.conf](https://docs.splunk.com/Documentation/Splunk/8.2.5/Admin/Savedsearchesconf)    



```
[stats with durable search]
search = index=_internal eps | stats avg(eps) as avg, max(eps) as max, min(eps) as min
dispatch.indexed_earliest = -30m
dispatch.indexed_latest   = now

durable.track_time_type   = _indextime
durable.lag_time          = 60
durable.backfill_type     = time_interval
durable.max_backfill_intervals = 100
```



---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 101](https://www.coursera.org/learn/splunk-knowledge-manager-101)    
