# IoT-mini-project-1

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#server-and-sensor-details">Server and Sensor details</a>
    </li>
    <li>
      <a href="video-link">Video Link</a>
    </li>
    <li>
      <a href="#preparing-the-backend">Preparing the Backend</a>
    </li>
    <li>
      <a href="#preparing-the-frontend">Preparing the Frontend</a>
    </li>
    <li>
      <a href="preparing-the-IoT-devices">Preparing the IoT Devices</a>
    </li>
  </ol>
</details>

<br>

## Server and Sensor details
Cloud server:
```
IPv4: 16.170.238.248
IPv6: 2a05:d016:eea:c800:ca30:d1a0:b5e6:7e41
```
Grenoble IP:
```
start range: 2001:660:5307:3101::/64
ending range: 2001:660:5307:317f::/64
```
<br>

## Video Link

<a href="https://unioulu-my.sharepoint.com/:v:/g/personal/msadeghi23_student_oulu_fi/EdusQCE2X8JJpt6V6e_nbnoBMqiTgkeJRsuZNdQCH-OLjg?e=fLEIfU&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D">link</a>

<br>

## Preparing the Backend


Step 1: Login to your backend cloud server
```
ssh user@server
```


Step 2: Clone this repository
```
https://github.com/eclipse/mosquitto.rsmb.git
```


Step 3: Go to src directory and compile
```
cd rsmb/src
make
```


Step 4: Make a new configuration
```
nano config.conf
```
put the below configuration
```
# Uncomment this to show you packets being sent and received
trace_output protocol

# Normal MQTT listener
listener 1883 INADDR_ANY
ipv6 true

# MQTT-SN listener
listener 1883 INADDR_ANY mqtts
ipv6 true
```



Step 5: Run MQTT server using the above configuration
```
./broker_mqtts config.conf
```

Leave the terminal open




<br>

## Preparing the Frontend


Step 1: Clone the repository
```
git clone https://github.com/p4l4s6/IoT-mini-project-1.git
```


Step 2: create a virtual environment
```
python -m venv venv
```


Step 3: Install the requirements
```
pip install -r requirements.txt
```


Step 4: Run the frontend code
```
python frontend.py
```







<br>

## Preparing the IoT Devices

```
Cloud server IPv4: 16.170.238.248
Cloud server IPv6: 2a05:d016:eea:c800:ca30:d1a0:b5e6:7e41
```

Step 1: Log in to the IoT lab server using SSH
```
ssh USERNAME@grenoble.iot-lab.info
```


Step 2: Submit an experiment
```
iotlab-experiment submit -n NAME_OF_EXP -d 120 -l 2,archi=m3:at86rf231+site=grenoble
```

Wait for the experiment to be started


Step 3: Get the id’s of nodes
```
iotlab-experiment get -i <exp_id> -p
```


Step 4: Clone the RIOT repo
```
git clone https://github.com/RIOT-OS/RIOT.git
```


Step 5: Go to the RIOT directory and set source
```
cd RIOT
source /opt/riot.source
```


Step 6: compile gnrc border router
```
make ETHOS_BAUDRATE=500000 DEFAULT_CHANNEL=26 BOARD=iotlab-m3 -C examples/gnrc_border_router clean all
```


Step 7: Flash the router firmware in the first node
```
iotlab-node --update examples/gnrc_border_router/bin/iotlab-m3/gnrc_border_router.elf -l grenoble,m3,ID_OF_M3_FIRST_NODE
```


Step 8: Create a network interface for the border router
```
sudo ethos_uhcpd.py m3-ID_OF_BORDER_NODE  tap0 2001:660:5307:3101::/64
```

Leave terminal open


Step 9: open a new terminal and login to IoT lab server again using ssh and clone the repo
```
git clone https://github.com/p4l4s6/IoT-mini-project-1.git
```


Step 10: go to the project directory and set source and compile the firmware
```
cd IoT-mini-project-1/iot/
source /opt/riot.source
make
```


Step 11: Flash firmware to the second node
```
iotlab-node --update bin/iotlab-m3/emcute_mqttsn.elf -l grenoble,m3,ID_OF_M3_SECOND_NODE
```


Step 12:  Open the second node shell
```
nc m3-ID_OF_M3_SECOND_NODE 20000
```


Step 13: Connect to the backend server
```
con 2a05:d016:eea:c800:ca30:d1a0:b5e6:7e41 1885
```


Step 14: Print the data into the terminal
```
data
```

Step 14: send data to MQTT server
```
apub
```


