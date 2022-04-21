# Index time versus search time
[Index time versus search time](https://docs.splunk.com/Documentation/Splunk/8.2.6/Indexer/Indextimeversussearchtime)

## At index time   
Index-time processes take place between the point when the data is consumed and the point when it is written to disk.      
   
Default field extraction (such as **host, source, sourcetype, and timestamp**)      
Static or dynamic host assignment for specific inputs      
Default host assignment overrides      
Source type customization      
Custom index-time field extraction      
Structured data field extraction      
Event timestamping      
Event linebreaking      
Event segmentation (also happens at search time)      
   
   
## At search time   
Search-time processes take place while a search is run, as events are collected by the search.       
   
Event segmentation (also happens at index time)      
Event type matching      
Search-time field extraction (automatic and custom field extractions, including multivalue fields and calculated fields)      
Field aliasing      
Addition of fields from lookups      
Source type renaming      
Tagging      


---
---

### Course
[Splunk Inc.- Splunk Search Expert 102](https://www.coursera.org/learn/splunk-search-expert-102)    
