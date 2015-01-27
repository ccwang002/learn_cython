from math import sin

def cysin(double x):
    return sin(x) ** 2

def integrate(double a, double b, f, int N=2000):
    cdef:
        int i
        double s = 0.0
        double dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
