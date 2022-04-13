# Computer Management (compmgmt)

System Tools, Storage, and Services and Applications.

### How to open

* search Computer Management (컴퓨터 관리)
* search compmgmt
* run compmgmt.msc

---

## System Tools

* ### Task Scheduler   
    : we can create and manage common tasks that our computer will carry out **automatically** at the times we specify.  


* ### Event Viewer
  : view events that have occurred on the computer  
     * [Event Types](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-types)  
     * [Eventlog Key](https://docs.microsoft.com/en-us/windows/win32/eventlog/eventlog-key)  


*  ### Shared Folders :   
    Shared Folders > Shares   
    C$ : the default share of Windows    
    ADMIN$ : default remote administration shares created by Windows  
    Shared Folders > Sessions  
    a list of users who are **currently** **connected** to the shares


*  ###  Local Users and Groups   
    = lusrmgr; Local User and Group Management


*  ### Performance  
    Performance Monitor (perfmon).  
    either in real-time or from a log file


*  ### Device Manager  
    configure the hardware



## Storage

## Services and Applications

a service is a special type of application that runs in the background

Services and Applications > WMI Control  
controls the Windows Management Instrumentation (WMI) service.

WMI allows scripting languages (such as VBScript or Windows PowerShell) to manage Microsoft Windows personal computers and servers, both locally and remotely


---
### References
[TryHackMe - Windows Fundamentals](https://tryhackme.com/module/windows-fundamentals)   
