# time modifiers    
   
[Specify time modifiers in your search](https://docs.splunk.com/Documentation/Splunk/8.2.5/Search/Specifytimemodifiersinyoursearch)   
[Time modifiers](https://docs.splunk.com/Documentation/Splunk/8.2.5/SearchReference/SearchTimeModifiers)   
   
```   
[+|-]<timeInt><timeUnit>@<timeUnit>   
```   
```[+|-]<timeInt><timeUnit>``` : calculate **FIRST** !   
then    
```@<timeUnit>```:snaps to the specified time unit   
  always round down(= go backwards)   

### ※ spl에 설정하기 전에 확인 방법   
검색 > 기간설정 > 고급(맨 아래) > 시작: 에 -53m@h 등 지정해서 22/04/06 오후 8시 0분 0초 등의 결과를 확인할 수 있다.

---
   
## time modifiers practice

```   
earliest=-h@h   
```   
the current time is 15:45:00    
The time modifier snaps to 14:00.   
   
```   
-1h@h	   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Wednesday, 05 February 2019, 12:00:00 P.M.   
1 hour ago, to the hour	   
   
```   
earliest=@d   
```   
since midnight (0:00)   
   
   
```   
-1d@d   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Tuesday, 04 February 2019, 12:00:00 A.M.   
Yesterday	   
```   
+1d@d	   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Thursday, 06 February 2019, 12:00:00 A.M.	   
Tomorrow   
   
```   
earliest=-2d@d   
```   
Search at 14:05 on April 28th.   
goes back to two days and snaps to the beginning of the day.    
The search looks for events starting from 00:00 on April 26th.   
   
```   
-7d@d	   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Wednesday, 28 January 2019, 12:00:00 A.M.   
7 days ago, 1 week ago today	   
```   
-7d@m	   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Wednesday, 28 January 2019, 01:37:00 P.M.   
7 days ago, snap to minute boundary	   
```   
earliest=-mon@mon latest=@mon   
```   
begins at the start of the previous month    
ends at the start of the current month.   
   
   
     
     
     
```   
@w0 or @w7 for Sunday   
@w1 for Monday   
...   
@w6 for Saturday   
```   
   
```   
eventtype=webaccess error earliest=@w0   
eventtype=webaccess error earliest=@w7   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Sunday, 02 February 2019, 12:00:00 A.M.	   
Beginning of the current week	   
```   
earliest=-5d@w1 latest=@w6   
```   
from the last full business week   
   
     
```   
eventtype=webaccess error earliest=@w1 latest=+7d@w6   
```   
starting from 12:00 A.M. of the Monday of the current week   
ending at 11:59 P.M. of the Friday of the current week.   
```   
eventtype=webaccess error earliest=-7d@w1 latest=@w6   
```   
starting from 12:00 A.M. of last Monday   
ending at 11:59 P.M. of last Friday.   
```   
index=myindex ((earliest=-24h latest<@d) OR (earliest>=@d+1h))   
```   
24 hours before the search is run, up to midnight   
starting at 1 hour after midnight or 1:00 A.M.   
   
   
```   
@q, @qtr, or @quarter   
```   
Jan 1, Apr 1, July 1, or Oct 1.   
   
   
   
   
chained relative time offsets   
     
     
```   
@d-2h	   
```   
10 P.M. last night.   
Snap to the beginning of today (12 A.M.) and subtract 2 hours from that time.   
```   
-mon@mon+7d   
```   
The 8th of last month at 12 A.M.   
One month ago, snapped to the first of the month at midnight, and add 7 days.   
   
```   
earliest=-2d@d latest=@d date_hour>=2 AND date_hour<5   
```   
from the last 2 days, excluding today   
between 2 am and 5 am    
                                                         
```                                    
((earliest=-24h latest<@d) OR (earliest>=@d+1h))   
```   
last 24 hours but omit the events from Midnight to 1:00 A.M.   
     
                                                         
---                                                         
     
      
### Simple    
   
```   
earliest=-30m latest=now   
```   
within the last 30 minutes   
```   
-60m	   
-60m@s   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Wednesday, 05 February 2019, 12:37:05 P.M.	   
60 minutes ago	   
```   
earliest=-2d   
```   
Search at 14:05 on April 28th.   
goes back exactly two days, starting at 14:05 on April 26th.   
   
```   
-24h	   
-24h@s   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Tuesday, 04 February 2019, 01:37:05 P.M.	   
24 hours ago (yesterday)	   
   
```   
+24h	   
+24h@s   
```   
Current time : Wednesday, 05 February 2019, 01:37:05 P.M   
Resulting time : Thursday, 06 February 2019, 01:37:05 P.M.	   
24 hours from now, tomorrow	   
   
```   
earliest=1   
```   
UNIX epoch time 1 is UTC January 1, 1970 at 12:00:01 AM.   
   
```   
earliest=0   
```   
time is not used in the search.   
   


---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)    
