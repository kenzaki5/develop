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
tradeBb=tradeBb(0.01,100,2,"btc_jpy")
while True:
    res=watcher.watch()
    if res:
        tradeBb.tradeBb()
        print("True")
    else:
        tradeStop.stop()
        print("False")
      
