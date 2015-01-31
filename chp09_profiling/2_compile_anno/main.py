import pyximport
pyximport.install()

from integrate_optim import demo, demo_no_overhead  # noqa

if __name__ == '__main__':
    import cProfile
    cProfile.run('demo()', sort='time')
    cProfile.run('demo_no_overhead()', sort='time')
