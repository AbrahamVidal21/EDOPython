## Librerías
import numpy as np

import matplotlib.pyplot as plt

import matplotlib as mpl

from matplotlib.font_manager import FontProperties

from sympy import symbols, Function, dsolve

from sympy.abc import t

from sympy import *


## Declaración de variables
s,x,= symbols('s x')   

# Declaración de símbolos
y = Function('y')(x)

## Declaración de la expresión
expr = y.diff(x,2) + 4*y.diff(x,1) + 4*y -4*exp(-2*x)
expr
print( expr )

solucion = dsolve(expr, y, ics={y.diff(x).subs(x, 0): 4,y.subs(x, 0): -1})
solucion

y = solucion


f = lambdify(x,y.rhs)

gra = np.linspace(0,10,100)

grafica= f(gra)

# Configuracion de output table
plt.plot(gra,grafica,'-',color='deepskyblue',lw = 1.5,label='Solución')
plt.legend(frameon=True,fontsize=14,loc=0,ncol=1)
plt.yticks(fontsize=16)
plt.xlabel("tiempo [s]",fontsize = 18, color = 'black')
plt.ylabel("y [m]",fontsize = 18, color = 'black')
titulog = 'Solución_EDO.png'
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--',linewidth = 1)
plt.xticks(fontsize=16,rotation=0,fontweight='bold')
plt.yticks(fontweight='bold')
plt.savefig(titulog, dpi = 600)
plt.show()