## Install and configure a webmail.

we going to install a service of email web, for it, we need undestad how working.

![image](/img/architecture.png)

###  Mail system architecture:
	
**Transfer agents (MTA)**, within of which we have:

* Of distribution (SMTP). It send mail between servers.
* Of end delivery (POR3, IMAP). They allow the user to manage his mail through a remote machine, that is, he communicates with his email server.

**User agents (MDA)**, is an application that works as a client, collects and sends email, there are different types of user agents for email:		

* A email client aplication or MUA (Mail User Agent) allows you to store emails locally, not having to be connected to read them.
* A web interface, which is accessed with a web browser,  it is confortable because it allows you to view and store messages from anywhere, although it may be slower.

![image](/img/service_email.png)

### Steps in send / receive mail.
* Alice compose  through her User Agent,  a message addressed to the destination user's email.
* The computer asks the DNS server for the address of the domain name of your mail server. As we are going to do a local test, we will change our local file to assign host names to IP addresses in /etc/hosts.
* The message is sent with SMTP to the mail server of the Alice user, in the same way it sends it to the destination mail server.
* Bob's mail server locates the message in the mailbox, Bob invokes his User Agent to read the message using POP3 or IMAP.

### Tools Used

- MySQL as database.
- Apache2 as HTTP Server, it is open-source and free. It is write in php.
- RoundCube as Webmail.
- Dovecot for IMAP and POP3
- Postfix for SMTP
