import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Función para ingresar la ecuación
def ingresar_ecuacion():
    ecuacion_texto = input("Ingrese la ecuación en términos de 'x': ")
    x = sp.symbols('x')
    ecuacion = sp.sympify(ecuacion_texto)
    return ecuacion, x

# Función para encontrar despejes
def encontrar_despejes(ecuacion, x):
    despejes = sp.solve(ecuacion, x)
    return despejes

# Función para encontrar una aproximación inicial
def encontrar_aprox_inicial(ecuacion, x, valor_inicial=0):
    if valor_inicial != 0:
        return valor_inicial
    else:
        iteraciones = 100
        x_valores = np.linspace(-10, 10, iteraciones)
        y_valores = [ecuacion.subs(x, val).evalf() for val in x_valores]
        valor_inicial = x_valores[np.argmin(np.abs(y_valores))]
        return valor_inicial

# Función para aplicar el método de punto fijo a una ecuación
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
            print(f"Raíz aproximada: {x_actual} (convergió en {i} iteraciones)")
            break
    else:
        print(f"El método de punto fijo no converge después de {max_iter} iteraciones.")



if __name__ == "__main__":
    ecuacion, x = ingresar_ecuacion()
    despejes = encontrar_despejes(ecuacion, x)
    
    for despeje in despejes:
        valor_inicial = encontrar_aprox_inicial(despeje, x)
        print(f"Despeje: {despeje}")
        punto_fijo(despeje, x, valor_inicial)

