from aoc import read_input
import re
from sympy import symbols, Eq, solve

# input
lines = [list(map(int,re.findall(r'\d+',line))) for line in read_input("inputdag13")]

# part 1 and 2    
def claw(A,B,C):
    x,y = symbols("x,y")
    eq1 = Eq(x*A[0]+y*B[0],C[0])
    eq2 = Eq(x*A[1]+y*B[1],C[1])
    solve_eq = solve((eq1, eq2), (x,y))
    if solve_eq[x]%1==0 and solve_eq[y]%1 == 0:
        return 3*solve_eq[x]+solve_eq[y]
    else:
        return 0

i = 0
money1 = money2 = 0
while i < len(lines):
    A = lines[i]
    B = lines[i+1]
    C = lines[i+2]
    money1 += claw(A,B,C)
    money2 += claw(A,B,(C[0]+10000000000000,C[1]+10000000000000))
    i += 4
    
print(money1,money2)
