wget https://artifacts.elastic.co/downloads/kibana/kibana-6.6.0-amd64.deb
shasum -a 512 kibana-6.6.0-amd64.deb 
sudo dpkg -i kibana-6.6.0-amd64.deb

sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service

vi /etc/kibana/kibana.yaml

sudo systemctl start kibana.service

mv kibana* ~
