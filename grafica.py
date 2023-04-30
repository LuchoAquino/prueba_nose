import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(0, 5, 0.1)
y = lambda x:(
    5*((0<=x)&(x<=1))+
    2*((1<x)&(x<=2.5))+
    0*((2.5<x)&(x<=5))
)

#ejex = 0*x

plt.title('Funcion Github')
plt.ylabel('V0- Hice cambio desde otra pc q no es la miaa')
plt.xlabel('V1- No me gusta q lo hagas desde github hazlo desde la terminal')
plt.xlim(0, 5)
plt.plot(x, y(x), 'blue')
#plt.plot(x, ejex, 'black')
plt.show()
