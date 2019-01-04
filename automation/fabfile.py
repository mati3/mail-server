
# coding: utf-8

from fabric.api import *
from fabric.contrib import files
from util import * 

# https://github.com/briancline/fabric-scripts/blob/master/appserver-php-ubuntu.py

def Install():

	run('sudo apt update')
	run('sudo apt-get install mysql-server -y')
	run('sudo apt install expect -y')
	run('cd /vagrant/automation && chmod +x mysql_secure.sh')
	run('cd /vagrant/automation && ./mysql_secure.sh')

	run('sudo apt install apache2 -y ')
	run('sudo ufw allow imap')
	run('sudo ufw allow smtp') 
	run('sudo ufw allow in "Apache Full"')
	run('sudo apt install php libapache2-mod-php php-mysql php-xml php-mbstring php-intl -y')
	
	with ConfigFile('/etc/php/7.2/apache2/php.ini', use_sudo = True ) as conf: 
  		conf.update( ' date.timezone = ' , ' date.timezone = "Europe/Madrid"  ' )

	run('sudo systemctl restart apache2')
	run('wget https://github.com/roundcube/roundcubemail/releases/download/1.3.6/roundcubemail-1.3.6-complete.tar.gz')
	run('tar -xvzf roundcubemail-1.3.6-complete.tar.gz')
	run('sudo mv roundcubemail-1.3.6 /var/www/html/roundcube')
	run('sudo chown -R www-data:www-data /var/www/html/roundcube')
	run('sudo chmod -R 775 /var/www/html/roundcube')

	run('cd /vagrant/automation && chmod +x mysql_root.sh')
	run('cd /vagrant/automation && ./mysql_root.sh') 

	run('sudo systemctl restart mysql')
	run('echo "$(expect -c "spawn cd /var/www/html/roundcube && mysql -u roundcube -p roundcubemail < /var/www/html/roundcube/SQL/mysql.initial.sql  expect \"Enter password:\" send \"contraderoundcube\r\"  except eof " )" ') 
	run('sudo apt purge expect -y')
	run('sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/roundcube.conf')

	with ConfigFile('/etc/apache2/sites-available/roundcube.conf', use_sudo = True ) as conf: 
  		conf.update( '#ServerName www.example.com' , '\tServerName 192.168.56.101' )
		conf.update( 'ServerAdmin webmaster@localhost' , '\tServerAdmin examplemail.com')
		conf.update( 'DocumentRoot /var/www/html' , '\t DocumentRoot /var/www/html/roundcube ')
		conf.update( "ErrorLog" , "\t ErrorLog ${APACHE_LOG_DIR}/roundcube-error.log")
		conf.update( 'CustomLog' , '\tCustomLog ${APACHE_LOG_DIR}/roundcube-access.log combined ')
		conf.update( '</VirtualHost>' , '#add directory')
		conf.update( 'alfinaldelfichero','\t<Directory /var/www/html/roundcube>\n\t\tOptions -Indexes \n\t\tAllowOverride All\n\t\tOrder allow,deny\n\t\tallow from all \n\t</Directory> \n</VirtualHost>')

	run('sudo a2dissite 000-default')
	run('sudo a2ensite roundcube')
	run('sudo a2enmod rewrite')
	run('sudo apache2ctl restart')
	run('sudo apt install dovecot-imapd -y')

	run('sudo DEBIAN_FRONTEND=noninteractive apt-get install postfix')
	with ConfigFile('/etc/postfix/main.cf', use_sudo = True ) as conf:
  		conf.update( 'mydestination' , 'mydestination = $myhostname, examplemail.com, vagrant.vm, localhost.vm, localhost' )
		conf.update( 'mynetworks' , 'mynetworks = 192.168.56.101, 127.0.0.0/8' )

	run('echo "user1" | sudo adduser user1')# contraseña user1
	run('sudo usermod -aG sudo user1')
	run('echo "user2" | sudo adduser user2')# contraseña user2
	run('sudo usermod -aG sudo user2')

	with ConfigFile('/etc/hosts', use_sudo = True ) as conf:
  		conf.update( 'finaldelarchivo' , '192.168.56.101  examplemail.com' )
		conf.update( 'finaldelarchivo' , '192.168.56.200  example.com' )

	run('sudo systemctl restart apache2')
