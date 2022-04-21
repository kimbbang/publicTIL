# limits.conf


[docs.splunk - limits.conf](https://docs.splunk.com/Documentation/Splunk/8.2.5/Admin/Limitsconf)    

---

## Have maximum concurrent scheduled report limits vary by time

[docs.splunk - Configure the priority of scheduled reports](https://docs.splunk.com/Documentation/Splunk/8.2.5/Report/Configurethepriorityofscheduledreports#How_the_report_scheduler_determines_the_concurrent_scheduled_report_limit) 
```
# The default limit, used when the periods defined below are not in effect.
max_searches_perc = 50 
 
# Increase the value between midnight-5AM.
max_searches_perc.0 = 75
max_searches_perc.0.when = * 0-5 * * *
 
# More specifically, increase it even more on weekends.
max_searches_perc.1 = 90
max_searches_perc.1.when = * 0-5 * * 0,6
```


---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 101](https://www.coursera.org/learn/splunk-knowledge-manager-101)    
