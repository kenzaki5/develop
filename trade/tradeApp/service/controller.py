# coding:utf-8
from slack import slackService
from trade_bb import tradeBb
import subprocess
import os
import sys
from watcher import watcher
from tradeStop import tradeStop

watcher=watcher()
tradeStop=tradeStop()
while True:
    res=watcher.watch()
    if res:
        subprocess.check_call('forever start /home/ec2-user/node/server.js')
        print("True")
    else:
        tradeStop.stop()
        print("False")
      