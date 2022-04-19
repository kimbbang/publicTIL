# in(FIELD, VALUE-LIST)

You can use this function with the eval, fieldformat, and where commands, and as part of eval expressions with other commands.

The following syntax is supported:
```
...| where in(field,"value1","value2", ...)  
...| where field in("value1","value2", ...)  
...| eval new_field=if(in(field,"value1","value2", ...), "value-if_true","value-if-false")
```

---

```
... | where status in("400", "401", "403", "404")
```
```
... | eval error=if(in(status, "error", "failure", "severe"),"true","false")
```
```
... | eval error=if(in(status, "404","500","503"),"true","false") | stats count by error
```


---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)

[docs.splunk - Comparison and Conditional functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/ConditionalFunctions)