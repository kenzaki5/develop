from django.db import models
from tradeApp.models.exchange import Exchange

class ApiTrade(models.Model):
    """API売買設定"""
    exchange_id = models.ForeignKey(Exchange, verbose_name='取引所', related_name='ApiTradeConfig', on_delete=models.CASCADE)
    order_min_size = models.FloatField('数量最小値', blank=True)
    order_digit = models.IntegerField('数量の桁数', blank=True)
    fee_rate = models.IntegerField('取引手数料のレート(%)', blank=True)
    buy_unit = models.IntegerField('購入単位', blank=True)
    profit = models.FloatField('価格差', blank=True)