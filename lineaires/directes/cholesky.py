def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                diag = A[i][i] - s
                if diag <= 0:
                    raise ValueError("Matrice non définie positive")
                L[i][j] = diag ** 0.5
            else:
                if L[j][j] == 0:
                    raise ValueError("Pivot nul")
                L[i][j] = (A[i][j] - s) / L[j][j]
    return L