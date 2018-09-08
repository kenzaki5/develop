from django.contrib import admin
from cms.models import Book, Impression
from tradeApp.models.exchange import Exchange
from tradeApp.models.bbapi import BbApi
from tradeApp.models.apitrade import ApiTrade

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目

admin.site.register(Book)

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('book',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）
    
admin.site.register(Impression)

admin.site.register(Exchange)
admin.site.register(BbApi)
admin.site.register(ApiTrade)

