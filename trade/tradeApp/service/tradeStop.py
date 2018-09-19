# coding:utf-8
import configparser

class tradeStop:
    def stop(self):
        config = configparser.ConfigParser()
        config.read('trade/tradeApp/service/config.ini', 'UTF-8')
        config['conf']['exec_flg']='0'