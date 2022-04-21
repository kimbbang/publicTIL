# authorize.conf

[authorize.conf](https://docs.splunk.com/Documentation/Splunk/8.2.6/Admin/Authorizeconf)  

* $SPLUNK_HOME/etc/system/local/authorize.conf
--- 

## creat account with a role


This creates the role 'ninja', which inherits capabilities from the 'user' role. 
```
[role_ninja]
rtsearch = enabled
importRoles = user
srchFilter = host=foo
srchIndexesAllowed = *
srchIndexesDefault = mail;main
srchJobsQuota   = 8
rtSrchJobsQuota = 8
srchDiskQuota   = 500
srchTimeWin = 86400
srchTimeEarliest = 2592000
```

#### ※ [Define roles on the Splunk platform with capabilities](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2201/Security/Rolesandcapabilities)
* admin
: This role has the most capabilities.

*  power
: This role can edit all shared objects and alerts, tag events, and other similar tasks.

*  user
: This role can create and edit its own saved searches, run searches, edit preferences, create and edit event types, and other similar tasks.

#### ※ [How to work with users and roles using the Splunk Enterprise SDK for Java](https://dev.splunk.com/enterprise/docs/devtools/java/sdk-java/howtousesdkjava/howtoworkusersrolessdkjava/)

```
// Connect to Splunk Enterprise
Service service = Service.connect(connectArgs);

// Get the collection of users
UserCollection usercollection = service.getUsers();

// Create a user
User user = service.getUsers().create(username, password, roles);
```


---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 101](https://www.coursera.org/learn/splunk-knowledge-manager-101)      
