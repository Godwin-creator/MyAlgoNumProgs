def dichotomie(f, a, b, tolerance=1e-6, max_iteration=100):

    if f(a) * f(b) >= 0:
        raise ValueError("La fonction doit changer de signe aux bornes.")
    for i in range(max_iteration):
        c = (a + b) / 2
        if abs(b - a) < tolerance:
            return c, i+1, True #indique si la convergence a été atteinte (True si la condition d'arrêt a été satisfaite
                                # dans le nombre d'itérations maximal, False sinon).
        if f(c) == 0:
            return c, i+1, True

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, max_iteration, False