import cvxpy as cp

# Cream variabilele de decizie
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()
x4 = cp.Variable()
x5 = cp.Variable()

# Cream obiectivul de maximizare
objective = cp.Maximize(15*x1 +22*x2 +23*x3 +17*x4 +20*x5 )

# Cream constrangerile
constraints = [350*x1 +70*x2 +420*x3 +700*x4 <=140000,
               400*x1 +600*x2 +80*x3 +100*x4+ 124*x5 <=200000,
               180*x1 +270*x2 +450*x3 + 810*x5 <=180000,
               6*x1 +12*x2 +18*x3 +12*x4+ 24*x5 <=9600,
               1000*x1 +1000*x2 +1000*x3 +1000*x4+ 1000*x5 <=550000,
               x1 >= 0, x2 >= 0, x3 >= 0, x4 >= 0, x5>=0]

# Cream problema de optimizare
problem = cp.Problem(objective, constraints)

# Rezolvam problema
problem.solve()

# Afisam rezultatele
print("Rezultatul optim:", problem.value)
print("Valoarea optima pentru x1:", x1.value)
print("Valoarea optima pentru x2:", x2.value)
print("Valoarea optima pentru x3:", x3.value)
print("Valoarea optima pentru x4:", x4.value)
print("Valoarea optima pentru x5:", x5.value)