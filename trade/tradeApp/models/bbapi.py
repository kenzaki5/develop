from django.db import models
from tradeApp.models.exchange import Exchange

class BbApi(models.Model):
    """BbAPI設定"""
    exchange_id = models.ForeignKey(Exchange, verbose_name='取引所', related_name='BbApiConfig', on_delete=models.CASCADE)
    api_key = models.CharField('APIキー', max_length=255)
    api_secret = models.CharField('APIシークレット', max_length=255)
    api_url = models.CharField('APIURL', blank=True, max_length=255)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

