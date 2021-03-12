'''
Grupo:

IRIS VIANA DOS SANTOS SANTANA
GABRIEL CASTRO DA SILVA GOMES
LUCAS DE FREITAS LIMA

'''
import matplotlib as plt


# EDO
def funcao_edo(x, y):
    return (-y)**3


# Funcao exata
def funcao_exata(x):
    return 1/((2 * x) + 1)**0.5


# Metodo exato
def metodo_exato(x_n, y_n, h, n, m):
    linha_x = []
    linha_y = []
    linha_x.append(x_n)
    linha_y.append(y_n)

    while n < m:
        x_n1 = x_n + h
        y_n1 = funcao_exata(x_n1)

        linha_x.append(x_n1)
        linha_y.append(y_n1)

        x_n = x_n1
        n += h

    return linha_x, linha_y


# Metodo de euler
def metodo_euler(x_n, y_n, h, n, m):
    linha_x = []
    linha_y = []
    linha_x.append(x_n)
    linha_y.append(y_n)

    while n < m:
        x_n1 = x_n + h
        y_n1 = y_n + (funcao_edo(x_n, y_n) * h)

        linha_x.append(x_n1)
        linha_y.append(y_n1)
        x_n = x_n1
        y_n = y_n1
        n += h

    return linha_x, linha_y


# Metodo de Runge Kutta
def metodo_runge_kutta(x_n, y_n, h, n, m):
    linha_x = []
    linha_y = []
    linha_x.append(x_n)
    linha_y.append(y_n)

    while n < m:
        x_n1 = x_n + h
        kn_1 = funcao_edo(x_n, y_n)
        kn_2 = funcao_edo(x_n + (0.5 * h), y_n + ((0.5 * h) * kn_1))
        kn_3 = funcao_edo(x_n + (0.5 * h), y_n + ((0.5 * h) * kn_2))
        kn_4 = funcao_edo(x_n + h, y_n + (h * kn_3))
        y_n1 = y_n + ((h / 6) * (kn_1 + (2 * kn_2) + (2 * kn_3) + kn_4))

        linha_x.append(x_n1)
        linha_y.append(y_n1)
        x_n = x_n1
        y_n = y_n1
        n += h

    return linha_x, linha_y


# Entradas dadas na questao, onde x0 = x_n, y0 = y_n, n e m = intervalo
x_n = 0
y_n = 1
h = 0.1
n = 0
m = 5

# Armazenando os valores obtidos em cada metodo.
x_exato, y_exato = metodo_exato(x_n, y_n, h, n, m)
x_euler, y_euler = metodo_euler(x_n, y_n, h, n, m)
x_runge_kutta, y_runge_kutta = metodo_runge_kutta(x_n, y_n, h, n, m)

# Imprimindo soluções entre 0 e 5
print("Metodo Exato:")
for k in range(6):
    print("X_%d = %.1f | Y_%d = %f" % (k, x_exato[k], k,  y_exato[k]))

print("\nMetodo Euler:")
for k in range(6):
    print("X_%d = %.1f | Y_%d = %f"%(k, x_euler[k], k, y_euler[k]))

print("\nMetodo Runge Kutta:")
for k in range(6):
    print("X_%d = %.1f | Y_%d = %f"%(k, x_runge_kutta[k], k, y_runge_kutta[k]))

# Adicionando as informações no gráfico.
plt.plot(x_exato, y_exato, x_euler, y_euler, x_runge_kutta, y_runge_kutta)
plt.show()
