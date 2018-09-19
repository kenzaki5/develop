# coding:utf-8
import configparser
from bbService import bbService
from time import sleep
from tradeStop import tradeStop
from subprocess import getoutput
import subprocess
from statistics import mean, median,variance,stdev

class watcher:
    config = configparser.ConfigParser()
    config.read('trade/tradeApp/service/config.ini', 'UTF-8')
    API_KEY=config['conf']['api_key']
    API_SECRET=config['conf']['api_secret']
    count=int(config['conf']['count'])
    CURRENCY_PAIR="btc_jpy"
    sellMean=[]
    buyMean=[]
    highMean=[]
    lowMean=[]
    lastMean=[]
    sellList=[]
    buyList=[]
    highList=[]
    lowList=[]
    lastList=[]

    bbservice=bbService(API_KEY,API_SECRET,CURRENCY_PAIR)
    tradeStop=tradeStop()

    def watch(self):
        for num in range(((int(self.count) * 3))//int(self.count)):
            for num in range(int(self.count)):
                ticker=self.getTicker()
                self.sellList.append(int(ticker['sell']))
                self.buyList.append(int(ticker['buy']))
                self.highList.append(int(ticker['high']))
                self.lowList.append(int(ticker['low']))
                self.lastList.append(int(ticker['last']))
                
            self.sellMean.append(mean(self.sellList))
            self.buyMean.append(mean(self.buyList))
            self.highMean.append(mean(self.highList))
            self.lowMean.append(mean(self.lowList))
            self.lastMean.append(mean(self.lastList))

        over0=self.sellMean[0] > self.buyMean[0]
        print(over0)
        over1=self.sellMean[1] > self.buyMean[1]
        print(over1)
        over2=self.sellMean[2] > self.buyMean[2]
        print(over2)
        golden=(self.getTake(over0,over1,over2) == True)
        dead=(self.getTake(over0,over1,over2) == False)
        print("golden {0}".format(golden))
        print("dead {0}".format(dead))

        if golden:
            print("golden")
            result = subprocess.check_output("ps ax | grep python trade.py | grep -v grep")
            if result!='python trade.py':
                return True
        elif dead:
            print("dead")
            return False

        sleep(self.count)
        print("finish {0}".format(self.count))

    def getTicker(self):
        ticker=self.bbservice.getTicker(self.CURRENCY_PAIR)
        sleep(2)
        return ticker
    
    def getTake(self,a,b,c):
        return (not(a) and b and c) or (a and not(b) and c) or (a and b and not(c)) or (a and b and c)

    def calculate_mean(self,data):
        s = sum(data)
        N = len(data)
        mean =s/N

        return mean

    #平均からの偏差を求める
    def find_difference(self,data):
        mean = self.calculate_mean(data)
        diff = []

        for num in data:
            diff.append(num-mean)
        return diff

    def calculate_variance(self,data):
        diff = self.find_difference(data)
        #差の２乗を求める
        squared_diff = []
        for d in diff:
            squared_diff.append(d**2)

        #分散を求める
        sum_squared_diff = sum(squared_diff)
        variance = sum_squared_diff/len(data)
        return variance






