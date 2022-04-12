# Operators

## &	
allows you to run commands in the **background** of your terminal.

※ Ctrl + Z : "pausing" the execution of a script or command  
※※ fg : bring background process back to focus

## &&	
allows you to combine multiple commands together in one line of your terminal.   
"command1 && command2" is worth noting that command2 will only run if command1 was successful.

## >	
is a redirector - meaning that we can take the output from a command (such as using cat to output a file) and direct it elsewhere.   
Note: If the file already exists, the contents will be **overwritten**!

## >>	
does the same function of the > operator but **appends** the output rather than replacing (meaning nothing is overwritten).


---

### References
[TryHackMe - Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals)


