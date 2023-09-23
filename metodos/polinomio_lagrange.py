import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def polinomio_lagrange(valores_x, valores_y):
    n = len(valores_x)
    x = sp.Symbol('x')
    polinomio_lagrange = 0

    for i in range(n):
        base = 1
        for j in range(n):
            if j != i:
                base *= (x - valores_x[j]) / (valores_x[i] - valores_x[j])
        polinomio_lagrange += valores_y[i] * base

    return polinomio_lagrange

def simplificar_polinomio(polinomio):
    return sp.simplify(polinomio)

def graficar_polinomio(valores_x, valores_y):
    polinomio = polinomio_lagrange(valores_x, valores_y)
    polinomio_simplificado = simplificar_polinomio(polinomio)
    print(polinomio_simplificado)
    return polinomio_simplificado


    # x = sp.Symbol('x')
    # expr = sp.lambdify(x, polinomio_simplificado, 'numpy')
    # print(expr)
    # valores_x_rango = np.linspace(min(valores_x), max(valores_x), 1000)
    # valores_y_inter = expr(valores_x_rango)

    # plt.figure()
    # plt.plot(valores_x, valores_y, 'ro', label='Puntos')
    # plt.plot(valores_x_rango, valores_y_inter, 'b-', label='Polinomio P')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Polinomio de Lagrange ')
    # plt.legend()
    # plt.grid()
    # plt.show()

valores_x = [0.50,0.33,0.25,4,2,6]
valores_y = [-4,-2,-6,3,6,2]
graficar_polinomio(valores_x, valores_y)