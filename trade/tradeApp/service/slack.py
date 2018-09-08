import requests, json

class slackService:
    WEB_HOOK_URL = "https://hooks.slack.com/services/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"
    def requestOnSlack(self,message) :
        requests.post(self.WEB_HOOK_URL, data = json.dumps({
            'text': message,  #通知内容
            'username': u'trade-python-log',  #ユーザー名
            'icon_emoji': u':smile_cat:',  #アイコン
            'link_names': 1,  #名前をリンク化
        }))