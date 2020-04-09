#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
echo "Configuration went well!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "/pass the PHP/i \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
