## Wrap external C library on OSX (using Clang)

Example `wrap_fib_ext.pyx`.

### Buid `cfib` as shared library

~~~bash
clang -Wall -c cfib.c
# create cfib.o
clang -shared -undefined dynamic_lookup -o libcfib.so cfib.c
# create libcfib.so
python setup_wrap_ext.py build_ext --inplace
~~~

Check it links to `libcfib.so`

~~~bash
otool -L wrap_fib_ext.so
# wrap_fib_ext.so:
# 	libcfib.so (compatibility version 0.0.0, current version 0.0.0)
# 	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1197.1.1)
~~~


### Build `cfib` from source

~~~bash
python setup_wrap.py build_ext --inplace
~~~

~~~bash
otool -L wrap_fib.so
# wrap_fib.so:
# 	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1197.1.1)
~~~
