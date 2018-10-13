#!/bin/sh
count_xrp=`ps aux | grep -v grep | grep controller_mona.py | wc -l`

if [ $count_xrp = 0 ] ; then
cd /home/ec2-user/git/develop/trade/tradeApp/service/
python controller_mona.py
fi

