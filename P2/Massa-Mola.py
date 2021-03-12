from drawnow import drawnow,figure
import matplotlib.pyplot as plt
import numpy as np
import math

def funcao_x_linha (t,x,v):
    equacao = v
    return equacao

def funcao_v_linha (K,M,L,alpha,t,x,v):
    equacao = - (K*x)/M + (K*L)/M - (alpha*v)/M
    return equacao

def makeFig():
    x0 = 0
    dx = (x[i+1]-x0)/N
    for k in range(N):
        xk = x0 + k*dx
        plt.plot((xk,xk + 0.1), (-0.1,0.1),'k-',linewidth=1)
    plt.plot( x[i+1], 0, marker='s', markersize=23, color='blue')
    plt.xlim(-2,8)
    plt.ylim(-2,4)
    plt.plot((0,0),(-0.27,1),'k-',linewidth=4)
    plt.plot((0,8),(-0.28,-0.28),'k-',linewidth=1)
    plt.grid()
    
h = 0.01
K = 3000
M = 2
L = 3
T = 5
N = 18
alpha = 0.5

n = round(T/h)

#ARRAYS
x = np.zeros(n+1)
v = np.zeros(n+1)
t = np.zeros(n+1)

#VALORES INICIAIS
x[0] = 5
v[0] = 0
t[0] = 0

#RUNGE-KUTTA
for i in np.arange(0,n):
    k11 = funcao_x_linha(t[i],x[i],v[i])
    k21 = funcao_v_linha(K,M,L,alpha,t[i],x[i],v[i])
    
    k12 = funcao_x_linha(t[i] + h/2,x[i]*h*k11, v[i] + (h/2)*k21)
    k22 = funcao_v_linha(K,M,L,alpha,t[i] + h/2,x[i] + (h/2)*k11, v[i] + (h/2)*k21)
    
    k13 = funcao_x_linha(t[i] + h/2,x[i] + (h/2)*k12, v[i] + (h/2)*k22)
    k23 = funcao_v_linha(K,M,L,alpha,t[i] + h/2,x[i] + (h/2)*k12, v[i] + (h/2)*k22)
    
    k14 = funcao_x_linha(t[i] + h,x[i] + h*k13, v[i] + h*k23)
    k24 = funcao_v_linha(K,M,L,alpha,t[i] + h,x[i] + h*k13, v[i] + h*k23)
    
    t[i+1] = t[i] + h
    x[i+1] = x[i] + (h/6)*(k11 + (2*k12) + (2*k13) + k14)
    v[i+1] = v[i] + (h/6)*(k21 + (2*k22) + (2*k23) + k24)
    
    drawnow (makeFig)

#PLOTAR GRAFICO DA MASSA-MOLA
'''
fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(t,x)
ax2.plot(t,v)

plt.show()
'''
