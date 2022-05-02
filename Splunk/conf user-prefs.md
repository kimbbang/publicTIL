# user-prefs.conf

[user-prefs.conf](https://docs.splunk.com/Documentation/Splunk/8.2.6/Admin/User-prefsconf)


* Windows: C:\Program Files\Splunk\etc\apps\user-prefs\default\user-prefs.conf
* Linux:/opt/splunk/etc/apps/user-pref/default/user-prefs.conf

---

## Set landing page (instead of default main page)

1. change setting in user-prefs.conf
    ```
    FROM
    [general_default]
    default_namespace = $default
    appOrder = search

    TO 
    [general_default]
    default_namespace = search
    appOrder = search
    ```

2. restart splunk
    ```
    net stop splunkd 
    net start splunkd
    ```


---
---

### Course
[TryHackMe - Splunk 101](https://tryhackme.com/room/splunk101)  
