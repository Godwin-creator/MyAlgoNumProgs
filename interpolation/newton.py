#Interpolation polynomiale par la méthode de Newton (différences divisées).

from .utils import verifier_points

def newton(xi, yi):

    n = verifier_points(xi, yi)

    dd = [[0.0] * n for _ in range(n)]
    for i in range(n):
        dd[i][i] = yi[i]

    for k in range(1, n):
        for i in range(n - k):
            dd[i][i+k] = (dd[i+1][i+k] - dd[i][i+k-1]) / (xi[i+k] - xi[i])

    coeffs = [dd[0][i] for i in range(n)]

    def p(x):
        res = coeffs[n-1]
        for k in range(n-2, -1, -1):
            res = res * (x - xi[k]) + coeffs[k]
        return res
    return p