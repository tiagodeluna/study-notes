# OWASP Top 10 List

* A10 - Underprotected APIs
    - Vulnerable APIs are used to exploit the application it is built upon
* A9 - Using components with known vulnerabilities
    - Vulnerable components are exploited and have same privileges as application
* A8 - Cross-site Request Forgery (CSRF)
    - Attacker send forged HTTP request authenticated as victim
* A7 - Insufficient attack protection
    - When applications have no ability to detect, prevent, or respond to attacks
* A6 - Sensitive data exposed
    - When sensitive data is stolen by an attacker
* A5 - Security misconfiguration
    - When insecure configurations on applications and servers are used, as well as using defaults and not keeping software up to date
* A4 - Broken access control
    - Restrictions on authenticated users are not enforced (too many privileges)
* A3 - Cross-site scripting (XSS)
    - When application places untrusted data in a new web page without using validation
* A2 - Broken authentication and session management
    - Functions of the application related to authentication and session management are implemented incorrectly
* A1 - Injection
    - Untrusted data is sent to the interpreter by an attacker

# CSRF Mitigation

* Secure coding
* OWASP CSRFGuard tool
* Cookies
    - "SameSite=strict" flag, to check the origin (where the request is coming from)
  