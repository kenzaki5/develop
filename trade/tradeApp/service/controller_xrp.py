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
tradeBb=tradeBb(50,0.1,2,"xrp_jpy")
res=watcher.watch()
if res:
    tradeBb.tradeBb()
    print("True")
else:
    os.system('./pyshell_stop_xrp.sh')
    print("False")
      
