#!/usr/bin/env bash
# Install nginx and create folders
# check nginx existence and install if it does not exist

nginx_check=$(whereis nginx | cut -d ":" -f 2| wc -w) > /dev/null
if [ "${nginx_check}" -le 1 ];
then
	sudo apt update
	sudo apt install -y nginx
	sudo service nginx start
else
	[ -d /data/web_static/releases/test ] || sudo mkdir -p /data/web_static/releases/test
	[ -d /data/web_static/shared ] || sudo mkdir -p /data/web_static/shared
	if [ -L /data/web_static/current ]; 
	then 
		sudo rm /data/web_static/current
		sudo ln -s /data/web_static/releases/test /data/web_static/current
	else
		sudo ln -s /data/web_static/releases/test /data/web_static/current
	fi
	echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
	sudo chown -R ubuntu:ubuntu /data/
fi

# update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# create a backup of config file
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak

# add the location /hbnb_static/ { } block to the default Nginx configuration
export replacement="\tlocation /hbnb_static {\n\t\t alias /data/web_static/current \n\t}\n"
sudo sed -ie '48a\ '"${replacement}"'' /etc/nginx/sites-available/default;
