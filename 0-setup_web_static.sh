#!/usr/bin/env bash
# Configurating the web server for deployment

# Installing nginx
sudo apt-get update
sudo apt-get install -y nginx

# Initiate the variable with the folder
data="/data/"
data_stat="/data/web_static/"
data_stat_rel="/data/web_static/releases/"
data_stat_shar="/data/web_static/shared/"
data_stat_rel_test="/data/web_static/releases/test/"
html_file="/data/web_static/releases/test/index.html"

# Create the folder if doesn't exists
if [ ! -d "$data" ]; then mkdir -p "$data"; fi
if [ ! -d "$data_stat" ]; then mkdir -p "$data_stat"; fi
if [ ! -d "$data_stat_rel" ]; then mkdir -p "$data_stat_rel"; fi
if [ ! -d "$data_stat_shar" ]; then mkdir -p "$data_stat_shar"; fi
if [ ! -d "$data_stat_rel_test" ]; then mkdir -p "$data_stat_rel_test"; fi

# Create the html file with content
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" >> "$html_file"

# Create the symbolic link to the folder
sl_name="/data/web_static/current"
sudo ln -sf "$data_stat_rel_test" "$sl_name"

# Give ownership and group of /data/ folder to ubuntu user
sudo chown -hR ubuntu:ubuntu "$data"

# Update the configuration off nginx server
config_file="/etc/nginx/sites-available/default"
new_string="server_name _;\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}\n"
sudo sed -i "s/server_name _;/$new_string/" "$config_file"

# Restarting nginx server
sudo service nginx restart
