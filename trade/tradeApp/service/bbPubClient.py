# coding:utf-8
import python_bitbankcc
import json
import os, json
import python_bitbankcc

class bbPubClient:
# public API classのオブジェクトを取得
    pub = python_bitbankcc.public()

# PUBLIC
    def getTicker(self, pair: str):
        value = self.pub.get_ticker(pair)
        return value

    def getDepth(self, pair):
        value = self.pub.get_depth(pair)
        return value

    def getTransactions(self, pair):
        value = self.pub.get_transactions(pair)
        return value

    # 同じメソッドを日にち指定で
    def getTransactionsWithDay(self, pair, day):
        value = self.pub.get_transactions(pair, day)
        return value

    def getCandlestick(self, pair, type, day):
        value = self.pub.get_candlestick(pair, type, day)
        return value