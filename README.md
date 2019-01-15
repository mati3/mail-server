## Install and configure a webmail.

we are going to install a web email service, for it, we need to undestand how it works.

![image](/img/architecture.png)

###  Mail system architecture:

**Transfer agents (MTA)**, within of which we have:

* Of distribution (SMTP). It send mail between servers.
* Of end delivery (POR3, IMAP). They allow the user to manage his mail through a remote machine, that is, he communicates with his email server.

**User agents (MDA)**, is an application that works as a client, collects and sends email, there are different types of user agents for email:		

* A email client aplication or MUA (Mail User Agent) allows you to store emails locally, not having to be connected to read them.
* A web interface, which is accessed with a web browser,  it is confortable because it allows you to view and store messages from anywhere, although it may be slower.

![image](/img/service_email.png)

### Steps in send/receive mail.
* Alice compose  through her User Agent,  a message addressed to the destination user's email.
* The computer asks the DNS server for the address of the domain name of your mail server. As we are going to do a local test, we will change our local file to assign host names to IP addresses in /etc/hosts.
* The message is sent with SMTP to the mail server of the Alice user, in the same way it sends it to the destination mail server.
* Bob's mail server locates the message in the mailbox, Bob invokes his User Agent to read the message using POP3 or IMAP.

### Tools Used

- Ubuntu-18.04 as operating systems.
- VirtualBox to run the operating systems.
- Vagrant as development environment.
- Apache2 as HTTP Server, it is open-source and free. It is write in php.
- RoundCube as Webmail.
- MySQL as database.
- Dovecot for IMAP and POP3.
- Postfix for SMTP.



The first that we have doing is install vagrand and create a file [vagrantfile](Vagrantfile), we have to open the ports that we need to all the protocols using. we give to the virtual machine the IP: 192.168.56.100

We install in our virtual machine: mysql, apache2, php, roundcube, dovecto, postfix and two user for send email betwen they. [Link to the extens explain](doc/configure.md)

We put in the browser the address of our service 192.168.56.100.
We enter with the user vagrant.

![image](/img/roundcube_01.png)

We have two users, mati and sammy, mati send an email to sammy:

![image](/img/roundcube_02.png)

We view how sammy to receivent:

![image](/img/roundcube_03.png)


***[To automate server installation and configuration](doc/automation.md)***

Now that we have automated the installation and configuration of the server, we are going to mount two servers to see if they communicate.

We just have to duplicate the tasks.

[Issues to take into account to mount two servers.](doc/issues.md)

As we can see the servers communicate properly.

![image](/img/roundcube_04.png)
