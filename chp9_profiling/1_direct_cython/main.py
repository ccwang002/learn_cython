"""\
Cython-ported integrate.py demo

Usage:
    main.py direct | anno | cysin
    main.py cyprof | csin | cyfull
    main.py -h | --help

Options:
    direct      pure port to Cython
    anno        add variable type
"""
# load Cython and compile on-the-fly
import pyximport
pyximport.install()

from math import pi, sin

def _sin2(x):
    return sin(x) ** 2

def main():
    a, b = 0.0, 2.0 * pi
    integrate(a, b, sin2, N=400000)

if __name__ == '__main__':
    import cProfile
    from docopt import docopt
    args = docopt(__doc__)
    if args['direct']:
        from integrate import integrate
        sin2 = _sin2
    elif args['anno']:
        from integrate_anno import integrate
        sin2 = _sin2
    elif args['cysin']:
        from integrate_anno import integrate
        from integrate_anno import cysin as sin2
    elif args['cyprof']:
        from integrate_anno_prof import integrate
        from integrate_anno_prof import cysin as sin2
    elif args['csin']:
        from integrate_csin import integrate
        from integrate_csin import cysin as sin2
    elif args['cyfull']:
        from integrate_full_cython import integrate
        sin2 = None
    cProfile.run('main()', sort='time')
