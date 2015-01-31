"""Test fibonacci numbers in three ways making Cython extensions.

Ex. 0, 1, 1, 2, 3, 5, 8, 13
"""

def test_fib():
    """Testing fib() written directly in Cython."""
    import fib
    _fib = fib.fib
    assert _fib(0) == 0
    assert _fib(1) == 1
    assert _fib(7) == 13


def test_wrap_fib():
    """Testing fib() written in external C (statically linked)."""
    import wrap_fib
    _fib = wrap_fib.fib
    assert _fib(0) == 0
    assert _fib(1) == 1
    assert _fib(7) == 13


def test_wrap_fib_ext():
    """Testing fib() written in external C (dynamic linked)."""
    import wrap_fib_ext
    _fib = wrap_fib_ext.fib
    assert _fib(0) == 0
    assert _fib(1) == 1
    assert _fib(7) == 13




