from django.db import models

class Exchange(models.Model):
    """取引所"""
    exchange_code = models.IntegerField('取引所コード', blank=False)
    name = models.CharField('取引所名', max_length=255)
    status = models.BooleanField('ステータス', blank=False)
    def __str__(self):
        return self.name

