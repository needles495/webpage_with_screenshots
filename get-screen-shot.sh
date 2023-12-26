#!/bin/bash
#[root@srv001-new ~]# cat /root/get-screen-shot.sh

parallel-ssh -i -h /root/product/ip-list-pssh "bash /home/zabbix_check/create.screenshot.sh"

rm -rf /tmp/image_test
mkdir /tmp/image_test

for i in `cat /root/product/ip-list-pssh`;do
        echo $i
        scp $i:/home/mia-asus1/zabbix_monitor.jpeg /tmp/image_test/$i.jpg &
        done
