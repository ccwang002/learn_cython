## Usage
### Setup

~~~bash
python setup.py build_ext --inplace
~~~

For shared lib `libcfib` run

~~~bash
# under ./lib
clang -shared -undefined dynamic_lookup -I../ -o libcfib.so cfib.c; and mv libcfib.so ..
~~~

### Demo

~~~bash
nosetests -v
~~~

## Wrap external C library on OSX (using Clang)

Example `wrap_fib_ext.pyx`.

### Buid `cfib` as shared library

~~~bash
clang -Wall -c cfib.c  # create cfib.o
# create libcfib.so
clang -shared -undefined dynamic_lookup -I../ -o libcfib.so cfib.c; and mv libcfib.so ..
~~~

Check it links to `libcfib.so`

~~~bash
otool -L wrap_fib_ext.so
# wrap_fib_ext.so:
# 	libcfib.so (compatibility version 0.0.0, current version 0.0.0)
# 	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1197.1.1)
~~~


### Build `cfib` from source

Example `wrap_fib.pyx` (same content as `wrap_fib_ext.pyx`)

~~~bash
otool -L wrap_fib.so
# wrap_fib.so:
# 	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1197.1.1)
~~~
