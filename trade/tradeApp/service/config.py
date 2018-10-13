# coding:utf-8

class config:
    api_key='0b10d8f3-6a14-4e1e-9272-b1ba8882cc29'
    api_secret='b72b0330c910f009fa246416b8774dba1bf9e2b239665958a121a82b12aa28b3'
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
        

