from libc.math cimport sqrt

cdef class Particle:
    """Simple Particle extension type."""
    cdef double mass, position, velocity

    def __init__(self, m, p, v):
        self.mass = m
        self.position = p
        self.velocity = v

    cpdef double get_momentum(self):
        return self.mass * self.velocity

    cdef double get_momentum_c(self):
        return self.mass * self.velocity

    property energy:
        """The energy Particle property."""
        def __get__(self):
            """energy's getter"""
            return self.mass * self.velocity * self.velocity / 2
        def __set__(self, e):
            """energy's setter"""
            self.velocity = sqrt(e * 2 / self.mass)


cdef class CParticle(Particle):
    cdef double momentum
    def __init__(self, m, p, v):
        # super(CParticle, self)
        super().__init__(m, p, v)
        self.momentum = self.mass * self.velocity

    cpdef double get_momentum(self):
        return self.momentum

    cdef double get_momentum_c(self):
        return self.momentum


def add_momentums_typed(list particles):
    """Returns the sum of the particle momentums."""
    cdef:
        double total_mom = 0.0
        Particle particle
    for particle in particles:
        total_mom += particle.get_momentum()
    return total_mom


def add_momentums_typed_c(list particles):
    """Returns the sum of the particle momentums."""
    cdef:
        double total_mom = 0.0
        Particle particle
    for particle in particles:
        total_mom += particle.get_momentum_c()
    return total_mom
