sudo apt-get update<br>
sudo apt-get upgrade<br>
sudo apt-get install python3-pip<br>
sudo apt install python3<br>
sudo apt install virtualenv<br>
<br>
sudo apt install -y mosquitto    # if brocker be run on client/server host
sudo apt install -y mosquitto-clients<br>
<br>
client:<br>
    virtualenv -p python3 client-env<br>
    source client-env/bin/activate<br>
    pip install -r client-recuirements.txt>
<br>
<br>
server:<br>
    <tb>virtualenv -p python3 server-env<br>
    source server-env/bin/activate<br>
    pip install -r server-recuirements.txt
