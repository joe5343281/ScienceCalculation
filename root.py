#!/usr/bin/env python3

def EvalSlope(func,x):
    dx = 0.000001
    dy = func(x + dx) - func(x)
    
    return dy/dx

def Newton(func, x):
    derivate = EvalSlope(func, x)
    xn = x - (func(x)/derivate)
    
    return Newton(func, xn) if func(xn) > 0.5 else xn
    
def f(x):
    return ((x**14) - 1234567890123456)
    
def main():
    print(Newton(f, 100))

main()
