# pyXC
short wrapper in python to allow calculation of XC energy density for GGA and LDA functionals using libxc

Please refer to the tests/ subdirectory for a couple of examples

## Installation

Requirements:
- hard:
    - cython
    - libXC
- optional:
    - cube (currently not publicly availble)

To build the Cython extension inplace with the repository:

    $ python setup.py build_ext --inplace

Then you can add the directory to your PYTHONPATH and everything should (hopefully) work as expected.
