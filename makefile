
all:
	@echo "Only for cleaning"

clean:
	python setup.py clean
	rm -rf evalxc.so build
