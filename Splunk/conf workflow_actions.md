# workflow_actions.conf

get, post로 외부 link와 연동 

[docs.splunk - Use special parameters in workflow actions](https://docs.splunk.com/Documentation/Splunk/8.2.5/Knowledge/Usespecialparametersinworkflowactions)      
[docs.splunk - workflow_actions.conf](https://docs.splunk.com/Documentation/Splunk/8.2.5/Admin/Workflow_actionsconf)  

Settings > Fields > workflow actions

---

## clientip가 어디서 온 건지 알고싶을 때 

### 웹에서 설정 예
Name(내가 만드는 workflow action의 이름): OPS_WFA_Network_Security_ns_GetWhoIs  
Label(기능을 실행할 때 선택할 이름): Get WhoIs for $src_ip$  
Apply only to the following fields(적용할 필드): src_ip  
URI : ```http://도메인검색사이트.com/$src_ip$   ```

### workflow_actions.conf 예
```
[whois]
display_location = field_menu
fields = clientip
label = Whois: $clientip$
link.method = get
link.target = blank
link.uri = http://ws.arin.net/whois/?queryinput=$clientip$
type = link
```

```
[Google]
display_location = field_menu
fields = *
label = Google $@field_name$
link.method = get
link.uri = http://www.google.com/search?q=$@field_value$
type = link
```



---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 101](https://www.coursera.org/learn/splunk-knowledge-manager-101)    
