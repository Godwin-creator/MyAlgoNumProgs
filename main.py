import os
import math
import sys
from sympy import symbols, sympify, pi, E #pour que l'user puisse saisir pi pour π.

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lineaires.directes import gauss_sans_pivot, gauss_pivot, gauss_jordan, crout, cholesky
from lineaires.iteratives import jacobi, gauss_seidel
from non_lineaires import balayage, dichotomie, newton, secante, point_fixe
from utils import saisir_fonction, saisir_matrice
#from utils.linear_utils import resoudre_LU, resoudre_Cholesky

def menu_principal():
    print("\n||- Analyse Numérique : Résolution d'équations -||")
    print("1. Systèmes linéaires")
    print("2. Équations non linéaires")
    print("0. Quitter")
    return input("Choix : ")

def menu_lineaire():
    print("\n--- Méthodes pour systèmes linéaires ---")
    print("1. Gauss sans pivot")
    print("2. Gauss avec pivot partiel")
    print("3. Gauss-Jordan")
    print("4. Crout (Décomposition LU)")
    print("5. Cholesky")
    print("6. Jacobi")
    print("7. Gauss-Seidel")
    print("0. Retour")
    return input("Choix : ")

def menu_non_lineaire():
    print("\n--- Méthodes pour équations non linéaires ---")
    print("1. Balayage (séparation des racines)")
    print("2. Dichotomie")
    print("3. Newton-Raphson")
    print("4. Sécante")
    print("5. Point fixe")
    print("0. Retour")
    return input("Choix : ")

