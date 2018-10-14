# coding:utf-8
from bbService import bbService
import time
from slack import slackService
from decimal import (Decimal, ROUND_DOWN)
from config import config
from statistics import mean, median,variance,stdev

class tradeBb:
    config=config()
    API_KEY=config.getApiKey()
    API_SECRET=config.getApiSecret()
    #取引所のパラメータ
    order_min_size=0      #数量最小値
    order_digit   =0      #数量の桁数　ex. 3=0.001
    fee_rate      =0      #取引手数料のレート(%)
    #取引パラメータ
    buy_unit      =0      #購入単位
    profit        =0      #価格差
    CURRENCY_PAIR=""

    bbservice=bbService(API_KEY,API_SECRET,CURRENCY_PAIR)
    slackService=slackService()
    pair=""

    exceptionCnt=0
    oidArray=[]
    
    buyadd=0.0
    add=0.0
    buy_price=0
    stay=True

    #コンストラクタ
    def __init__(self,buyUnit,profit,orderDigit,currencyPair):
        self.order_min_size=buyUnit
        self.order_digit=orderDigit
        self.buy_unit=buyUnit
        self.profit=float(profit)
        self.pair=currencyPair
        self.CURRENCY_PAIR=currencyPair

    def tradeBb(self):
        while True:
            self.buyadd=0.0
            self.add=0.0
            ob=self.bbservice.orderbook(self.pair)
            buy_price=float(ob["bids"][0][0])
            self.buy_price=buy_price
            #購入数量を計算。 購入数量 = 数量*(1+fee*2) - BTC残高
            balance=self.bbservice.balance()
            print("Log : JPY {0}".format(float(balance["jpy"])))
            self.slackService.requestOnSlack("Log : JPY {0}".format(float(balance["jpy"])))
            buy_amount=round(float(self.buy_unit)*(1+0.01*self.fee_rate*2) - float(balance["xrp"]),self.order_digit)
            if float(self.buy_price) > float(buy_price):
                if (float(self.buy_price) - float(buy_price)) > 500:
                    self.stay=False
            if buy_amount > 0:
                #BTC残高が不十分なら注文の最小値を考慮して追加購入。
                buy_amount=max(self.order_min_size,buy_amount)
                #単位の整形
                #
                #JPY残高の確認
                if float(balance["jpy"])<buy_amount*buy_price:
                    print("Log : Insufficient JPY balance")
                    break
                #注文 BTCの場合はpriceを整数に強制する。
                if self.stay:
                    #print("Log : Buy order {0} x {1}".format(float(buy_price),buy_amount))
                    #self.slackService.requestOnSlack("Log : Buy order {0} x {1}".format(float(buy_price),buy_amount))
                    for i in range(0,5):
                        time.sleep(2)
                        try:
                            self.buyadd += 0.01
                            price=buy_price + self.buyadd
                            oid=self.bbservice.order(self.pair,price,buy_amount,"buy","limit")
                            self.oidArray.append(oid)
                        except Exception as e:
                            print("exception buy limit")
                            print(e)
                            self.exceptionCnt+=1
                            if self.exceptionCnt > 5:
                                self.bbservice.cancel(self.pair,oid)
                                print("Log : Sell canceled! oid={0}".format(oid))
                                self.exceptionCnt=0
                                time.sleep(5)
                            continue
                    #注文がサーバーで処理されるまで少し待つ
                    time.sleep(5)
                    #さらに最大30秒間、注文が約定するのを待つ
                    for oid in self.oidArray:
                        try:
                            self.bbservice.cancel(self.pair,oid)
                            print("Log : Buy canceled! oid={0}".format(oid))
                        except:
                            time.sleep(5)
                        break
                    print("Log : Buy Wait")
                    time.sleep(5)
            else:
                #売却するBTCがすでにあるなら何もしない
                print("Log : Sufficient BTC balance")
            #BTC残高を調べる
            balance=self.bbservice.balance()
            #売却数量は,BTC残高*(1-fee)
            sell_amount=float(balance["xrp"])
            if sell_amount<self.order_min_size:
                if self.stay:
                    #部分的な約定などで最小売却単位に届かないなら買いましする
                    print("Log : Insufficient BTC balance")
                    ob=self.bbservice.orderbook(self.pair)
                    buy_price_add=float(ob["bids"][0][0])
                    oid=self.bbservice.order(self.pair,buy_price_add,10,"buy","limit")
                    self.oidArray.append(oid)      
            #print("Log : Sell order {0} x {1}".format(float(buy_price+self.profit),sell_amount))
            #self.slackService.requestOnSlack("Log : Sell order {0} x {1}".format(float(buy_price+self.profit),sell_amount))
            #利益をのせて注文　BTCの場合はpriceを整数に強制する。
            for i in range(0,5):
                time.sleep(2)
                try:
                    self.add += 0.01
                    ob=self.bbservice.orderbook(self.pair)
                    buy_price=float(ob["bids"][0][0]) + self.add
                    oid=self.bbservice.order(self.pair,buy_price+self.profit,10,"sell","limit")
                    self.oidArray.append(oid)
                except Exception as e:
                    print("exception sell limit")
                    print(e)
                    self.exceptionCnt+=1
                    if self.exceptionCnt > 5:
                        activeOrders=self.bbservice.getActiveOrders(self.pair)
                        for i in activeOrders:
                            self.bbservice.cancel(self.pair,i["order_id"])
                            print("Log : Sell canceled! oid={0}".format(oid))
                        self.exceptionCnt=0
                        time.sleep(5)
                    continue  
            #注文がサーバーで処理されるまで少し待つ
            time.sleep(10)
            #注文が成立するまで永遠に待つ
            count=0
            for i in self.bbservice.getActiveOrders(self.pair):
                print("Log : Sell Wait count")
                count+=1
                time.sleep(3)
                #15byou売れなかったら
                if (count > 5) :
                    for r in self.oidArray:
                        oid=self.bbservice.cancel(self.pair,r)
                break
