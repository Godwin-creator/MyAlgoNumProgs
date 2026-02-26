"""
Saisie d'une fonction mathématique sous forme d'expression.
"""

def saisir_fonction():
    """
    Demande à l'utilisateur une expression en x et retourne une fonction évaluable.
    Exemple: 'x**2 - 2' ou 'math.sin(x)'.
    """
    import math
    expr = input("Entrez l'expression de la fonction f(x) (utilisez 'x' comme variable) : ")
    # Espace de noms autorisé pour eval
    namespace = {'x': 0.0, 'math': math, 'sin': math.sin, 'cos': math.cos,
                 'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
                 'pi': math.pi, 'e': math.e}
    # Test avec une valeur simple pour vérifier la validité
    try:
        namespace['x'] = 1.0
        eval(expr, namespace)
    except Exception as e:
        raise ValueError(f"Expression invalide : {e}")
    def f(x):
        namespace['x'] = x
        return eval(expr, namespace)
    return f