#2D wave equation
# Tomado del blog "The Beginner Programmer".

import numpy as np
from scipy.special import jn, jn_zeros
from numpy import pi,sin,cos,sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.gca(projection='3d')

x = np.linspace(0,1,30)
y = np.linspace(0,1,30)

X,Y = np.meshgrid(x,y)

#Rapidez de la onda
c = 1

#Tiempo inicial
t0 = 0

#Incremento temporal
dt = 0.03

#Combinaciones para los modos
p = 4
q = 1

#Frecuencia
w = pi*c*sqrt(p**2+q**2)

#Desplazamiento de la onda
def u(x,y,t):
    return (cos(w*t)+sin(w*t))*sin(pi*p*x)*sin(q*pi*y)

#Evaluación de la función
a = []
for i in range(500):
    z = u(X,Y,t0)
    t0 = t0 + dt
    a.append(z)

#Colorbar 
m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
m.set_array(a[0])
cbar = plt.colorbar(m)

k = 0
def animate(i):
    global k
    Z = a[k]
    k += 1
    ax1.clear()
    ax1.plot_surface(X,Y,Z,rstride=1, cstride=1,cmap=plt.cm.jet,linewidth=0,antialiased=False)
    #ax1.contour(X,Y,Z)
    ax1.set_zlim(0,5)
    
anim = animation.FuncAnimation(fig,animate,frames=220,interval=20)
plt.show()
