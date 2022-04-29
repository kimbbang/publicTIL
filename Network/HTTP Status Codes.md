# HTTP Status Codes

## ranges

#### 100-199 - Information Response	
These are sent to tell the client the first part of their request has been accepted and they should continue sending the rest of their request. 

#### 200-299 - Success	
the client their request was successful.

#### 300-399 - Redirection	
These are used to redirect the client's request to another resource.   
This can be either to a different webpage or a different website altogether.

#### 400-499 - Client Errors	
Used to inform the client that there was an error with their request.

#### 500-599 - Server Errors	
This is reserved for errors happening on the server-side and usually indicate quite a major problem with the server handling the request.

---

## Common HTTP Status Codes

#### 200 - OK	
The request was completed successfully.

#### 201 - Created	
A resource has been created (for example a new user or new blog post).

#### 301 - Permanent Redirect
This redirects the client's browser to a new webpage or tells search engines that the page has moved somewhere else and to look there instead.

#### 302 - Temporary Redirect
only a temporary change and it may change again in the near future.

#### 400 - Bad Request
This tells the browser that something was either wrong or missing in their request.     
expected a certain parameter that the client didn't send.

#### 401 - Not Authorised
You are not currently allowed to view this resource until you have authorised with the web application,   
most commonly with a username and password.

#### 403 - Forbidden
You do not have permission to view this resource whether you are logged in or not.

#### 405 - Method Not Allowed
for example, you send a GET request to the resource /create-account when it was expecting a POST request instead.

#### 404 - Page Not Found
The page/resource you requested does not exist.

#### 500 - Internal Service Error
The server has encountered some kind of error with your request that it doesn't know how to handle properly.

#### 503 - Service Unavailable
This server cannot handle your request as it's either overloaded or down for maintenance.
if the web server cannot access its database and the application crashes

---
---

### Course
[TryHackMe - How The Web Works](https://tryhackme.com/module/how-the-web-works)    
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
