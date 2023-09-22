import math
import numpy as np
import matplotlib.pyplot as plt


def metodo_trapezoidal(funcion, a, b, n):
    
    h = (b - a) / n
    integral = 0.5 * (funcion(a) + funcion(b))

    for i in range(1, n):
        
        x_i = a + i * h
        integral += funcion(x_i)

    integral *= h
    return integral




# función e^(x^4)
def funcion(x):
    return math.exp(x**4)


# intervalo y número de puntos 
a = -1
b = 1
n = 1000


# valores de x en el intervalo
x_values = np.linspace(a, b, n)

# valores de y para la función
y_values = [funcion(x) for x in x_values]

# aplicando el método trapezoidal
resultado = metodo_trapezoidal(funcion, a, b, n)
print(f"Aproximación de la integral definida: {resultado}")
