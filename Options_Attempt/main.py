import definitions
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import inspect


x = definitions.option(2, 'call', 30, .30)
y = definitions.stock(27.79, 201)
z = definitions.option(-2, 'call', 25, 2.95)


# print(x.value(28.68))
#print(y.startval)

# print(z.value(28.68))
# print(xx.value(28.68))
# print(x.value(28.68)+y.value(28.68)+z.value(28.68)+xx.value(28.68))

porto = definitions.portfolio([x, y, z])
#print (z.change(20))
#print (norm.expect(porto.value, loc = 27, lb=0))
#portfolio.portplot(np.arange(25, 32, .1))

print("from just the stock:", y.value(27.79))
porto.expected(loc=27.79, sd=1, plot=True)




#definitions.plotter(portfolio, [80, 90, 100, 200, 300])



#tester = np.arange(-5, 5, .01)
#vals = norm.pdf(tester)

#plt.plot(tester, vals)
#plt.show()
