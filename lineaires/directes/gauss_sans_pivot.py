from utils.verifications import verifier_egalite_dimensions, verifier_tolerance
from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_sans_pivot(A, b, tol=1e-12):
    """
    Résolution par élimination de Gauss sans pivot.
    La matrice A doit être inversible et avoir tous ses pivots non nuls.
    Paramètres :
        A : matrice carrée (liste de listes)
        b : second membre (liste)
        tol : seuil pour considérer un pivot comme nul (par défaut 1e-12)
    Retourne :
        x : vecteur solution (liste)
    Lève une exception si un pivot est nul ou si la matrice est singulière.
    """
    n = verifier_egalite_dimensions(A, b)
    tol = verifier_tolerance(tol)

    A = copie_matrice(A)
    b = copie_vecteur(b)

    # Triangularisation
    for k in range(n-1):
        if abs(A[k][k]) < tol:
            raise ValueError(f"Pivot nul à l'étape {k} : |a[{k}][{k}]| = {abs(A[k][k])} < {tol}. Utilisez la méthode avec pivot.")
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            # Mise à jour de la ligne i à partir de k+1
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
            # Optionnel : A[i][k] = 0.0

    # Vérification du dernier pivot
    if abs(A[n-1][n-1]) < tol:
        raise ValueError("Matrice singulière : dernier pivot nul.")

    # Résolution par remontée
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x