# like(TEXT, PATTERN)

※ 정규표현식 일치여부는 match(SUBJECT, "REGEX")

This function takes two arguments, a string to match TEXT and a string expression to match PATTERN. It returns TRUE if, and only if, TEXT matches PATTERN. The pattern matching supports an exact text match, as well as single and multiple character matches.

Use the percent ( % ) symbol as a wildcard for multiple characters.  
Use the underscore ( _ ) character for a single character match.  
You can use the percent ( % ) wildcard anywhere in the PATTERN.  

---

```
... | eval is_a_foo=if(like(field, "foo%"), "yes a foo", "not a foo")
```
```
... | where like(ipaddress, "198.%")
```



---
---

### Course
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)
### References

[docs.splunk - Comparison and Conditional functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/ConditionalFunctions)