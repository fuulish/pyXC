
local:
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	rm -rf evalxc.so build
