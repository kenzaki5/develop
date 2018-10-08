#!/bin/sh
count=`ps aux | grep -v grep | grep controller.py | wc -l`

if [ $count = 0 ] ; then
cd /home/ec2-user/git/develop/trade/tradeApp/service/
python controller.py
fi

