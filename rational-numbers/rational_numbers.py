from __future__ import division
import math


class Rational(object):
    def __init__(self, numer, denom):
        self.gcd = math.gcd(numer, denom)
        if denom < 0:
            self.gcd = self.gcd * -1
        self.numer = numer // self.gcd
        self.denom = denom // self.gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        """(a1 * b2 + a2 * b1) / (b1 * b2)"""
        return Rational((self.numer * other.denom + other.numer * self.denom),
                        (self.denom * other.denom))

    def __sub__(self, other):
        """(a1 * b2 - a2 * b1) / (b1 * b2)"""
        return Rational((self.numer * other.denom) - (self.denom * other.numer),
                        (self.denom * other.denom))

    def __mul__(self, other):
        """ (a1 * a2) / (b1 * b2)"""
        return Rational(self.numer * other.numer,
                        self.denom * other.denom)

    def __truediv__(self, other):
        """(a1 * b2) / (a2 * b1)"""
        return Rational(self.numer * other.denom,
                        other.numer * self.denom)

    def __abs__(self):
        """|a|/|b|"""
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        """r^n = (a^n)/(b^n)"""
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        """r = a/b` is `x^(a/b) = root(x^a, b)`
        root(p, q) is the q th root of p
        """
        return (base**(self.numer//self.gcd))**(1/(self.denom//self.gcd))
