import sympy as sp

def trapezoidal(func, a, b, n):
 
    x = sp.symbols('x')
    func_expr = sp.sympify(func)
    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]

    integral = (h / 2) * (func_expr.subs(x, x_values[0]) + func_expr.subs(x, x_values[n]))
    for i in range(1, n):
        integral += h * func_expr.subs(x, x_values[i])

    return float(integral)

if __name__ == "__main__":

    ecuacion = input("Ingresa la función en términos de 'x': ")
    a = float(input("Ingresa el límite inferior 'a': "))
    b = float(input("Ingresa el límite superior 'b': "))
    n = int(input("Ingresa el número de subintervalos 'n': "))


    integral_aproximada = trapezoidal(ecuacion, a, b, n)
    print(f"Aproximación de la integral definida: {integral_aproximada:.6f}")

