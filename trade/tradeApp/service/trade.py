# coding:utf-8
import configparser
from slack import slackService
from trade_bb import tradeBb
import subprocess
import os
import sys

class trade:
    slackService=slackService()
    tradeBb=tradeBb(0.01,200,2,"btc_jpy")
    print('trade start!')
    tradeBb.tradeBb(self)
    print('trade end!')
