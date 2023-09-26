import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x0 = np.array(x0, dtype=float)
    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_new = np.zeros(n)

        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new

    raise ValueError("El método de Jacobi no convergió después de {} iteraciones.".format(max_iter))

if __name__ == "__main__":
.
    A = [[4, -1, 0,0], [-1, 4, -1,0], [0, -1, 4,-1],[0, 0, -1,4]]
    b = [1, 1, 1,1]
    x0 = [0, 0, 0,0]

    try:
        solucion_aproximada = jacobi(A, b, x0)
        print("Solución aproximada:", solucion_aproximada)
    except ValueError as e:
        print(e)
