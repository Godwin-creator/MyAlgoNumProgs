import copy

def est_matrice_valide(A):
    if not isinstance(A, list) or not A:
        raise TypeError("La matrice doit être une liste non vide.")
    if not all(isinstance(ligne, list) for ligne in A):
        raise TypeError("Chaque ligne doit être une liste.")
    nb_colonnes = len(A[0])
    if nb_colonnes == 0:
        raise ValueError("Les lignes de la matrice ne peuvent pas être vides.")
    for i, ligne in enumerate(A):
        if len(ligne) != nb_colonnes:
            raise ValueError(f"La ligne {i} a {len(ligne)} colonnes, alors que la première ligne en a {nb_colonnes}.")
    return True

def est_matrice_carree(A):
    est_matrice_valide(A)
    if len(A) != len(A[0]):
        raise ValueError("La matrice n'est pas carrée (nombre de lignes différent du nombre de colonnes).")
    return True

def transpose_matrice(A):
    est_matrice_valide(A)
    n_lignes = len(A)
    n_colonnes = len(A[0])
    # Création de la matrice transposée
    At = [[A[i][j] for i in range(n_lignes)] for j in range(n_colonnes)]
    return At

def produit_matrices(A, B):
    est_matrice_valide(A)
    est_matrice_valide(B)
    n = len(A)          # nombre de lignes de A
    m = len(A[0])       # nombre de colonnes de A
    p = len(B[0])       # nombre de colonnes de B
    if m != len(B):
        raise ValueError(f"Dimensions incompatibles : A ({n}x{m}) et B ({len(B)}x{p}) ne peuvent pas être multipliées.")

    # Initialisation de la matrice produit avec des zéros
    C = [[0.0] * p for _ in range(n)]

    # Calcul du produit
    for i in range(n):
        for j in range(p):
            s = 0.0
            for k in range(m):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

def determinant_matrice(A):
    est_matrice_carree(A)
    n = len(A)
    # Copie de la matrice pour ne pas modifier l'originale
    M = [ligne[:] for ligne in A]
    det = 1.0
    for k in range(n-1):
        # Recherche du pivot maximal dans la colonne k à partir de la ligne k
        pivot_row = max(range(k, n), key=lambda r: abs(M[r][k]))
        if abs(M[pivot_row][k]) < 1e-12:
            # Pivot quasi nul => matrice singulière
            raise ValueError("Matrice singulière, déterminant nul.")
        # Échange de lignes si nécessaire
        if pivot_row != k:
            M[k], M[pivot_row] = M[pivot_row], M[k]
            det = -det  # changement de signe du déterminant
        # Élimination
        pivot = M[k][k]
        det *= pivot
        for i in range(k+1, n):
            factor = M[i][k] / pivot
            if factor != 0:
                for j in range(k+1, n):
                    M[i][j] -= factor * M[k][j]
                # On ne met pas à zéro explicitement, on peut laisser M[i][k] non nul,
                # mais cela n'affecte pas le calcul du déterminant.
    # Dernier pivot
    if abs(M[n-1][n-1]) < 1e-12:
        raise ValueError("Matrice singulière, déterminant nul.")
    det *= M[n-1][n-1]
    return det

def inverse_matrice(A):
    est_matrice_carree(A)
    n = len(A)
    # Création de la matrice augmentée [A | I]
    Aug = [A[i][:] + [1.0 if j == i else 0.0 for j in range(n)] for i in range(n)]

    # Gauss-Jordan avec pivot partiel
    for k in range(n):
        # Recherche du pivot
        pivot_row = max(range(k, n), key=lambda r: abs(Aug[r][k]))
        if abs(Aug[pivot_row][k]) < 1e-12:
            raise ValueError("Matrice singulière, inversion impossible.")
        # Échange de lignes
        if pivot_row != k:
            Aug[k], Aug[pivot_row] = Aug[pivot_row], Aug[k]
        # Normalisation de la ligne k
        pivot = Aug[k][k]
        for j in range(2*n):
            Aug[k][j] /= pivot
        # Élimination dans toutes les autres lignes
        for i in range(n):
            if i != k:
                factor = Aug[i][k]
                if factor != 0:
                    for j in range(2*n):
                        Aug[i][j] -= factor * Aug[k][j]

    # Extraction de l'inverse (partie droite de la matrice augmentée)
    inv = [Aug[i][n:] for i in range(n)]
    return inv

# Exemple d'utilisation pour deux matrices A et B
if __name__ == "__main__":
    # Tests simples
    A = [[1, 2,-3], [0, 2, -1], [0, 0, 2]]
    print("A =", A)
    print("Transposée de A :", transpose_matrice(A))
    B = [[1, 2,-3], [2, 6, -5], [1, -2, 1]]
    print("Produit A * B :", produit_matrices(A, B))
    print("Déterminant de A :", determinant_matrice(A))
    invA = inverse_matrice(A)
    print("Inverse de A :", invA)
    # Vérification A * invA ≈ I
    I = produit_matrices(A, invA)
    print("A * invA =", I)