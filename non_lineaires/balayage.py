def balayage(f, a, b, h):

    if h <= 0:
        raise ValueError("Le pas doit être strictement positif.")

    x_prev = a
    f_prev = f(a)
    intervalles = []
    cpt = 0  # compteur de changements de signe

    x_curr = a + h
    while x_curr <= b:  # parcours par pas h
        f_curr = f(x_curr)
        if f_prev * f_curr < 0:
            intervalles.append((x_prev, x_curr))
            cpt += 1
        x_prev, f_prev = x_curr, f_curr
        x_curr += h

    if x_prev < b:
        f_b = f(b)
        if f_prev * f_b < 0:
            intervalles.append((x_prev, b))
            cpt += 1

    if cpt == 0:
        print(f"Aucun changement de signe détecté sur l'intervalle: [{a}; {b}]")
    else:
        print(f"Nombre total de changements de signe : {cpt}")
        print("Fin du balayage")

    return intervalles