CFLAGS=-Wall -g -I..
LDFLAGS=-L.
LDLIBS=-lcfib

all: libcfib.so
test: test_libcfib
	./test_libcfib

test_libcfib: test_libcfib.o

test_libcfib.o: test_libcfib.c

libcfib.so: cfib.o
	$(CC) -shared -undefined dynamic_lookup -o libcfib.so cfib.o
	cd .. && ln -s lib/libcfib.so libcfib.so

cfib.o: cfib.c

.PHONY: clean

clean:
	rm -f cfib.o test_libcfib.o
	rm -f test_libcfib
	rm -f libcfib.so
	rm -f ../libcfib.so
