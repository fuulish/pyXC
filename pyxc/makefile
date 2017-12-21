
libevalXC.so: evalXC.o
	gcc -shared -o libevalXC.so evalXC.o

libevalXC.a: evalXC.o
	ar -cvq libevalXC.a evalXC.o

evalXC.o:
	gcc -c -Wall -Werror -fpic evalXC.c
