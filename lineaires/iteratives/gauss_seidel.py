from utils.verifications import verifier_egalite_dimensions, verifier_tolerance, verifier_iterations, verifier_vecteur
from utils.linear_utils import norme_vecteur, copie_vecteur

def gauss_seidel(A, b, x0=None, tolerance=1e-6, max_iteration=100):

    n = verifier_egalite_dimensions(A, b)
    tolerance = verifier_tolerance(tolerance)
    max_iteration = verifier_iterations(max_iteration)

    if x0 is None:
        x = [0.0] * n
    else:
        verifier_vecteur(x0, n, "x0")
        x = copie_vecteur(x0)

    # Vérifions les diagonales
    for i in range(n):
        if abs(A[i][i]) < 1e-12:
            raise ValueError(f"Élément diagonal A[{i}][{i}] nul ou trop petit : {A[i][i]}. La méthode de Gauss-Seidel ne peut pas s'appliquer.")

    for iteration in range(max_iteration):
        old_x = x[:]  # copie pour le calcul de la différence
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))        # valeurs déjà mises à jour
            s2 = sum(A[i][j] * old_x[j] for j in range(i+1, n))  # anciennes valeurs
            x[i] = (b[i] - s1 - s2) / A[i][i]

        difference = norme_vecteur([x[i] - old_x[i] for i in range(n)])
        if difference < tolerance:
            return x, iteration+1, True

    return x, max_iteration, False