# timechart

[docs.splunk - timechart](https://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Timechart) 
  
---

예
```
sourcetype=access_* action=purchase 
| timechart span=1d count by categoryId usenull=f
```
```
_time	ACCESSORIES	ARCADE	SHOOTER	SIMULATION	SPORTS	STRATEGY	TEE
2018-03-29	5	17	6	3	5	32	9
2018-03-30	62	63	39	30	22	127	56
```

---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)    
