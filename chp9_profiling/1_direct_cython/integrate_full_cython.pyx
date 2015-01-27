# cython: profile=True
from libc.math cimport sin

cdef double c_sin2(double x):
    return sin(x) ** 2

def integrate_sin2(double a, double b, f, int N=2000):
    cdef:
        int i
        double s = 0.0
        double dx = (b - a) / N
    for i in range(N):
        s += c_sin2(a + i * dx)
    return s * dx

def integrate_no_overhead(double a, double b, f, int N=2000):
    cdef:
        int i
        double s = 0.0
        double dx = (b - a) / N
    for i in range(N):
        s += sin(a + i * dx) ** 2
    return s * dx
