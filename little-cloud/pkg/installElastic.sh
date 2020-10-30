sudo apt-get update

# sudo chown ubuntu:ubuntu /opt

sudo apt install openjdk-8-jre-headless


wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.0.deb
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.0.deb.sha512
shasum -a 512 -c elasticsearch-6.6.0.deb.sha512
sudo dpkg -i elasticsearch-6.6.0.deb

mv elastic* ~

sudo systemctl enable  elasticsearch
sudo systemctl start  elasticsearch

