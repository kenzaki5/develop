# coding:utf-8
import python_bitbankcc
import json
import os, json
import python_bitbankcc

class bbPrvClient:

    prv = ""

    def __init__(self, key, secret):
        self.prv = python_bitbankcc.private(key, secret)
        return

    # PRIVATE TEST
    def getAsset(self):
        value = self.prv.get_asset()
        return value

    def getOrder(self, pair, orderId):
        value = self.prv.get_order(pair, orderId)
        return value

    def getActiveOrders(self, pair):
        value = self.prv.get_active_orders(pair)
        return value

    def order(self, pair, price, orderUnit, orderSide, orderType):
        value = self.prv.order(pair, price, orderUnit, orderSide, orderType)
        return value

    def cancelOrder(self, pair, orderId):
        value = self.prv.cancel_order(pair, orderId)
        return value

    def cancelOrders(self, pair, orderIds):
        value = self.prv.cancel_orders(pair, orderIds)
        return value

    def getOrdersInfo(self, pair, orderIds):
        value = self.prv.get_orders_info(pair, orderIds)
        return value

    def getTradeHistory(self, pair, tradeNum):
        value = self.prv.get_trade_history(pair, tradeNum)
        return value

    def getWithdrawAccount(self, assetType):
        value = self.prv.get_withdraw_account(assetType)
        return value

    def requestWithdraw(self, assetType, withDrawUuid, withDrawNum, otpToken, smsToken):
        value = self.prv.request_withdraw(assetType, withDrawUuid, withDrawNum, { # 有効になっていた場合に必須
                'otp_token': otpToken,
                'sms_token': smsToken
            }
        )
        return value