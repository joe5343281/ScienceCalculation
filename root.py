#!/usr/bin/env python3

def EvalSlope(func,x):
    dx = 0.000001
    dy = func(x + dx) - func(x)
    
    return dy/dx

def NewtonMethond(func, x):
    slope = EvalSlope(func, x)
    xn = x - (func(x)/slope)
    
    if((func(xn) > 0.5) or (func(xn) < -0.5)):
        return NewtonMethond(func, xn)
    else:
        return xn
    
def f(x):
    return ((x**14) - 1234567890123456)
    
def main():
    print(NewtonMethond(f, 100))

main() 
