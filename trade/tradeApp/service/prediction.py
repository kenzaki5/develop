# coding:utf-8
from bbService import bbService
from time import sleep
import requests
from datetime import datetime
import time
from config import config

class prediction:
    config=config()
    API_KEY=config.getApiKey()
    API_SECRET=config.getApiSecret()
    count=int(config.getCount())
    CURRENCY_PAIR="btc_jpy"
    candle_type="1min"
    datetime=datetime()
    bbservice=bbService(API_KEY,API_SECRET,CURRENCY_PAIR)

    def print_price(self, data):
        print( "時間： " + datetime.fromtimestamp(data["close_time"]).strftime('%Y/%m/%d %H:%M') + " 始値： " + str(data["open_price"]) + " 終値： " + str(data["close_price"]) )


    def check_candle(self, data):
        realbody_rate = abs(data["close_price"] - data["open_price"]) / (data["high_price"]-data["low_price"]) 
        increase_rate = data["close_price"] / data["open_price"] - 1

        if data["close_price"] < data["open_price"] : return False
        elif increase_rate < 0.0005 : return False
        elif realbody_rate < 0.5 : return False
        else : return True


    def check_ascend(self, data, last_data):
        if data["open_price"] > last_data["open_price"] and data["close_price"] > last_data["close_price"]:
            return True
        else:
            return False

    def predition(self):
        flag = 0

        while True:
            now = self.datetime.today().strftime("%Y%m%d")
            candle_stick=self.bbservice.getCandleStick(self.CURRENCY_PAIR, self.candle_type, now)
            last_data = self.convert_data(candle_stick[-2])
            data = self.convert_data(candle_stick[-1])
            
            if data["close_time"] != last_data["close_time"]:
                
                if flag == 0 and self.check_candle( data ):
                    flag = 1
                elif flag == 1 and self.check_candle( data )  and self.check_ascend( data,last_data ):
                    print("２本連続で陽線")
                    flag = 2
                elif flag == 2 and self.check_candle( data )  and self.check_ascend( data,last_data ):
                    print("３本連続で陽線 なので 買い！")
                    flag = 3
                else:
                    flag = 0
                
                last_data["close_time"] = data["close_time"]
                last_data["open_price"] = data["open_price"]
                last_data["close_price"] = data["close_price"]
                
            time.sleep(60)

    def convert_data(self, single_data):
        return { "close_time" : datetime.datetime.fromtimestamp(single_data[5])strftime("%Y%m%d"),
            "open_price" : int(single_data[0]),
            "high_price" : int(single_data[1]),
            "low_price" : int(single_data[2]),
            "close_price": int(single_data[3]) }
