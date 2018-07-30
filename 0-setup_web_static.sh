#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get install -y nginx
sudo service nginx start

sudo mkdir -p "/data/"
sudo mkdir -p "/data/web_static/"
sudo mkdir -p "/data/web_static/releases/"
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"
sudo touch "/data/web_static/releases/test/index.html"
sudo echo "Hello Holberton" | sudo tee "/data/web_static/releases/test/index.html"

linkTo="/data/web_static/current"
link_file="/data/web_static/releases/test/"
sudo ln -sf "$link_file" "$linkTo"
data="/data/"
sudo chown -R ubuntu:ubuntu "$data"
con="/etc/nginx/sites-enabled/default"
sudo sed -i "42i \\\\tlocation /hbnb_static/ {\n\t\talias $linkTo/;\n\t\tautoindex off;\n\t}\n" "$con"
sudo service nginx restart
