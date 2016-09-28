#!/usr/bin/env python3

def integral(f, a, b):
    sum = 0.0
    dx = 0.001
    while(a < (b - 0.001)): 
        sum += f(b - dx) * dx
        b -= dx
    
    return sum
    
def f(x):
    return (3 * (x**2))
    
def main():
    print("f(x)=3*(x^3),from 0 to 10")
    print(interal(f, 0, 10))
    
main()
