# relative_time(X,Y)

relative_time(UNIX time, relative time specifier)

[docs.splunk - Date and time format variables](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/Commontimeformatvariables)  
[docs.splunk - Time modifiers](https://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/SearchTimeModifiers)   

---

※ now() : UNIX time value of the start of yesterday, based on the value of now().
```
... | eval n=relative_time(now(), "-1d@d")
```


---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)
### References

[docs.splunk - Date and Time functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/DateandTimeFunctions)