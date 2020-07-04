from flask import Flask
import sympy as sp

# om even te testen:
sp.init_printing()

x = sp.symbols('x')
I = sp.Integral(sp.exp(-x**2/2), (x, -sp.oo, sp.oo))
print(I, I.doit())
# met pretty printing
sp.pprint(I)
sp.pprint(I.doit()) # zou sqrt(2*pi) moeten geven