#!/bin/sh
count=`ps aux | grep -v grep | grep controller_mona.py | wc -l`

if [ $count = 1 ] ; then
ps aux | grep controller_mona.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh
fi
