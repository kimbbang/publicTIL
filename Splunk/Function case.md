# case(X,"Y",...)

조건1, 결과1, 
조건2, 결과2, 
..
조건n, 결과n, 
디폴트결과

---

```
sourcetype=access_* | eval description=case(status == 200, "OK", status ==404, "Not found", status == 500, "Internal Server Error") | table status description
```




---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)

[docs.splunk - Comparison and Conditional functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/ConditionalFunctions)