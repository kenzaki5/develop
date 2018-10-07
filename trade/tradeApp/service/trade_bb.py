# coding:utf-8
from bbService import bbService
import time
from slack import slackService
from decimal import (Decimal, ROUND_DOWN)
from config import config

class tradeBb:
    config=config()
    API_KEY=config.getApiKey()
    API_SECRET=config.getApiSecret
    execFlg=config.getExecFlg
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

    #コンストラクタ
    def __init__(self,buyUnit,profit,orderDigit,currencyPair):
        self.order_min_size=buyUnit
        self.order_digit=orderDigit
        self.buy_unit=buyUnit
        self.profit=float(profit)
        self.pair=currencyPair
        self.CURRENCY_PAIR=currencyPair

    def tradeBb(self):
        while self.execFlg == 1:
            ob=self.bbservice.orderbook(self.pair)
            buy_price=float(ob["bids"][0][0])
            #購入数量を計算。 購入数量 = 数量*(1+fee*2) - BTC残高
            balance=self.bbservice.balance()
            print("Log : JPY {0}".format(float(balance["jpy"])))
            self.slackService.requestOnSlack("Log : JPY {0}".format(float(balance["jpy"])))
            buy_amount=round(float(self.buy_unit)*(1+0.01*self.fee_rate*2) - float(balance["btc"]),self.order_digit)
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
                print("Log : Buy order {0} x {1}".format(float(buy_price),buy_amount))
                self.slackService.requestOnSlack("Log : Buy order {0} x {1}".format(float(buy_price),buy_amount))
                try:
                    oid=self.bbservice.order(self.pair,buy_price,buy_amount,"buy","limit")
                except:
                    print("exception")
                    self.exceptionCnt+=1
                    if self.exceptionCnt > 5:
                        self.bbservice.cancel(self.pair,oid)
                        print("Log : Sell canceled! oid={0}".format(oid))
                        self.exceptionCnt=0
                        time.sleep(5)
                    continue
                print("Log : Buy oid={0}".format(oid))
                #注文がサーバーで処理されるまで少し待つ
                time.sleep(10)
                #さらに最大30秒間、注文が約定するのを待つ
                for i in range(0,10):
                    if self.bbservice.is_active_order(self.pair,oid)==False:
                        try:
                            self.bbservice.cancel(self.pair,oid)
                            print("Log : Buy canceled! oid={0}".format(oid))
                        except:
                            time.sleep(5)
                        break
                    print("Log : Buy Wait")
                    time.sleep(5)
                #注文が残っていたらキャンセルする
                if oid!=None:
                    try:
                        self.bbservice.cancel(self.pair,oid)
                        print("Log : Buy canceled! oid={0}".format(oid))
                    except:
                        time.sleep(5)
                else:
                    print("Log : Buy completed! oid={0}".format(oid))
                    self.slackService.requestOnSlack("Log : Buy completed! oid={0}".format(oid))
            else:
                #売却するBTCがすでにあるなら何もしない
                print("Log : Sufficient BTC balance")
            #BTC残高を調べる
            balance=self.bbservice.balance()
            #売却数量は,BTC残高*(1-fee)
            sell_amount=round(float(balance["btc"]),self.order_digit)
            if sell_amount<self.order_min_size:
                #部分的な約定などで最小売却単位に届かないなら買いましする
                print("Log : Insufficient BTC balance")
                oid=self.bbservice.order(self.pair,buy_price,0.001,"buy","limit")
            else:
                #注文が残っていたらキャンセルする
                if oid!=None:
                    time.sleep(5)
                    if self.bbservice.is_active_order(self.pair,oid)==True:
                        self.bbservice.cancel(self.pair,oid)
                        print("Log : Buy canceled! oid={0}".format(oid))
                        time.sleep(5)      
                print("Log : Sell order {0} x {1}".format(float(buy_price+self.profit),sell_amount))
                self.slackService.requestOnSlack("Log : Sell order {0} x {1}".format(float(buy_price+self.profit),sell_amount))
                #利益をのせて注文　BTCの場合はpriceを整数に強制する。
                try:
                    oid=self.bbservice.order(self.pair,buy_price+self.profit,float(sell_amount),"sell","limit")
                except:
                    print("exception")
                    self.exceptionCnt+=1
                    if self.exceptionCnt > 5:
                        self.bbservice.cancel(self.pair,oid)
                        print("Log : Sell canceled! oid={0}".format(oid))
                        self.exceptionCnt=0
                        time.sleep(5)
                    continue
                print("Log : Sell oid={0}".format(oid))   
                #注文がサーバーで処理されるまで少し待つ
                time.sleep(10)
                #注文が成立するまで永遠に待つ
                count=0
                while self.bbservice.is_active_order(self.pair,oid):
                    print("Log : Sell Wait count:".count + 1)
                    time.sleep(3)
                    #1分売れなかったら今の買値で売る
                    if (count > 20) :
                        ob=self.bbservice.orderbook(self.pair)
                        buy_price=float(ob["bids"][0][0])
                        oid=self.bbservice.order(self.pair,float(buy_price),sell_amount,"sell","limit")
                        #注文がサーバーで処理されるまで少し待つ
                        time.sleep(10)
                        break
                print("Log : Sell completed! oid={0}".format(oid))
                self.slackService.requestOnSlack("Log : Sell completed! oid={0}".format(oid))
                #注文がサーバーで処理されるまで少し待つ
                time.sleep(10)
