__author__ = 'stKy1219Lo7351'

import random

class Symbols():
    def __init__(self):
            self._symbol = 0
            self._symbollist = []
            self._combolist = ""

    def getSymbol(self):
        for index in range(3):
            KappaRoss = random.randint(0,199)
            if KappaRoss < 101:
                    self._symbol = "7"

            elif KappaRoss >= 101 and KappaRoss < 152:
                    self._symbol = "9"

            elif KappaRoss >= 152 and KappaRoss < 178:
                    self._symbol = "J"

            elif KappaRoss >= 178 and KappaRoss < 192:
                    self._symbol = "Q"

            else:
                    self._symbol = "K"

            self._symbollist.append(self._symbol)
        self._combolist = "".join(self._symbollist)

    def __str__(self):
        return self._combolist

class balance():
    def __init__(self):
        self._balance = 100

    def Changedbalance(self, amount):
        self._balance = amount

    def setBalance(self,amount):
        self._balance += amount


    def __str__(self):
        return str(self._balance)
