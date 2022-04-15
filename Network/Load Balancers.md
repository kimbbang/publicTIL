# Load Balancers

ensuring high traffic websites can handle the load   
providing a failover if a server becomes unresponsive

When you request a website with a load balancer, the load balancer will receive your request first and then forward it to one of the multiple servers behind it.

If a server doesn't respond appropriately or doesn't respond, the load balancer will stop sending traffic until it responds appropriately again.


### round-robin  

sends it to each server in turn, or   
weighted, which checks how many requests a server is currently dealing with and   
sends it to the least busy server.


### health check  
perform periodic checks with each server to ensure they are running correctly

---


### References
[How The Web Works](https://tryhackme.com/module/how-the-web-works)    
