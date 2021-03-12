from drawnow import drawnow,figure
import matplotlib.pyplot as plt
import numpy as np
import math

def funcao_1 (t,theta,w):
    equacao = w
    return equacao

def funcao_2 (t,theta,w):
    equacao = -(G/L)*(math.sin(theta)) - alpha*w
    return equacao

def makeFig():    
    plt.plot((0, x), (0,y),'b-',linewidth=1,color='black')
    plt.plot(x,y,marker='o',markersize=25,color='blue')
    plt.plot(0,0,marker='o',markersize=5,color='black')
    plt.xlim(-borda,borda)
    plt.ylim(-borda,borda)
    plt.axes().set_aspect('equal')
    plt.grid()

theta_graus = 60
theta_inicial = theta_graus*(math.pi/180)
G = 9.8
L = 0.15  
h = 0.05
T = 6
N = 18
alpha = 0.5
borda = L + (0.2*L)

n = round(T/h)

#ARRAYS
theta = np.zeros(n+1)
w = np.zeros(n+1)
t = np.zeros(n+1)

#VALORES INICIAIS
theta[0] = theta_inicial
w[0] = 0
t[0] = 0

#RUNGE-KUTTA
for i in np.arange(0,n):
    k11 = funcao_1(t[i],theta[i],w[i])
    k21 = funcao_2(t[i],theta[i],w[i])
    
    k12 = funcao_1(t[i] + h/2,theta[i]*h*k11, w[i] + (h/2)*k21)
    k22 = funcao_2(t[i] + h/2,theta[i] + (h/2)*k11, w[i] + (h/2)*k21)
    
    k13 = funcao_1(t[i] + h/2,theta[i] + (h/2)*k12, w[i] + (h/2)*k22)
    k23 = funcao_2(t[i] + h/2,theta[i] + (h/2)*k12, w[i] + (h/2)*k22)
    
    k14 = funcao_1(t[i] + h,theta[i] + h*k13, w[i] + h*k23)
    k24 = funcao_2(t[i] + h,theta[i] + h*k13, w[i] + h*k23)
    
    t[i+1] = t[i] + h
    theta[i+1] = theta[i] + (h/6)*(k11 + (2*k12) + (2*k13) + k14)
    w[i+1] = w[i] + (h/6)*(k21 + (2*k22) + (2*k23) + k24)
    
    x = L*math.cos(theta[i+1] - (math.pi/2))
    y = L*math.sin(theta[i+1] - (math.pi/2))

    drawnow(makeFig)

#PLOTAR GRAFICO DO PENDULO
'''
fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(t,theta)
ax2.plot(t,w)

plt.show()
'''

