
**Donwload or copy the automation folder of this respository**

    git clone https://github.com/mati3/mail-server.git

**Changed the name email-server**

    mv email-server email-second-server

**Re-clone the repository**    

    git clone https://github.com/mati3/mail-server.git

- We already have two server, now we goint to changed email-second-server configuration.

**Files to modify**

- Vagrantfile:

    Changed this:

       config.vm.network "forwarded_port", guest: 80, host: 80, host_ip: "0.0.0.0"
       config.vm.network "private_network", ip: "192.168.56.101"
       config.vm.network "forwarded_port", guest: 110, host: 110
       config.vm.network "forwarded_port", guest: 995, host: 995
       config.vm.network "forwarded_port", guest: 143, host: 143
       config.vm.network "forwarded_port", guest: 993, host: 993
       config.vm.network "forwarded_port", guest: 25, host: 25
       config.vm.network "forwarded_port", guest: 465, host: 465
       config.vm.network "forwarded_port", guest: 443, host: 443
    To this:

       config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "0.0.0.0"
       config.vm.network "private_network", ip: "192.168.56.200"
       config.vm.network "forwarded_port", guest: 110, host: 1100
       config.vm.network "forwarded_port", guest: 995, host: 9950
       config.vm.network "forwarded_port", guest: 143, host: 1430
       config.vm.network "forwarded_port", guest: 993, host: 9930
       config.vm.network "forwarded_port", guest: 25, host: 250
       config.vm.network "forwarded_port", guest: 465, host: 4650
       config.vm.network "forwarded_port", guest: 443, host: 4430

- Fabfile.py:

        (1)Search and changet this:

            with ConfigFile('/etc/apache2/sites-available/roundcube.conf', use_sudo = True ) as conf:
                conf.update( '#ServerName www.example.com' , '\tServerName 192.168.56.101' )
                conf.update( 'ServerAdmin webmaster@localhost' , '\tServerAdmin examplemail.com')
        (1)For this:

            with ConfigFile('/etc/apache2/sites-available/roundcube.conf', use_sudo = True ) as conf:
                conf.update( '#ServerName www.example.com' , '\tServerName 192.168.56.200' )
                conf.update( 'ServerAdmin webmaster@localhost' , '\tServerAdmin example.com')

        (2)Search and changet this:

            with ConfigFile('/etc/postfix/main.cf', use_sudo = True ) as conf:
                conf.update( 'mydestination' , 'mydestination = $myhostname, examplemail.com, vagrant.vm, localhost.vm, localhost' )
                conf.update( 'mynetworks' , 'mynetworks = 192.168.56.101, 127.0.0.0/8' )

            run('echo "user1" | sudo adduser user1')# contraseña user1
            run('sudo usermod -aG sudo user1')
            run('echo "user2" | sudo adduser user2')# contraseña user2
            run('sudo usermod -aG sudo user2')

        (2)For this:

            with ConfigFile('/etc/postfix/main.cf', use_sudo = True ) as conf:
                conf.update( 'mydestination' , 'mydestination = $myhostname, example.com, vagrant.vm, localhost.vm, localhost' )
                conf.update( 'mynetworks' , 'mynetworks = 192.168.56.200, 127.0.0.0/8' )
            run('echo "user3" | sudo adduser user3')# contraseña user3
            run('sudo usermod -aG sudo user3')
            run('echo "user4" | sudo adduser user4')# contraseña user4
            run('sudo usermod -aG sudo user4')


**Enter your email-server folder**

    cd email-server

**Starts virtual machine**

    vagrant up

**Run fabric**

    fab -f fabfile.py -H vagrant@192.168.56.101 Install

**Enter your email-second-server folder**

    cd email-second-server

**Starts virtual machine**

    vagrant up

**Run fabric**

    fab -f fabfile.py -H vagrant@192.168.56.200 Install

We go to the browser, put "192.168.56.101/installer", [checking install](configure.md), and we already can enter in your email in "192.168.56.101".

Open anoter tab in the browser, put "192.168.56.200/installer", [checking install](configure.md), and we already can enter in your email in "192.168.56.200".

We try sending an email from one server to another.
