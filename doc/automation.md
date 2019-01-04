**Install Fabric:**
        
    sudo apt install fabric -y

**Donwload or copy the automation folder of this respository**

    git clone https://github.com/mati3/mail-server.git

**Enter your email-server folder**

    cd email-server

**Starts virtual machine**

    vagrant up

**Run fabric**

    fab -f automation/fabfile.py -H vagrant@192.168.56.101 Install


Password: vagrant

We go to the browser, put "192.168.56.101/installer", [checking install](configure.md), and we already can enter in your email in "192.168.56.101".

