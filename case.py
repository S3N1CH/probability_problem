from math import exp
from scipy.integrate import quad
from termcolor import cprint
from random import random, randint

print("Rezolvarea problemei S10.4(S1.34)")
print("\nProgram realizat de studentii:")
print("Peleskov Semion, Energetica 2104_1D,")
print("Rescanu Ana-Maria-Ruxandra, Energetica 2102_1D.")

print("\nCazuri posibile:")
print("1) p < m, b - a > 1/2, p(A) > p(B);")
print("2) p < m, b - a < 1/2, p(A) < p(B);")
print("3) p > m, b + a > 3/2, p(A) > p(B);")
print("4) p > m, b + a < 3/2, p(A) < p(B).")

count = 1
case = input("\nIntroduceti caz: ")

while True:

    m = random()
    p = random()
    sigma = randint(1, 5)

    # Functia Laplace
    def phi(u):
        return quad(lambda u: exp(-(u**2)/2), 0, u)[0]

    if p < m:
        x1 = (m - p) / sigma
        x2 = (m + p) / sigma
        alpha = phi(x1)
        beta = phi(x2)
        rel = beta - alpha

        if rel > 1 / 2:
            current_case = 1
        elif rel < 1 / 2:
            current_case = 2

    elif p > m:
        u1 = (p - m) / sigma
        u2 = (m + p) / sigma
        alpha = phi(u1)
        beta = phi(u2)
        rel = beta + alpha

        if rel > 3 / 2:
            current_case = 3
        elif rel < 3 / 2:
            current_case = 4

    if current_case == int(case):
        print(f"\nDatele initiale propuse de program pentru caz {case}:")
        cprint(f"Media(m) = {str(m)[:4]}", "green")
        cprint(f"Probabilitatea(p) = {str(p)[:4]}", "green")
        cprint(f"Abaterea medie patratica(sigma) = {sigma}", "green")

        print("\nSolutie:")
        print(f"\nVariabila aleatoare este:\nX ~ N({str(m)[:4]}, {sigma ** 2});")
        cprint(f"Evenimente: A:|X| < {str(p)[:4]}, B:|X| >= {str(p)[:4]};", "cyan")
        cprint("B = 1 - A (B este complementul lui A);", "cyan")

        if current_case in [1, 2]:
            print("\nModulul se expliciteaza pentru cazul p < m:")
            cprint(f"Alpha = FI[(m-p)/sigma] = {str(alpha)[:6]};", "blue")
            cprint(f"Beta = FI[(m+p)/sigma] = {str(beta)[:6]};", "blue")
            print(f"Beta - Alpha = {str(rel)[:6]};\n")

            if rel > 1 / 2:
                current_case = 1
                print("Beta - Alpha > 1/2, caz 1;")
                cprint("Concluzie: p(A) > p(B),\nProbabilitatea lui A mai mare decat probabilitate lui B.", "red")
            else:
                current_case = 2
                print("Beta - Alpha < 1/2, caz 2;")
                cprint("Concluzie: p(A) < p(B),\nProbabilitatea lui A mai mica decat probabilitate lui B.", "red")
        else:
            print("\nModulul se expliciteaza pentru cazul p > m:")
            cprint(f"Alpha = FI[(p-m)/sigma] = {str(alpha)[:6]};", "blue")
            cprint(f"Beta = FI[(m+p)/sigma] = {str(beta)[:6]};", "blue")
            print(f"Beta + Alpha = {str(rel)[:6]};\n")

            if rel > 3 / 2:
                current_case = 3
                print("Beta + Alpha > 3/2, caz 3;")
                cprint("Concluzie: p(A) > p(B),\nProbabilitatea lui A mai mare decat probabilitate lui B.", "red")
            else:
                current_case = 4
                print("Beta + Alpha < 3/2, caz 4;")
                cprint("Concluzie: p(A) < p(B),\nProbabilitatea lui A mai mica decat probabilitate lui B.", "red")

        cprint(f"\nNumar de iteratii: {count}.", "magenta")
        end = input("\nApasati 'Enter' pentru a trece la urmatoare problema.")
        print("\nCazuri posibile:")
        print("1) p < m, b - a > 1/2, p(A) > p(B);")
        print("2) p < m, b - a < 1/2, p(A) < p(B);")
        print("3) p > m, b + a > 3/2, p(A) > p(B);")
        print("4) p > m, b + a < 3/2, p(A) < p(B).")
        case = input("\nIntroduceti caz: ")
        count = 1

    else:
        count += 1
