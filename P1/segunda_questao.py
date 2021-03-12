'''
Grupo:

IRIS VIANA DOS SANTOS SANTANA
GABRIEL CASTRO DA SILVA GOMES
LUCAS DE FREITAS LIMA

'''

import matplotlib.pyplot as plt


def funcao1(t, x, y):
    return x - (0.1 * (x**2)) - (0.05 * x * y)


def funcao2(t, x, y):
    return (1.7 * y) - (0.1 * (y**2)) - (0.15 * x * y)


def metodo_euler(t_n, x_n, y_n, h, n, m):
    linha_t = []
    linha_x = []
    linha_y = []

    linha_t.append(t_n)
    linha_x.append(x_n)
    linha_y.append(y_n)

    while n < m:
        t_n1 = t_n + h
        x_n1 = x_n + (funcao1(t_n, x_n, y_n) * h)
        y_n1 = y_n + (funcao2(t_n, x_n, y_n) * h)

        linha_t.append(t_n1)
        linha_x.append(x_n1)
        linha_y.append(y_n1)

        t_n = t_n1
        x_n = x_n1
        y_n = y_n1
        n += h

    return linha_t, linha_x, linha_y


def metodo_runge_kutta(t_n, x_n, y_n, h, n, m):
    linha_t = []
    linha_x = []
    linha_y = []

    linha_t.append(t_n)
    linha_x.append(x_n)
    linha_y.append(y_n)

    while n < m:
        t_n1 = t_n + h

        kn1_1 = funcao1(t_n, x_n, y_n)
        kn2_1 = funcao2(t_n, x_n, y_n)

        kn1_2 = funcao1(t_n + (0.5 * h), x_n + ((0.5 * h) * kn1_1), y_n + ((0.5 * h) * kn2_1))
        kn2_2 = funcao2(t_n + (0.5 * h), x_n + ((0.5 * h) * kn1_1), y_n + ((0.5 * h) * kn2_1))

        kn1_3 = funcao1(t_n + (0.5 * h), x_n + ((0.5 * h) * kn1_2), y_n + ((0.5 * h) * kn2_2))
        kn2_3 = funcao2(t_n + (0.5 * h), x_n + ((0.5 * h) * kn1_2), y_n + ((0.5 * h) * kn2_2))

        kn1_4 = funcao1(t_n + h, x_n + (h * kn1_3), y_n + (h * kn2_3))
        kn2_4 = funcao2(t_n + h, x_n + (h * kn1_3), y_n + (h * kn2_3))

        x_n1 = x_n + ((h / 6) * (kn1_1 + (2 * kn1_2) + (2 * kn1_3) + kn1_4))
        y_n1 = y_n + ((h / 6) * (kn2_1 + (2 * kn2_2) + (2 * kn2_3) + kn2_4))

        linha_t.append(t_n1)
        linha_x.append(x_n1)
        linha_y.append(y_n1)

        
        t_n = t_n1
        x_n = x_n1
        y_n = y_n1
        n += h

    return linha_t, linha_x, linha_y


t_n = 0
x_n = 9
y_n = 4
h = 0.1
n = 0
m = 100

t_euler, x_euler, y_euler = metodo_euler(t_n, x_n, y_n, h, n, m)
t_runge_k, x_runge_k, y_runge_k = metodo_runge_kutta(t_n, x_n, y_n, h, n, m)

# Imprimindo soluções entre 0 e 100

print("\nMetodo Euler:")
for k in range(101):
    print("T_%d = %.1f | X_%d = %f | Y_%d = %f"%(k, t_euler[k], k, x_euler[k], k, y_euler[k]))

print("\nMetodo Runge Kutta:")
for k in range(101):
    print("T_%d = %.1f | X_%d = %f | Y_%d = %f"%(k, t_runge_k[k], k, x_runge_k[k], k, y_runge_k[k]))





# Adicionando as informações no gráfico.
#plt.plot(t_euler, x_euler, t_euler, y_euler, t_runge_k, x_runge_k, t_runge_k, y_runge_k)
#plt.show()
