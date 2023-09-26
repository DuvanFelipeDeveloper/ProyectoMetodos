import sympy as sp

def bisection_solver(equation_str, a, b, tol=1e-4, max_iterations=100):

    x = sp.symbols('x')
    equation = sp.sympify(equation_str)
    

    f = sp.lambdify(x, equation)
    

    if f(a) * f(b) >= 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b].")
    

    iteration = 0
    
    while (b - a) / 2 > tol and iteration < max_iterations:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint  
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1
    

    return (a + b) / 2

if __name__ == "__main__":
    equation_str = input("Ingresa la ecuación en términos de 'x': ")
    a = float(input("Ingresa el valor de 'a': "))
    b = float(input("Ingresa el valor de 'b': "))
    
    try:
        result = bisection_solver(equation_str, a, b)
        print(f"La raíz aproximada es: {result:.4f}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

