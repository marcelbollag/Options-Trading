import numpy
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


class option:
    def __init__(self, quant:int, type:str, strike:float, premium:float, expiration=0):
        self.type = type
        self.strike = strike
        self.premium = premium
        self.quant = quant
        self.expiration = expiration
        #this could be improved by putting quant in negative for sells:
        self.startval = -self.value(strike)

    #can add expiration to change to make it worthless once date format decided
    def value(self, price):
        if (self.quant == 0):
            return (0)
        if (self.quant > 0):
            if (self.type == 'call'):
                if (price > self.strike):
                    return (self.quant * 100 * (price - self.strike - self.premium))
                else:
                    return (self.quant * 100 * -self.premium)
            if (self.type == 'put'):
                if (price < self.strike):
                    return (self.quant * 100 * (self.strike - price - self.premium))
                else:
                    return (self.quant * 100 * -self.premium)
        if (self.quant < 0):
            if (self.type == 'call'):
                if (price > self.strike):
                    return (self.quant * 100 * (price - self.strike - self.premium))
                else:
                    return (self.quant * 100 * -self.premium)
            if (self.type == 'put'):
                if (price < self.strike):
                    return (self.quant * 100 * (self.strike - price - self.premium))
                else:
                    return (self.quant * 100 * -self.premium)
    def change(self, price):
        return(self.value(price)-self.startval)

class stock:
    def __init__(self, premium, quant):
        self.premium = premium
        self.quant = quant
        self.startval = premium * quant
    def change(self, price):
        return(self.quant * (price - self.premium))
    def value(self, price):
        return(self.startval + self.change(price))

class portfolio:
    def __init__(self, port):
        self.port = port
        self.startval = 0
        #this will break percentchange if there are no stocks in port
        for i in self.port:
            if type(i) == stock:
                self.startval = self.startval + i.startval

    def change(self, price):
        change = 0
        for i in self.port:
            change = change + i.change(price)
        return (change)

    def value(self, price):
        value = 0
        for i in self.port:
            value = value + i.value(price)
        return(value)

    def percentchange(self, price):
        #return(self.change(price)/self.startval)
        #this will break when there are no stocks in the portfolio
        return(self.value(price)/self.startval - 1)

    #percentchange = new value/original value - 1

    def portplot(self, rng):
        x = rng
        y = []
        for i in rng:
            y.append(self.value(i))
        print(x)
        print(y)
        plt.plot(x, y)
        plt.show()

    def expected(self, loc=0, sd=1, plot=False):
        #****plugging in change vs percent change not matching up for exp, look for error****
        exp = norm.expect(self.value, loc=loc, lb=0, scale=sd)
        print (exp)

        if (plot):
            plb = max(loc - 12 * sd, 0)
            pub = loc + 12 * sd
            dx = (pub-plb)/100
            x = np.arange(plb, pub, dx)
            #print (x)
            y1 = norm.pdf(x, loc=loc)
            y2 = []
            y3 = []
            for i in x:
                #print (i)
                y2.append(self.change(i))
            for i in x:
                y3.append(self.value(i))
            plt.subplot(311)
            plt.plot(x, norm.pdf(x, loc))
            plt.subplot(312)
            plt.plot(x, y2)
            plt.subplot(313)
            plt.plot(x, y3)
            plt.show()
        return (exp)

def plotter(portf, rng):
    x = rng
    y = []
    for price in x:
        value = 0
        for security in portf:
            value = value + security.change(price)
        y.append(value)
    plt.plot(x, y)
    plt.show()
