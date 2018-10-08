# coding:utf-8

class config:
    api_key=''
    api_secret=''
    exec_flg='1'
    count='5'

    def getApiKey(self):
        return self.api_key

    def getApiSecret(self):
        return self.api_secret

    def getExecFlg(self):
        return self.exec_flg

    def getCount(self):
        return self.count

    def setExecFlg(self,execFlg):
        self.exec_flg = execFlg
        

