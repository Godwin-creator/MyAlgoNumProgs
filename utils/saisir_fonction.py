# Saisie d'une fonction mathématique sous forme d'expression num.
def saisir_fonction():
    import math
    expr = input("Entrez l'expression de la fonction f(x) (utilisez 'x' comme variable) : ")

    namespace = {'x': 0.0, 'math': math, 'sin': math.sin, 'cos': math.cos,
                 'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
                 'pi': math.pi, 'e': math.e}

    # Small test avec une valeur simple pour vérifier la validité de la saisie
    try:
        namespace['x'] = 1.0
        eval(expr, namespace)
    except Exception as e:
        raise ValueError(f"Expression invalide : {e}")
    def f(x):
        namespace['x'] = x
        return eval(expr, namespace)
    return f