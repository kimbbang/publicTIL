# Command types

## Streaming commands
A streaming command operates on each event as the event is returned by a search.

eval, tags, streamstats

## Generating commands
A generating command generates events or reports from one or more indexes without transforming the events.

search 

## Transforming commands
A transforming command orders the results into a data table. The command "transforms" the specified cell values for each event into numerical values for statistical purposes.

chart, stats, table, timechart

## Orchestrating commands
Orchestrating commands control some aspect of how a search is processed. They do not directly affect the final result set of the search. For example, you might apply an orchestrating command to a search to enable or disable a search optimization that helps the overall search complete faster.

lookup

## Dataset processing commands
A dataset processing command is a command that requires the entire dataset before the command can run. Some of these commands fit into other command types in specific situations or when specific arguments are used.

append, bin, dedup, sort 



---
---

### Course
[docs.splunk - Command types](https://docs.splunk.com/Documentation/Splunk/8.2.6/SearchReference/Commandsbytype)    
