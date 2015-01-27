# cython: profile=True
from libc.math cimport sin

def integrate(double a, double b, f, int N=2000):
    cdef:
        int i
        double s = 0.0
        double dx = (b - a) / N
    for i in range(N):
        s += sin(a + i * dx) ** 2
    return s * dx
