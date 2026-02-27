from utils.verifications import verifier_egalite_dimensions, verifier_tolerance, verifier_iterations, verifier_vecteur
from utils.linear_utils import norme_vecteur, copie_vecteur

def jacobi(A, b, x0=None, tolerance=1e-6, max_iteration=100):

    n = verifier_egalite_dimensions(A, b)
    tolerance = verifier_tolerance(tolerance)
    max_iteration = verifier_iterations(max_iteration)

    if x0 is None:
        x = [0.0] * n
    else:
        verifier_vecteur(x0, n, "x0")
        x = copie_vecteur(x0)

    new_x = [0.0] * n

    # Vérifions que les éléments diagonaux ne sont pas nuls
    for i in range(n):
        if abs(A[i][i]) < 1e-12:
            raise ValueError(f"Élément diagonal A[{i}][{i}] nul ou trop petit : {A[i][i]}. La méthode de Jacobi ne peut pas s'appliquer.")

    for iteration in range(max_iteration):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            new_x[i] = (b[i] - s) / A[i][i]

        # Calcul de l'erreur relative
        difference = norme_vecteur([new_x[i] - x[i] for i in range(n)])
        if difference < tolerance:
            return new_x, iteration+1, True

        # échange des références pour éviter une copie inutile
        x, new_x = new_x, x

    return x, max_iteration, False