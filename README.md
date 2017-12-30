# pyXC
short wrapper in python to allow calculation of XC energy density for GGA and LDA functionals using libxc

Please refer to the tests/ subdirectory for a couple of examples

## Installation

Requirements:
- hard:
    - Cython (http://cython.org/)
    - libxc (https://gitlab.com/libxc/libxc)
    - NumPy (http://www.numpy.org/)
- optional:
    - cube (currently not publicly availble)

To build the C extension in place with the repository:

    $ python setup.py build_ext --inplace

Then you can add the directory to your PYTHONPATH and everything should (hopefully) work as expected.
