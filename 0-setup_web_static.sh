#!/usr/bin/env bash
# set my servers for deployment

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create a fake html for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# give ownership of /data/ to user and group
sudo chown -R ubuntu:ubuntu /data/

# nginx configuration
sudo sed -i "53i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
# Restart nginx
sudo service nginx restart
