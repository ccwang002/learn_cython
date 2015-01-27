# cython: profile=True
from libc.math cimport sin
from math import pi
cimport cython

cdef double sin2(double x):
    return sin(x) ** 2

@cython.cdivision(True)
cdef double c_integrate(double a, double b, double (*f)(double), int N):
    cdef:
        int i
        double s = 0.0
        double dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx


@cython.cdivision(True)
cdef double c_integrate_no_overhead(double a, double b, int N):
    cdef:
        int i
        double s = 0.0
        double dx = (b - a) / N
    for i in range(N):
        s += sin(a + i * dx) ** 2
    return s * dx

def demo():
    cdef:
        double a = 0.0, b = 2.0 * pi
        int N = 400000
    c_integrate(a, b, sin2, N)

def demo_no_overhead():
    cdef:
        double a = 0.0, b = 2.0 * pi
        int N = 400000
    c_integrate_no_overhead(a, b, N)
