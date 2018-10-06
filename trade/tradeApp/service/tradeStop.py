# coding:utf-8
from config import config

class tradeStop:
    config=config()
    def stop(self):
        self.config.setExecFlg('0')