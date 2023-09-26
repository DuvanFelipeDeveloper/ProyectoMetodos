import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x0 = np.array(x0, dtype=float)
    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

        if np.linalg.norm(x - x0) < tol:
            return x

        x0 = x.copy()

    raise ValueError("El método de Gauss-Seidel no convergió después de {} iteraciones.".format(max_iter))

if __name__ == "__main__":
   
    A = [[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 4]]
    b = [1, 1, 1, 1]
    x0 = [0, 0, 0, 0]

    try:
        solucion_aproximada = gauss_seidel(A, b, x0)
        print("Solución aproximada:", solucion_aproximada)
    except ValueError as e:
        print(e)
