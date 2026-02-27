#Approximation polynomiale au sens des moindres carrés.

from .utils import verifier_points
from lineaires.directes.gauss_pivot import gauss_pivot  # à importer depuis le module lineaire

def moindres_carres_polynomial(xi, yi, degre):

    n = verifier_points(xi, yi)
    if not isinstance(degre, int) or degre < 0:
        raise ValueError("Le degré doit être un entier positif ou nul.")
    if degre >= n:
        raise ValueError(f"Le degré ({degre}) doit être strictement inférieur au nombre de points ({n}).")

    m = degre + 1  # nombre de coefficients
    M = [[0.0] * m for _ in range(m)]
    b = [0.0] * m

    for i in range(n):
        x = xi[i]
        y = yi[i]

        puiss = [1.0]
        for k in range(1, 2*degre + 1):
            puiss.append(puiss[-1] * x)

        for j in range(m):
            for k in range(m):
                M[j][k] += puiss[j + k]
            b[j] += y * puiss[j]

    try:
        a = gauss_pivot(M, b)
    except Exception as e:
        raise RuntimeError(f"Échec de la résolution du système des moindres carrés : {e}")
    return a