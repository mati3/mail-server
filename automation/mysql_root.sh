#!/bin/bash


MYSQL_ROOT_PASSWORD=password

ROOT_MYSQL=$(expect -c "
set timeout 1
spawn sudo mysql -u root -p

expect \"Enter password:\"
send \"$MYSQL_ROOT_PASSWORD\r\"
expect \"mysql>\"
send \"ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; 
	FLUSH PRIVILEGES;
	CREATE DATABASE roundcubemail /*!40101 CHARACTER SET utf8 COLLATE utf8_general_ci */;
	CREATE USER 'roundcube'@'localhost' IDENTIFIED BY 'contraderoundcube';
	GRANT ALL PRIVILEGES ON roundcubemail.* to 'roundcube'@'localhost';
	FLUSH PRIVILEGES;\r\"
expect eof
")

echo "$ROOT_MYSQL"

