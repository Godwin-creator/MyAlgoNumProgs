def norme_vecteur(v):
    return max(abs(x) for x in v)

def norme_matrice(A):
    return max(sum(abs(aij) for aij in ligne) for ligne in A)

def produit_matrice_vecteur(A, v):
    n = len(A)
    if len(v) != n:
        raise ValueError("Dimensions incompatibles")
    return [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]

def copie_matrice(A):
    return [ligne[:] for ligne in A]

def copie_vecteur(v):
    return v[:]

def est_diagonale_dominante(A, strict=True):
    n = len(A)
    for i in range(n):
        somme = sum(abs(A[i][j]) for j in range(n) if j != i)
        if strict:
            if abs(A[i][i]) <= somme:
                return False
        else:
            if abs(A[i][i]) < somme:
                return False
    return True

def resoudre_LU(L, U, b):
    n = len(L)
    # Résolution de L y = b (descente)
    y = [0.0] * n
    for i in range(n):
        s = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - s
    # Résolution de U x = y (remontée)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(U[i][j] * x[j] for j in range(i+1, n))
        if U[i][i] == 0:
            raise ValueError("Matrice U singulière (pivot nul)")
        x[i] = (y[i] - s) / U[i][i]
    return x

def resoudre_Cholesky(L, b):
    n = len(L)
    # Résolution de L y = b (descente)
    y = [0.0] * n
    for i in range(n):
        s = sum(L[i][j] * y[j] for j in range(i))
        if L[i][i] == 0:
            raise ValueError("Matrice L singulière")
        y[i] = (b[i] - s) / L[i][i]
    # Résolution de L^T x = y (remontée)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(L[j][i] * x[j] for j in range(i+1, n))
        x[i] = (y[i] - s) / L[i][i]
    return x