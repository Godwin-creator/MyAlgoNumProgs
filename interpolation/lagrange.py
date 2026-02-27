#Interpolation polynomiale par la méthode de Lagrange.

from .utils import verifier_points

def lagrange(xi, yi):

    n = verifier_points(xi, yi)

    def p(x):
        result = 0.0
        for i in range(n):
            Li = 1.0
            for j in range(n):
                if j != i:
                    Li *= (x - xi[j]) / (xi[i] - xi[j])
            result += yi[i] * Li
        return result
    return p