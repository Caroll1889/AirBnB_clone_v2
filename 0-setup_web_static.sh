#!/usr/bin/env bash
#script that sets up the web servers for the deployment of web_static

apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "test" | tee -a /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -ie "45ilocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service ngnix start
