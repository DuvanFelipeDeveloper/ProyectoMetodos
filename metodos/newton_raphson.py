import sympy as sp

def newton_raphson(func, x, xi, tol=1e-6, max_iter=100):
    
    # Convertimos la cadena de función a una expresión simbólica.
    x = sp.symbols(x)
    func_expr = sp.sympify(func)

    # Derivamos la función.
    func_prime = sp.diff(func_expr, x)

    # Búsqueda incremental para encontrar un valor inicial x0.
    x0 = xi
    # while abs(func_expr.subs(x, x0)) > tol and max_iter > 0:
    #     x0 += 0.1  # Ajusta el paso de búsqueda según tus necesidades.
    #     max_iter -= 1

    # if max_iter == 0:
    #     raise ValueError("No se pudo encontrar un valor inicial adecuado.")

    # Aplicamos el método de Newton-Raphson.
    for _ in range(max_iter):
        x1 = x0 - func_expr.subs(x, x0) / func_prime.subs(x, x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

    raise ValueError("El método de Newton-Raphson no convergió.")

# Ejemplo de uso:
if __name__ == "__main__":
    ecuacion = "x**3+3*x**2+12*x+8"  # Cambia esta ecuación según tus necesidades.
    x0_aproximado = newton_raphson(ecuacion, 'x',-5)
    print(f"Aproximación de la raíz: {x0_aproximado:.6f}")
