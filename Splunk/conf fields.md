# fields.conf

Multivalue fields are fields that can appear multiple times in an event and have a different value for each appearance. 


[docs.splunk - Configure extractions of multivalue fields with fields.conf](https://docs.splunk.com/Documentation/Splunk/8.2.6/Knowledge/ConfigureSplunktoparsemulti-valuefields)

---
xx.log file 
```
From:          sender@splunkexample.com
To:            recipient1@splunkexample.com, recipient2@splunkexample.com, recipient3@splunkexample.com
CC:            cc1@splunkexample.com, cc2@splunkexample.com, cc3@splunkexample.com
Subject:       Multivalue fields are out there!
X-Mailer:      Febooti Automation Workshop (Unregistered)
Content-Type:  text/plain; charset=UTF-8
Date:          Wed, 3 Nov 2017 17:13:54 +0200
X-Priority:    3 (normal)
```
fields.conf
```
[To]
TOKENIZER = (\w[\w\.\-]*@[\w\.\-]*\w)

[From]
TOKENIZER = (\w[\w\.\-]*@[\w\.\-]*\w)

[Cc]
TOKENIZER = (\w[\w\.\-]*@[\w\.\-]*\w)
```


---
---

### Course
[Splunk Inc.- Splunk Knowledge Manager 102](https://www.coursera.org/learn/splunk-knowledge-manager-102)    
