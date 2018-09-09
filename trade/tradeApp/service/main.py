# coding:utf-8
from slack import slackService
from trade_bb import tradeBb
import subprocess
import os
import sys

slackService=slackService()
tradeBb=tradeBb(500,0.01,"xrp_jpy")

print('trade start!')
tradeBb.tradeBb()
print('trade end!')
