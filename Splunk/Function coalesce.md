# coalesce(X,...)

두가지 필드에 있는 값을 하나의 필드에 합칠 때   

A　B　　new field value  
O　X　->　A  
X　O　->　B  
O　O　->　A  

You have a set of events where the IP address is extracted to either clientip or ipaddress.   
This example defines a new field called ip, that takes the value of either the clientip field or ipaddress field, depending on which field is not NULL (does not exist in that event).   
<u>If both</u> the clientip and ipaddress <u>field exist in the event</u>, this function returns the **first argument**, the clientip field.

---

```
... | eval ip=coalesce(clientip,ipaddress)
```

---

### References
[Splunk Inc.- Splunk Search Expert 101](https://www.coursera.org/learn/splunk-search-expert-101)

[docs.splunk - Comparison and Conditional functions](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/ConditionalFunctions)