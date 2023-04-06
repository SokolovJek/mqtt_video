sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo apt install python3
sudo apt install virtualenv
virtualenv -p python3 server-en

sudo apt install -y mosquitto                       # if brocker be run on client host
sudo apt install -y mosquitto-clients

pip install paho-mqtt