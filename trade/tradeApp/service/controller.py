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
tradeBb=tradeBb(0.01,200,2,"btc_jpy")
res=watcher.watch()
if res:
    tradeBb.tradeBb()
    print("True")
else:
    os.system('./pyshell_stop.sh')
    print("False")
      
