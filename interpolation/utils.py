#Utilitaires pour les méthodes d'interpolation et d'approximation.
import sympy as sp

def expr_lagrange(xi, yi):
    x = sp.Symbol('x')
    n = len(xi)
    expr = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if j != i:
                Li *= (x - xi[j]) / (xi[i] - xi[j])
        expr += yi[i] * Li
    return sp.simplify(expr)

def expr_newton(xi, yi):

    x = sp.Symbol('x')
    n = len(xi)
    # Calcul des différences divisées
    dd = [[0]*n for _ in range(n)]
    for i in range(n):
        dd[i][i] = yi[i]
    for k in range(1, n):
        for i in range(n-k):
            dd[i][i+k] = (dd[i+1][i+k] - dd[i][i+k-1]) / (xi[i+k] - xi[i])
    coeffs = [dd[0][i] for i in range(n)]
    # Construction du polynôme
    expr = 0
    produit = 1
    for i in range(n):
        expr += coeffs[i] * produit
        if i < n-1:
            produit *= (x - xi[i])
    return sp.simplify(expr)

def verifier_points(xi, yi):

    if not isinstance(xi, list) or not isinstance(yi, list):
        raise TypeError("xi et yi doivent être des listes.")
    if len(xi) != len(yi):
        raise ValueError("Les listes xi et yi doivent avoir la même longueur.")
    if len(xi) == 0:
        raise ValueError("Les listes ne peuvent pas être vides.")
    # Vérification que tous les éléments sont des nombres
    for i, (x, y) in enumerate(zip(xi, yi)):
        if not isinstance(x, (int, float)):
            raise TypeError(f"xi[{i}] n'est pas un nombre.")
        if not isinstance(y, (int, float)):
            raise TypeError(f"yi[{i}] n'est pas un nombre.")
    # Vérification des abscisses distinctes
    if len(set(xi)) != len(xi):
        raise ValueError("Les abscisses xi doivent être distinctes.")
    return len(xi)

def eval_polynome(coeffs, x):

    if not isinstance(coeffs, list):
        raise TypeError("coeffs doit être une liste.")
    if len(coeffs) == 0:
        raise ValueError("La liste des coefficients ne peut pas être vide.")
    result = 0.0
    for a in reversed(coeffs):
        result = result * x + a
    return result