# macros.conf

Search macros are reusable chunks of Search Processing Language (SPL) that you can insert into other searches. 


[docs.splunk - Use search macros in searches](https://docs.splunk.com/Documentation/Splunk/8.2.6/Knowledge/Usesearchmacros)    
[docs.splunk - Define search macros in Settings](https://docs.splunk.com/Documentation/Splunk/8.2.6/Knowledge/Definesearchmacros)    
[docs.splunk - macros.conf](https://docs.splunk.com/Documentation/Splunk/8.2.6/Admin/macrosconf)    
* $SPLUNK_HOME/etc/system/local/macros.conf  
* Settings > Advanced search > Search macros

---

## 기본 사용 

mygeneratingmacro 마크로 설정 내용 
```
tstats latest(_time) as latest where index!=filemon by index host source sourcetype
```
검색
```
| `mygeneratingmacro`
```

## 파라미터를 넘겨줄 때 
iis_search 마크로 설정 내용 
```
sourcetype="iis" cs_username!="-" /$fragment$/ .pdf
```
검색
```
`iis_search(fragment=TM)`
```

## Validating macro arguments 
문자 기준 정렬에서 숫자 기준으로 정렬로 바꾸기(11 > 1 > 22 > 2 를 1 > 2 > 11 > 22 로)  

### 마크로 설정 내용 

Name: 기존 파라미터 + 1개(cmd)
```
convertUSD(2)
```
Definition 
```
$cmd$ $moolah$ = "$" + tostring(round($moolah$, 2), "commas")
```
validation Expression : 아래 형식이면 마크로 신택스가 true, 아니면 false 
```
$cmd$="fieldformat" OR $cmd$="eval"
```
Validation Error Message : 마크로 신택스가 false인 경우 표시할 메시지 
```
convertUSD macro must include a cmd argument of field format or eval 
```

### 검색
```
...
|stats avg(sale_price) as Average_Price by product_name
|`convertUSD(eval, Average_Price)`
|sort - fieldformat
```









---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 101](https://www.coursera.org/learn/splunk-knowledge-manager-101)    
