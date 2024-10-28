# use pip install z3 and pip install z3-solver on the terminal 

from z3 import Solver, Int, sat

# This library uses wizardcraft  

# Define variables
x = Int('x')
y = Int('y')

s = Solver()

s.add(x**2 + y**2 == 0)
s.add(x == 1)

# This somehow checks if the expression is satisfiable
if s.check() == sat:
    model = s.model()
    print(f'x = {model[x]}')
    print(f'y = {model[y]}')

else:
    print('the expression is bullshit\n')