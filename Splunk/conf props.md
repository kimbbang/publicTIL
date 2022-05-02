# props.conf
```
[<stanza>]
EVAL-<field_name> = <eval statement>

<stanza> can be:
<source type>, the source type of an event.
host::<host>, where <host> is the host for an event.
source::<source>, where <source> is the source for an event.
```

---

## Calculated fields
[docs.splunk - About calculated fields](https://docs.splunk.com/Documentation/SplunkCloud/latest/Knowledge/definecalcfields)      
[docs.splunk - Create calculated fields with Splunk Web](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2202/Knowledge/CreatecalculatedfieldswithSplunkWeb)      
[docs.splunk - Configure calculated fields with props.conf](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2202/Knowledge/Configurecalculatedfieldswithprops.conf)      


Settings > KNOWLEDGE > Fields > Calculated fields


```
[<foo>]
EVAL-x = x * 2
EVAL-y = x * 2
```
```
[<access_common>]
EVAL-response_time =  response_time/1000
EVAL-bitrate = bytes*1000/response_time
```

---

## field aliases

A sourcetype의 user필드,   
B sourcetype의 username필드  
등으로 필드 이름이 다르지만 동일한 값이 들어있을 때(같은 그룹으로 묶어주고 싶을 때)  
모두 employee필드로 검색이 되도록 설정할 수 있다.   

[docs.splunk - Create field aliases in Splunk Web](https://docs.splunk.com/Documentation/Splunk/8.2.6/Knowledge/Addaliasestofields)      
[docs.splunk - Configure field aliases with props.conf](https://docs.splunk.com/Documentation/Splunk/8.2.6/Knowledge/Configurefieldaliaseswithprops.conf)      

[Field alias behavior change](https://docs.splunk.com/Documentation/Splunk/8.2.6/ReleaseNotes/Fieldaliasbehaviorchange)


Settings > KNOWLEDGE > Fields > Field aliases
```
FIELDALIAS-<class> = <orig_field_name> AS <new_field_name>
```
```
[accesslog]
EXTRACT-extract_ip = (?<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
FIELDALIAS-extract_ip = ip AS ipaddress
```
---

## field EXTRACT
```
# The following stanza extracts an ip address from _raw
[my_sourcetype]
EXTRACT-extract_ip = (?<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
```
---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 101](https://www.coursera.org/learn/splunk-knowledge-manager-101)    
[Splunk Inc.- Splunk Knowledge Manager 102](https://www.coursera.org/learn/splunk-knowledge-manager-102)    
