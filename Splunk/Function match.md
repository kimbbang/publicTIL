# match(SUBJECT, "REGEX")

※ 정규표현식이 아닌 패턴 일치여부는 like(TEXT, PATTERN)

This function compares the regex string REGEX to the value of SUBJECT and returns a Boolean value. It returns TRUE if the REGEX can find a match against any substring of SUBJECT.

---

```
... | eval n=if(match(field, "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"), 1, 0)
```
```
... | eval matches = if(match(test,"yes"), 1, 0)
```
```
| makeresults | eval test="\"yes\"" | eval matches = if(match(test, "\"yes\""), 1, 0)
```


---
---

### Course
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)
### References

[docs.splunk - Comparison and Conditional functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/ConditionalFunctions)