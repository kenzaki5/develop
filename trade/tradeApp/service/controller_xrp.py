# coding:utf-8
from slack import slackService
from trade_bb_xrp import tradeBb
import subprocess
import os
import sys
from watcher_xrp import watcher_xrp
from tradeStop import tradeStop

watcher=watcher_xrp()
tradeStop=tradeStop()
tradeBb=tradeBb(500,0.05,2,"xrp_jpy")
while True:
    res=watcher.watch()
    if res:
        tradeBb.tradeBb()
        print("True")
    else:
        tradeStop.stop()
        print("False")
      