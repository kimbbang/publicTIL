# Web Server

a software that listens for incoming connections and then utilises the HTTP protocol to deliver web content to its clients  
A Web server delivers files from what's called its root directory
Apache, Nginx, IIS and NodeJS



## default location

Nginx and Apache share the same default location of /var/www/html in Linux operating systems,  
IIS uses C:\inetpub\wwwroot for the Windows operating systems. 

if you requested the file http://www.example.com/picture.jpg,   
it would send the file /var/www/html/picture.jpg from its local hard drive.


## Virtual Hosts

Web servers can host multiple websites with different domain names; to achieve this, they use virtual hosts



Virtual Hosts can have their root directory mapped to different locations on the hard drive.   
For example, one.com being mapped to /var/www/website_one,   
two.com being mapped to /var/www/website_two  




---

### References
[How The Web Works](https://tryhackme.com/module/how-the-web-works)    
[Wikipedia - Web server](https://en.wikipedia.org/wiki/Web_server)