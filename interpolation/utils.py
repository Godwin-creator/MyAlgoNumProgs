#Utilitaires pour les méthodes d'interpolation et d'approximation.

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