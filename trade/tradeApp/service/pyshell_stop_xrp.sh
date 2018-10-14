#!/bin/sh
count=`ps aux | grep -v grep | grep controller_xrp.py | wc -l`

if [ $count = 1 ] ; then
ps aux | grep controller_xrp.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh
fi

