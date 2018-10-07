# coding:utf-8

class config:
    api_key='5962ac20-5ad9-472f-a469-37e1b9391b79'
    api_secret='b4f9f6f96ec0722bba47c22bcb2476e0246ef32de14bac32c72fba795427be14'
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
