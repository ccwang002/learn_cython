import unittest
from functools import partial
import numpy as np
import numexpr
from inheritance import (
    Particle, CParticle,
    add_momentums_typed, add_momentums_typed_c
)


class PyParticle(object):
    """Simple Particle Type."""
    def __init__(self, m, p, v):
        self.mass = m
        self.position = p
        self.velocity = v

    def get_momentum(self):
        return self.mass * self.velocity


class PyCParticle(Particle):
    def __init_(self, m, p, v):
        super().__init__(m, p, v)

    def get_momentum(self):
        return super().get_momentum()


def generate_particles(n=0, particle_cls=None, seed=None):
    rs = np.random.RandomState(seed)
    rand_mass = np.abs(rs.normal(5e3, 3e3, size=n))
    rand_pos = rs.random_sample(size=n)
    rand_pos = numexpr.evaluate("rand_pos * 10 - 5")
    rand_velo = rs.normal(2, 10, size=n)
    if particle_cls is None:
        particle_cls = PyParticle  # fall back to Py Particle
    PCls = particle_cls
    return [
        PCls(m, p, v)
        for m, p, v in zip(rand_mass, rand_pos, rand_velo)
    ]

# fixate the number and data particles generate
_gen_particles = partial(generate_particles, n=1e3, seed=5566)
_true_mom = 9427780.8643737361

def add_momentums(particles):
    """Returns the sum of the particle momentums."""
    return sum(p.get_momentum() for p in particles)


class _GeneralAddMomentums(unittest.TestCase):
    _particle_cls = None

    def setUp(self):
        self.particles = _gen_particles(particle_cls=self._particle_cls)

    def test_add_momentums(self):
        self.assertAlmostEqual(
            add_momentums(self.particles), _true_mom)

    def test_add_momentums_typed(self):
        self.assertAlmostEqual(
            add_momentums_typed(self.particles), _true_mom)

    def test_add_momentums_typed_c(self):
        self.assertAlmostEqual(
            add_momentums_typed_c(self.particles), _true_mom)

    def test_change_private_member(self):
        self.particles[0].mass = 10


class PyAddMomentums(_GeneralAddMomentums):
    _particle_cls = PyParticle

    @unittest.skip("Not implemented")
    def test_add_momentums_typed(self):
        pass

    @unittest.skip("Not implemented")
    def test_add_momentums_typed_c(self):
        pass


class CyAddMomentums(_GeneralAddMomentums):
    _particle_cls = Particle

    @unittest.skip("Cannot access membor defined in Cython")
    def test_change_private_member(self):
        pass


class CySubClassAddMomentums(_GeneralAddMomentums):
    _particle_cls = CParticle

    @unittest.skip("Cannot access membor defined in Cython")
    def test_change_private_member(self):
        pass


class CyPySubClassAddMomentums(_GeneralAddMomentums):
    _particle_cls = PyCParticle

    @unittest.skip("Not implemented")
    def test_access_clevel_momentum(self):
        pass


class ParticleProperty(unittest.TestCase):
    def setUp(self):
        self.particle = Particle(100, 3.3, 2)  # m, p, v

    def test_get_energy(self):
        self.assertAlmostEqual(self.particle.energy, 200)

    def test_set_energy(self):
        self.particle.energy = 112.5
        self.assertAlmostEqual(self.particle.get_momentum(), 150)

