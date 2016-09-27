#!/usr/bin/env python3

def diff(func, x):
    dx = 0.0000001
    dy = func(x + dx) - func(x)   
    
    return dy/dx

def f(x):
    return ((x**2) + (3*x) + 2)

def main():
    print(diff(f, 1))
    
main()
