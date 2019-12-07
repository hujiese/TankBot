#!/bin/bash

cd /home/pi

sudo ./create_ap/create_ap -n wlan0 father myfather &

sleep 2

cd /home/pi/workspace/tankRobot/server

./gpio_server.py &

#sleep 2

#ps -ef | grep /usr/bin/python | grep -v grep | awk '{print $2}' | xargs kill -9

#sleep 2

#cd /home/pi/workspace/tankRobot/server

#./gpio_server.py

sleep 2

cd /home/pi/mjpg-streamer/mjpg-streamer-experimental

./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www" &




