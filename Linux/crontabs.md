## crontab

A crontab is simply a special file with formatting that is recognised by the cron process to execute each line step-by-step

### How to open
```
Ctryhackme@linux3:~$ crontab -e


GNU nano 4.8           /tmp/crontab.FaoQ2v/crontab                     
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
...
# m h  dom mon dow   command
@reboot /var/opt/processes.sh
```



### Crontabs require 6 specific values:

MIN	: What minute to execute at
HOUR	: What hour to execute at
DOM	: What day of the month to execute at
MON	: What month of the year to execute at
DOW	: What day of the week to execute at
CMD	: The actual command that will be executed.


### '*': every
```
0 *12 * * * cp -R /home/cmnatic/Documents /var/backups/
```

[Crontab Generator](https://crontab-generator.org/)  
[crontab guru](https://crontab.guru/)



---
### References
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)  
