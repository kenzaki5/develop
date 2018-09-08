# coding:utf-8
import hashlib
import hmac
import requests
import urllib.parse
import datetime
import random
from bbPubClient import bbPubClient
from bbPrvClient import bbPrvClient

class bbService:
    CURRENCY_PAIR=""
    API_KEY=""
    API_SECRET=""
    bbPubClient="" 
    bbPrvClient=""
    #コンストラクタ
    def __init__(self,key,secret,currency_pair):
        self.API_KEY = key
        self.API_SECRET = secret
        self.CURRENCY_PAIR = currency_pair
        self.bbPubClient = bbPubClient()
        self.bbPrvClient = bbPrvClient(key,secret)
        return
    def balance(self):
        asset=self.bbPrvClient.getAsset()
        assets=asset["assets"]
        return {"btc":str(assets[1]['onhand_amount']),"jpy":str(assets[0]['onhand_amount']),"xrp":str(assets[3]['onhand_amount'])}
    #注文板情報を得る
    def orderbook(self,pair):
        depth=self.bbPubClient.getDepth(pair)
        return {"asks":[tuple(i) for i in depth["asks"]],"bids":[tuple(i) for i in depth["bids"]]}
    # 買い売り注文を出す
    def order(self, pair, price, orderUnit, orderSide, orderType):
        order=self.bbPrvClient.order(pair, price, orderUnit, orderSide, orderType)
        return order["order_id"]
    #注文をキャンセルする
    def cancel(self,pair,oid):
        return self.bbPrvClient.cancelOrder(pair, oid)
    #注文が有効かを返す
    def is_active_order(self,pair,oid):
        activeOrders=self.bbPrvClient.getActiveOrders(pair)
        return str(oid) in activeOrders["orders"] 
        

