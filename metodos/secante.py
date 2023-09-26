import sympy as sp

def secante(func, x0, x1, tol=1e-6, max_iter=100):
  

    x = sp.symbols('x')
    func_expr = sp.sympify(func)

    for i in range(max_iter):

        f_x0 = func_expr.subs(x, x0)
        f_x1 = func_expr.subs(x, x1)


        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x_next - x1) < tol:
            return x_next

        x0, x1 = x1, x_next

    raise ValueError("El método de la secante no convergió.")

if __name__ == "__main__":

    ecuacion = input("Ingresa la ecuación en términos de 'x': ")
    x0 = float(input("Ingresa el primer valor inicial x0: "))
    x1 = float(input("Ingresa el segundo valor inicial x1: "))


    try:
        raiz_aproximada = secante(ecuacion, x0, x1)
        print(f"Aproximación de la raíz: {raiz_aproximada:.6f}")
    except ValueError as e:
        print(e)
