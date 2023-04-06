sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo apt install python3
sudo apt install virtualenv

sudo apt install -y mosquitto                       # if brocker be run on client host
sudo apt install -y mosquitto-clients

client:
    virtualenv -p python3 client-env
    source client-env/bin/activate
    pip install paho-mqtt


server:
    virtualenv -p python3 server-env
    source server-env/bin/activate
    pip install numpy
    pip install paho-mqtt
