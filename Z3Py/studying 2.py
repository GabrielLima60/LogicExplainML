from z3 import *

x = Int('x')
y = Int('y')

s = Solver()

s.add(Or(x == 3, y == 7))
s.add(And(x > 0, y > 0))

if s.check() == sat:
    model = s.model()

    print(f'x = {model[x]}')
    print(f'y = {model[y]}')