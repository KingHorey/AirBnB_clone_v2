#!/usr/bin/env bash
# Install nginx and create folders
# check nginx existence and install if it does not exist

nginx_check=$(whereis nginx | cut -d ":" -f 2| wc -w) > /dev/null
if [ "${nginx_check}" -le 1 ];
then
	sudo apt update
	sudo apt install -y nginx
	sudo service nginx start
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

# get the line location / is on
location=$(grep -n "location /" /etc/nginx/sites-available/default | head -1 | cut -d ":" -f 1)

# add the location /hbnb_static/ { } block to the default Nginx configuration
export replacement="\tlocation /hbnb_static {\n\t\t alias /data/web_static/current \n"
sed -i "${location}c\ $replacement" /etc/nginx/sites-available/default

# populate index.html with html boilerplate
echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html

# delete the symbolic link /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-enabled/default

# create a new symbolic link /etc/nginx/sites-enabled/default to /etc/nginx/sites-available/default
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

sudo service nginx restart
exit 0
