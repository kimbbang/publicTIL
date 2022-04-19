# stats

---

```
index=* | stats count(eval(status="404")) AS count_status BY sourcetype
```
```
| stats first(startTime) AS startTime, first(status) AS status, 
first(histID) AS currentHistId, last(histID) AS lastPassHistId BY testCaseId
```
```
| stats latest(startTime) AS startTime, latest(status) AS status, 
latest(histID) AS currentHistId, earliest(histID) AS lastPassHistId BY testCaseId
```


---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)  

[docs.splunk - stats](https://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/Stats) 