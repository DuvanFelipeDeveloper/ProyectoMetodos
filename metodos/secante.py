import sympy as sp

def secante(func, x0, x1, tol=1e-6, max_iter=100):
  
    # Convertimos la cadena de función a una expresión simbólica.
    x = sp.symbols('x')
    func_expr = sp.sympify(func)

    for i in range(max_iter):
        # Calculamos el valor de la función en los puntos actuales.
        f_x0 = func_expr.subs(x, x0)
        f_x1 = func_expr.subs(x, x1)

        # Calculamos el siguiente punto de aproximación.
        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x_next - x1) < tol:
            return x_next

        x0, x1 = x1, x_next

    raise ValueError("El método de la secante no convergió.")

if __name__ == "__main__":
    # Solicitar la función y los valores iniciales al usuario.
    ecuacion = input("Ingresa la ecuación en términos de 'x': ")
    x0 = float(input("Ingresa el primer valor inicial x0: "))
    x1 = float(input("Ingresa el segundo valor inicial x1: "))

    # Llama a la función secante con los valores proporcionados.
    try:
        raiz_aproximada = secante(ecuacion, x0, x1)
        print(f"Aproximación de la raíz: {raiz_aproximada:.6f}")
    except ValueError as e:
        print(e)
