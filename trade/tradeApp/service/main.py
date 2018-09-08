# coding:utf-8
from slack import slackService
from trade_bb import tradeBb
import subprocess
import os
import sys

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs)

if argc != 3:
    print("args is not 2")
    quit()

slackService=slackService()
tradeBb=tradeBb(argvs[1],argvs[2],"xrp_jpy")

print('trade start!')
tradeBb.tradeBb()
print('trade end!')
