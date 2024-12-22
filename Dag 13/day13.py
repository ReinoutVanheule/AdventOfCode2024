from aoc import read_input
import math
import re
from sympy import symbols, Eq, solve

# input
lines = [list(map(int,re.findall(r'\d+',line))) for line in read_input("inputdag13")]

# part 1 and 2
k,p = symbols('k,p') 

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def one_combo(a,b,c):
    i = 0
    while True:
        q,r = divmod(c-i*a,b)
        if r==0:
            return (i,q)
        i+=1
        if i == b:
            raise Exception()
    

def claw(A,B,C):
    try:
        a,b = one_combo(A[0],B[0],C[0])
        prod = lcm(A[0],B[0])
        m = prod//A[0]
        l = prod//B[0]
        
        c,d = one_combo(A[1],B[1],C[1])
        prod = lcm(A[1],B[1])
        q = prod//A[1]
        r = prod//B[1]
        
        eq1 = Eq(a+k*m, c+p*q) 
        eq2 = Eq(b-k*l,d-p*r)
        
        solve_eq = solve((eq1, eq2), (k,p))
        k_value = solve_eq[k]
        p_value = solve_eq[p]
        
        if k_value%1==0 and p_value%1==0:
            A = a+k_value*m
            B = b-k_value*l
            return 3*A+B
        return 0
    
    except:
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