#!/bin/sh
count=`ps aux | grep -v grep | grep controller.py | wc -l`

if [ $count = 1 ] ; then
ps aux | grep controller.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh
fi
