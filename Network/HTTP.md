# HTTP
port : 80  
HyperText Transfer Protocol  
is the set of rules used for communicating with web servers for the transmitting of webpage data

# HTTPS  
port : 443  
HyperText Transfer Protocol Secure  
is the secure version of HTTP

---

## URL

Uniform Resource Locator

```
http://user:password@tryhackme.com:80/view-room?id=1#task3
```

* http : **Scheme**: This instructs on what **protocol** to use for accessing the resource such as HTTP, HTTPS, FTP (File Transfer Protocol).  
* tryhackme.com : **Host**: The domain name or IP address of the server
* 80 : **Port**: usually 80 for HTTP and 443 for HTTPS, but this can be hosted on any port between 1 - 65535.  
* view-room : **Path**: The file name or location of the resource  
* id=1 : **Query String**: Extra bits of information that can be sent to the requested path.    
* task3 : **Fragment**: This is a reference to a location on the actual page requested.   
  This is commonly used for pages with long content and can have a certain part of the page directly linked to it, so it is viewable to the user as soon as they access the page.  
---

## HTTP methods

GET Request

This is used for **getting** information from a web server.

POST Request

This is used for submitting data to the web server and potentially **creating new** records

PUT Request

This is used for submitting data to a web server to **update** information

DELETE Request

This is used for **deleting** information/records from a web server.

---

## Example Request + common Header

### First line
```
GET / HTTP/1.1
POST /accounts/reset_password/ HTTP/1.1  
```
Type of web request 
  
### Host 
```
Host: tryhackme.com
```
tells the web server which website is being requested  
We tell the web server we want the website tryhackme.com    
Some web servers host multiple websites    
otherwise you'll just receive the default website for the server.  

### User-Agent
```
User-Agent: Mozilla/5.0 Firefox/87.0
User-Agent: Mozilla/5.0 Chrome/74    
```
your browser software and version number  
using the Firefox version 87 Browser  
using a Google Chrome (version 74) browser  

### Accept-Encoding

what types of compression methods the browser supports so the data can be made smaller for transmitting over the internet

### Cookie
```
Cookie: name=adam
```
Data sent to the server to help remember your information (see cookies task for more information).

### Referer 
```
Referer: https://tryhackme.com/
```
We are telling the web server that the web page that referred us to this one is https://tryhackme.com

### Last line 
```

```
HTTP requests always end with a blank line to inform the web server that the request has finished.

---

## Example Response + common Header

### First line
```
HTTP/1.1 200 OK
```
HTTP 1.1 version of the HTTP protocol, the HTTP Status Code in this case "200 Ok" 


### Server
```
Server: nginx/1.15.8
```
web server software and version number.

### Date
```
Date: Fri, 09 Apr 2021 13:34:03 GMT
```

### Content-Type
```
Content-Type: text/html
```
HTML, CSS, JavaScript, Images, PDF, Video, etc.

### Content-Length
```
Content-Length: 98
```
we can confirm no data is missing.

### Set-Cookie
```
Set-Cookie: name=adam
```
Information to store which gets sent back to the web server on each request (see cookies task for more information).

### Cache-Control

How long to store the content of the response in the browser's cache before it requests it again.

### Content-Encoding
What method has been used to compress the data to make it smaller when sending it over the internet.

### The information that has been requested, in this instance the homepage.
```
             # HTTP response contains a blank line to confirm the end of the HTTP response.
<html>
<head>
    <title>TryHackMe</title>
</head>
<body>
    Welcome To TryHackMe.com
</body>
</html>
```

---

## Cookies


a small piece of data that is stored on your computer  
Cookies are saved when you receive a "Set-Cookie" header from a web server.







---
---

### Course
[TryHackMe - How The Web Works](https://tryhackme.com/module/how-the-web-works)    
[TryHackMe - Network Fundamentals](https://tryhackme.com/module/network-fundamentals)
