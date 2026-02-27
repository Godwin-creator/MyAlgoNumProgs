import math

def point_fixe(g, x0, tolerance=1e-6, max_iteration=100):
    x = x0

    for i in range(max_iteration):
        try:
            new_x = g(x)
        except Exception:
            return x, i+1, False

        if math.isnan(new_x) or math.isinf(new_x):
            return x, i+1, False

        if abs(new_x - x) < tolerance:
            return new_x, i+1, True

        x = new_x

    return x, max_iteration, False