# time()

The value of the time() function will be different for each event, based on when that event was processed by the eval command.

---

※ now()

returns the UNIX time when the search is run

예) UNIX time value of the start of yesterday, based on the value of now().
```
... | eval n=relative_time(now(), "-1d@d")
```



---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)
### References

[docs.splunk - Date and Time functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/DateandTimeFunctions)