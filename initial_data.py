from math import exp
from scipy.integrate import quad
from termcolor import cprint

print("Rezolvarea problemei S10.4(S1.34)")
print("\nProgram realizat de studentii:")
print("Peleskov Semion, Energetica 2104_1D,")
print("Rescanu Ana-Maria-Ruxandra, Energetica 2102_1D.")

while True:

    print("\nIntroduceti datele initiale:")

    try:
        m = float(input("Media(m) = "))
        p = float(input("Probabilitatea(p) = "))
        sigma = float(input("Abaterea medie patratica(sigma) = "))
    except ValueError:
        print("Error! Datele introduse nu sunt corecte!")
        continue

    print("\nSolutie:")
    print(f"\nVariabila aleatoare este:\nX ~ N({m}, {sigma ** 2});")
    cprint(f"Evenimente: A:|X| < {p}, B:|X| >= {p};", "cyan")
    cprint("B = 1 - A (B este complementul lui A);", "cyan")

    # Functia Laplace
    def phi(u):
        return quad(lambda u: exp(-(u**2)/2), 0, u)[0]

    if p < m:
        print("\nModulul se expliciteaza pentru cazul p < m:")
        x1 = (m - p) / sigma
        x2 = (m + p) / sigma
        alpha = phi(x1)
        beta = phi(x2)
        rel = beta - alpha
        cprint(f"Alpha = FI[(m-p)/sigma] = {str(alpha)[:6]};", "blue")
        cprint(f"Beta = FI[(m+p)/sigma] = {str(beta)[:6]};", "blue")
        print(f"Beta - Alpha = {str(rel)[:6]};\n")

        if rel > 1/2:
            print("Beta - Alpha > 1/2, caz 1;")
            cprint("Concluzie: p(A) > p(B),\nProbabilitatea lui A mai mare decat probabilitate lui B.", "red")
        else:
            print("Beta - Alpha < 1/2, caz 2;")
            cprint("Concluzie: p(A) < p(B),\nProbabilitatea lui A mai mica decat probabilitate lui B.", "red")

    elif p > m:
        print("\nModulul se expliciteaza pentru cazul p > m:")
        u1 = (p - m) / sigma
        u2 = (m + p) / sigma
        alpha = phi(u1)
        beta = phi(u2)
        rel = beta + alpha
        cprint(f"Alpha = FI[(p-m)/sigma] = {str(alpha)[:6]};", "blue")
        cprint(f"Beta = FI[(m+p)/sigma] = {str(beta)[:6]};", "blue")
        print(f"Beta + Alpha = {str(rel)[:6]};\n")

        if rel > 3/2:
            print("Beta + Alpha > 3/2, caz 3;")
            cprint("Concluzie: p(A) > p(B),\nProbabilitatea lui A mai mare decat probabilitate lui B.", "red")
        else:
            print("Beta + Alpha < 3/2, caz 4;")
            cprint("Concluzie: p(A) < p(B),\nProbabilitatea lui A mai mica decat probabilitate lui B.", "red")

    end = input("\nApasati 'Enter' pentru a trece la urmatoare problema.")
