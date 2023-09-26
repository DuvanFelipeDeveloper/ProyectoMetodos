import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def ingresar_ecuacion(inputecuacion):
    ecuacion_texto = inputecuacion
    x = sp.symbols('x')
    ecuacion = sp.sympify(ecuacion_texto)
    return ecuacion, x


def encontrar_despejes(ecuacion, x):
    despejes = sp.solve(ecuacion, x)
    return despejes


def encontrar_aprox_inicial(ecuacion, x, valor_inicial=0):
    if valor_inicial != 0:
        return valor_inicial
    else:
        iteraciones = 100
        x_valores = np.linspace(-10, 10, iteraciones)
        y_valores = [ecuacion.subs(x, val).evalf() for val in x_valores]
        valor_inicial = x_valores[np.argmin(np.abs(y_valores))]
        return valor_inicial


def punto_fijo(ecuacion, x, valor_inicial, max_iter=100, tolerancia=1e-4):
    iteraciones = [0]
    aproximaciones = [valor_inicial]
    errores = []
    x_actual = valor_inicial

    for i in range(1, max_iter + 1):
        x_anterior = x_actual
        x_actual = ecuacion.subs(x, x_anterior).evalf()
        error_actual = abs((x_actual - x_anterior) / x_actual) * 100

        iteraciones.append(i)
        aproximaciones.append(x_actual)
        errores.append(error_actual)

        if error_actual < tolerancia:
            return x_actual
            break
    else:
        print(f"El método de punto fijo no converge después de {max_iter} iteraciones.")



def punto_fijo_inicio(imputecuacion):
    ecuacion, x = ingresar_ecuacion(imputecuacion)
    despejes = encontrar_despejes(ecuacion, x)
    
    raizes = []
    for despeje in despejes:
        valor_inicial = encontrar_aprox_inicial(despeje, x)
        print(f"Despeje: {despeje}")
        raizes.append( str(punto_fijo(despeje, x, valor_inicial)))
    return raizes

