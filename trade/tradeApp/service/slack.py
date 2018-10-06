# coding:utf-8
import requests, json

class slackService:
    WEB_HOOK_URL = "https://hooks.slack.com/services/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"
    def requestOnSlack(self,message) :
        requests.post(self.WEB_HOOK_URL, data = json.dumps({
            'text': message,  #通知内容
            'username': u'trade-log',  #ユーザー名
            'icon_emoji': u':smile_cat:',  #アイコン
            'link_names': 1,  #名前をリンク化
        }))