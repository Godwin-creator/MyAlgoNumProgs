import math

def secante(f, x0, x1, tolerance=1e-6, max_iteration=100):

    try:
        f_x0 = f(x0)
        f_x1 = f(x1)
    except Exception:
        return x1, 0, False
    for i in range(max_iteration):
        denominateur = f_x1 - f_x0
        # Protection division par zéro
        if abs(denominateur) < 1e-14:
            return x1, i+1, False
        x2 = x1 - f_x1 * (x1 - x0) / denominateur
        if math.isnan(x2) or math.isinf(x2):
            return x1, i+1, False
        if abs(x2 - x1) < tolerance:
            return x2, i+1, True
        x0, x1 = x1, x2
        f_x0, f_x1 = f_x1, f(x1)

    return x1, max_iteration, False