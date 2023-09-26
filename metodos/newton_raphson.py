import sympy as sp

def newton_raphson(func, x, xi, tol=1e-6, max_iter=100):
    

    x = sp.symbols(x)
    func_expr = sp.sympify(func)


    func_prime = sp.diff(func_expr, x)


    x0 = xi
 
    for _ in range(max_iter):
        x1 = x0 - func_expr.subs(x, x0) / func_prime.subs(x, x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

    raise ValueError("El método de Newton-Raphson no convergió.")


if __name__ == "__main__":
    ecuacion = "x**3+3*x**2+12*x+8"  
    x0_aproximado = newton_raphson(ecuacion, 'x',-1)
    print(f"Aproximación de la raíz: {x0_aproximado:.6f}")
