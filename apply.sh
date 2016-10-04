#!/bin/bash

cp ./weight.service /etc/systemd/system/weight.service
chmod 664 /etc/systemd/system/weight.service

systemctl daemon-reload
systemctl enable weight.service
service weight restart
