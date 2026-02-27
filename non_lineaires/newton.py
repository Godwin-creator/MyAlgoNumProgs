def newton(f, f_prime, x0, tolerance=1e-6, max_iteration=100, max_restart=10):

    x = x0
    for restart in range(max_restart):
        for iteration in range(max_iteration):
            try:
                fx = f(x)
                fpx = f_prime(x)
                if abs(fpx) < 1e-12:  # en vrai, la dérivée est quasi nulle
                    raise ZeroDivisionError("Bon bah, la dérivé est nulle")

                new_x = x - fx / fpx
                if abs(new_x - x) < tolerance:
                    return new_x, iteration + 1, f"Il y a eu CONVERGENCE after {restart} redémarrages 'elle est rapide si < 10 itérations'"

                x = new_x
            except (ZeroDivisionError, OverflowError, ValueError) as e:
                #on change x0
                print(f"Il y a eu un blème à l'itération {iteration} : {e}")
                break  # sort de la boucle for interne
        else:
            # La boucle interne s'est terminée normalement sans break => dépassement max_iter
            return x, max_iteration, f"On a eu NON CONVERGENCE après {max_iteration} itérations (restart {restart})"

        #Si le prog arrive ici, c'est qu'une exception a été levée. Ce qui m'oblige à modifier le x.
        eps = tolerance * (1 + abs(x))
        x += eps
        print(f"Redémarrage with x0 = {x}")

    return x, max_restart * max_iteration, f"échec après {max_restart} redémarrages"