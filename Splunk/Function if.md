# if(X,Y,Z)

X : 조건  
Y : X가 true  
Z : X가 false  

---

```
... | eval err=if(error == 200, "OK", "Error")
```
```
... | eval isLocal=if(cidrmatch("123.132.32.0/25",ip), "local", "not local")
```


---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)

[docs.splunk - Comparison and Conditional functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/ConditionalFunctions)