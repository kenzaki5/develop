# coding:utf-8
from tradeApp/service/common/slack import slackService
from trade_bb_mona import tradeBb
import subprocess
import os
import sys
from watcher_mona import watcher_mona
from tradeStop import tradeStop

watcher=watcher_mona()
tradeStop=tradeStop()
tradeBb=tradeBb(100,0.5,2,"mona_jpy")
res=watcher.watch()
if res:
    tradeBb.tradeBb()
    print("True")
else:
    os.system('./pyshell_stop_mona.sh')
    print("False")
      
