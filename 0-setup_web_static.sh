#!/usr/bin/env bash
# 

# Update server and install nginx
sudo apt update
sudo apt install -y nginx

# Configures firewall to allow Nginx connections
sudo ufw allow 'Nginx HTTP'

# Create new directories: /data/web_static/shared & /data/web_static/releases/test
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create Symbolic link of current directory to test directory
sudo ln -sf /data/web_static/releases/test /data/web_static/current

printf %s "
    <html>
        <head>
        </head>
        <body>
            Holberton School
        </body>
    </html>
" | sudo tee /data/web_static/releases/test/index.html

# Give ownership of /data to ubuntu and group
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
printf %s "server{
    listen      80;
    listen      [::]:80;
    root        /data/web_static/release/test;
    index       index.html index.htm;

    location /hbnb_static{
        alias    /data/web_static/current;
    }
}" |  sudo tee /etc/nginx/sites-available/default


sudo service nginx restart
