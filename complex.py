#!/usr/bin/env python3

import math
import re

class  Complex():
    
    
    def __init__(self, real=0, imaginary=0):
        self.r = real
        self.i = imaginary

    def __add__(self, other):
        """It can make operator, +, be used for adding two Complex object"""    
        r = self.r + other.r
        i = self.i + other.i
        
        return Complex(r, i)
    
    def __sub__(self, other):
        """Above"""
        r = self.r - other.r
        i = self.i - other.i

        return Complex(r, i)

    def __mul__(self, other):
        """(a+bi)*(c+di) = a*c-b*d + (a*d+b*c)i"""
        a = self.r
        b = self.i
        c = other.r
        d = other.i
        
        r = a * c - b * d
        i = a * d + b * c

        return Complex(r, i)

    def __truediv__(self, other):
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        r = (a * c + b * d) / (c * c + d * d)
        i = (b * c - a * d) / (c * c + d * d)
        
        return Complex(r, i)

    def conj(self):
        return Complex(self.r, -1 * self.i)

    def ln(self):
        a = self.r
        b = self.i
        r = a * a + b * b
        w = (1/2)*math.log(r)
        x = math.acos(a/math.sqrt(r))
        
        return Complex(w, x)

    def exp(self):
        a = self.r
        b = self.i
        r = math.exp(a)

        return Complex(r * math.cos(b), r * math.sin(b))

    def rad(self):
        a = self.r
        b = self.i
        sqsum = a * a + b * b
        r = math.sqrt(sqsum)   
        co = a/r
        rad = math.acos(co)

        return rad

    def parser(self, comp):
        m = re.match('^([-/+]?\d*)?([-/+]?\d*)(i?)', comp)
        r = int(m.group(1))
        i = int(m.group(2)) 
        
        return Complex(r, i)

    def toString(self):
        return str(self.r) + str(self.i) + 'i'

