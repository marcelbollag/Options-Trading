import definitions
import unittest



t = definitions.option(-4, 'put', 25, 5.23)
u = definitions.option(2, 'put', 25, 2.13)
v = definitions.option(-6, 'call', 25, 11.10)
w = definitions.option(3, 'call', 25, 1.16)
x = definitions.option(4, 'put', 25, 2.14)
y = definitions.option(-3, 'call', 30, 1.10)
z = definitions.stock(27.00, 201)

print('put test:', )
