# coding:utf-8
import configparser
from slack import slackService
from trade_bb import tradeBb
import subprocess
import os
import sys
from config import config

slackService=slackService()
config=config()
tradeBb=tradeBb(0.01,200,2,"btc_jpy",True)

config.setExecFlg('1')

print('trade start!')
tradeBb.tradeBb()
print('trade end!')
