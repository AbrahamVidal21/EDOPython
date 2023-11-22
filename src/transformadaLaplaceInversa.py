import sympy as sym
import numpy as np
from sympy import *
from sympy.abc import x
import matplotlib.pyplot as plt

s,x = symbols('s x')
y = symbols('y',cls=Function)
expr = (4-s*(s+2))/((s**2+4*s+4)*(s+2))
expr
Fn = inverse_laplace_transform(expr,s,x)
Fn

y = Fn

f = lambdify(x,y)

v_independiente = np.linspace(10,24,100)

solucion = f(v_independiente)
print( solucion )

plt.plot(v_independiente,solucion)