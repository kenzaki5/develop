# coding:utf-8
import configparser
from slack import slackService
from trade_bb import tradeBb
import subprocess
import os
import sys

slackService=slackService()
config = configparser.ConfigParser()
config.read('trade/tradeApp/service/config.ini', 'UTF-8')
tradeBb=tradeBb(0.01,200,2,"btc_jpy")

config['conf']['exec_flg']='1'

print('trade start!')
tradeBb.tradeBb()
print('trade end!')
