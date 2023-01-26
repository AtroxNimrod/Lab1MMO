import cvxpy as cp
import numpy as np

# Cream variabilele de decizie
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()
x4 = cp.Variable()
x5 = cp.Variable()

# Cream obiectivul de minimizat
objective = cp.Minimize(30*x1 +5*x2 +4*x3 +3*x4 +2*x5 )

# Cream constrangerile
constraints = [10*x1 +2*x2 +2*x3 +x4+x5 >=100,
               2*x1 +x2 + x4 >= 100,
               12*x2 +10*x3 + 12*x4 +x5 >=300,
               x1 +6*x2 +3*x3 +x4+ 7*x5 >=200,
               12*x2 +10*x3 +12*x4+ x5 <=600,
               x1 >= 0, x2 >= 0, x3 >= 0, x4 >= 0, x5>=0]

# Cream problema de optimizare
problem = cp.Problem(objective, constraints)

# Rezolvam problema
problem.solve()

# Afisam rezultatele
print("Rezultatul optim:", round(problem.value))
print("Valoarea optima pentru x1:", np.round(x1.value))
print("Valoarea optima pentru x2:", np.round(x2.value))
print("Valoarea optima pentru x3:", np.round(x3.value))
print("Valoarea optima pentru x4:", np.round(x4.value))
print("Valoarea optima pentru x5:", np.round(x5.value))