'''
Grupo:

IRIS VIANA DOS SANTOS SANTANA
GABRIEL GOMES

'''
import matplotlib.pyplot as plt


#ENTRADAS
global C,R,h,T,V
C = 0.000001
R=2000
h = 0.1
T= 6*R*C
V=10
h=0.000001
q0=0
t0=0

def funcao_edo(q):#calcula a carga
    return ((V/R)-((1*q)/(R*C)))





# Metodo de Runge Kutta
def metodo_runge_kutta(v_n,q_n,T,C,h,t_n):
    linha_VR = []#tensao do resistor
    linha_VC = []#tensao do capacitor
    linha_Q = []#carga
    linha_VF = []#tensao da fonte
    linha_t = []#tempo
    
   
    
    v_c=q_n/C#tensao do capacitor
    v_r=v_n-v_c#tensao do resistor
   
    linha_VF.append(v_n)
    linha_VC.append(v_c)
    linha_VR.append(v_r)
    linha_Q.append(q_n)
    linha_t.append(t_n)
    
    while t_n < T:
      
        t_n1=t_n+h
        kn_1 = funcao_edo(q_n)
        kn_2 = funcao_edo(q_n+ ((0.5 * h) * kn_1))
        kn_3 = funcao_edo(q_n+ ((0.5 * h) * kn_2))
        kn_4 = funcao_edo(q_n+ (h * kn_3))
        Q_N = q_n+ ((h / 6) * (kn_1 + (2 * kn_2) + (2 * kn_3) + kn_4))
        linha_Q.append(Q_N)
        
        
        q_n=Q_N
        v_c=q_n/C
        v_r=v_n-v_c
        
         
        
        linha_VF.append(v_n)
        linha_VC.append(v_c)
        linha_VR.append(v_r)
        linha_t.append(t_n1)
        t_n+=h

    return linha_Q,linha_VF,linha_VC,linha_VR, linha_t



Q_runge_kutta, VF_runge_kutta ,VC_runge_kutta,VR_runge_kutta,T_runge_kutta= metodo_runge_kutta(V,q0,T,C,h,t0)

# Adicionando as informações no gráfico.

plt.plot(T_runge_kutta,Q_runge_kutta)
plt.show()
plt.plot(T_runge_kutta,VF_runge_kutta,T_runge_kutta,VC_runge_kutta,T_runge_kutta ,VR_runge_kutta)
plt.show()