def main():
    while True:
        choix = menu_principal()
        if choix == '0':
            print("Au revoir !")
            break
        elif choix == '1':
            while True:
                sous_choix = menu_lineaire()
                if sous_choix == '0':
                    break
                try:
                    print("\nSaisie de la matrice A :")
                    A = saisir_matrice.saisir_matrice()
                    n = len(A)
                    b = saisir_matrice.saisir_vecteur(n)

                    if sous_choix == '1':
                        x = gauss_sans_pivot.gauss_sans_pivot(A, b)
                        print("Solution :", x)
                    elif sous_choix == '2':
                        x = gauss_pivot.gauss_pivot(A, b)
                        print("Solution :", x)
                    elif sous_choix == '3':
                        x = gauss_jordan.gauss_jordan(A, b)
                        print("Solution :", x)
                    elif sous_choix == '4':
                        L, U = crout.crout(A)
                        print("L =", L)
                        print("U =", U)
                        #x = resoudre_LU(L, U, b)
                        print("Solution :", x)
                    elif sous_choix == '5':
                        L = cholesky.cholesky(A)
                        print("L (Cholesky) =", L)
                        #x = resoudre_Cholesky(L, b)
                        print("Solution :", x)
                    elif sous_choix == '6':
                        x0 = [0.0]*n
                        x, iter, conv = jacobi.jacobi(A, b, x0)
                        print(f"Solution : {x}, itérations : {iter}, convergence : {conv}")
                    elif sous_choix == '7':
                        x0 = [0.0]*n
                        x, iter, conv = gauss_seidel.gauss_seidel(A, b, x0)
                        print(f"Solution : {x}, itérations : {iter}, convergence : {conv}")
                    else:
                        print("Choix invalide")
                except Exception as e:
                    print(f"Erreur : {e}")

        elif choix == '2':
            while True:
                sous_choix = menu_non_lineaire()
                if sous_choix == '0':
                    break
                try:
                    f = saisir_fonction.saisir_fonction()

                    if sous_choix == '1':
                        a = float(input("Borne inférieure a : "))
                        b = float(input("Borne supérieure b : "))
                        h = float(input("Pas de balayage h : "))
                        if h <= 0:
                            print("Le pas doit être positif.")
                        else:
                            intervalles = balayage.balayage(f, a, b, h)
                            print("Intervalles contenant une racine :", intervalles)

                    elif sous_choix == '2':
                        a = float(input("Borne inférieure a : "))
                        b = float(input("Borne supérieure b : "))
                        tolerance = float(input("Tolérance (def=1e-6) : ") or 1e-6)
                        max_iteration = int(input("Max itérations (def=100) : ") or 100)
                        racine, iter, conv = dichotomie.dichotomie(f, a, b, tolerance, max_iteration)
                        print(f"Racine : {racine}, itérations : {iter}, convergence : {conv}")

                    elif sous_choix == '3':
                        #la dérivée est indisp
                        print("Saisie de la dérivée f'(x) :")
                        f_prime = saisir_fonction.saisir_fonction()

                        # Avant : x0 = float(input("Point initial x0 : "))
                        # Maintenant pour que l'user puisse saisir x0 = pi pour π :
                        x0_str = input("Point initial x0 : ")
                        x0 = float(sympify(x0_str))

                        tolerance = float(input("Tolérance (def=1e-6) : ") or 1e-6)
                        max_iteration = int(input("Max itérations (def=100) : ") or 100)
                        racine, iter, message = newton.newton(f, f_prime, x0, tolerance, max_iteration)
                        print(f"Racine = {racine}, itérations = {iter}")
                        print(message)
                        #racine, iter, conv = newton.newton(f, f_prime, x0, tolerance, max_iteration)
                        #print(f"Racine : {racine}, itérations : {iter}, convergence : {conv}")

                    elif sous_choix == '4':
                        try:
                            x0 = float(sympify(input("Premier point x0 : ")))
                            x1 = float(sympify(input("Second point x1 : ")))
                        except Exception as e:
                            print("Erreur dans les points initiaux :", e)
                            return
                        try:
                            f0 = f(x0)
                            f1 = f(x1)
                        except Exception as e:
                            print("Erreur : f(x0) ou f(x1) non définie :", e)
                            return
                        if math.isnan(f0) or math.isnan(f1) or math.isinf(f0) or math.isinf(f1):
                            print("Erreur : valeur infinie ou NaN détectée.")
                            return
                        tolerance = float(input("Tolérance (def=1e-6) : ") or 1e-6)
                        max_iteration = int(input("Max itérations (def=100) : ") or 100)
                        racine, nb_iter, conv = secante.secante(f, x0, x1, tolerance, max_iteration)
                        print(f"Racine : {racine}, itérations : {nb_iter}, convergence : {conv}")

                    elif sous_choix == '5':
                        # Pour point fixe, on a besoin de g(x) = x - f(x) ou autre
                        print("Saisie de la fonction g(x) pour le point fixe x = g(x) :")
                        g = saisir_fonction.saisir_fonction()
                        try:
                            x0_str = input("Point initial x0 : ")
                            allowed = {"pi": pi, "E": E}
                            x0 = float(sympify(x0_str, locals=allowed))
                        except Exception:
                            print("Erreur : valeur initiale invalide.")
                            return
                        try:
                            tol_str = input("Tolérance (def=1e-6) : ")
                            tolerance = float(sympify(tol_str, locals=allowed)) if tol_str else 1e-6
                            if tolerance <= 0:
                                raise ValueError
                        except Exception:
                            print("Erreur : tolérance invalide.")
                            return
                        try:
                            max_str = input("Max itérations (def=100) : ")
                            max_iteration = int(max_str) if max_str else 100
                            if max_iteration <= 0:
                                raise ValueError
                        except Exception:
                            print("Erreur : nombre d'itérations invalide.")
                            return
                        racine, nb_iter, conv = point_fixe.point_fixe(g, x0, tolerance, max_iteration)
                        print(f"Point fixe : {racine}")
                        print(f"Itérations : {nb_iter}")
                        print(f"Convergence : {conv}")

                    else:
                        print("Choix invalide")
                except Exception as e:
                    print(f"Erreur : {e}")

if __name__ == "__main__":
    main()