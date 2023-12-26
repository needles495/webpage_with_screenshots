#!/bin/bash

ssh 192.168.122.2 "bash /root/get-screen-shot.sh"
cd /var/www/termon/
rm *.jpg
scp 192.168.122.2:/tmp/image_test/*.jpg .
python3 sc_v3.py
python3 sc3_v1.py
#python3 sc2_v3.py
