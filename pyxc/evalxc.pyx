import cython
import numpy as np
cimport numpy as np

cdef extern int c_xc_energy_density( double * exc, double * rho, double * sigma, long int len, long int * func_id, long int nfunc )

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_exc(np.ndarray[double, ndim=1, mode="c"] density not None, np.ndarray[double, ndim=1, mode="c"] sigma not None, np.ndarray[double, ndim=1, mode="c"] exc not None, np.ndarray[long int, ndim=1, mode="c"] func_id):

    cdef int ln
    cdef int err

    nrho = density.shape[0]
    nfunc = func_id.shape[0]

    err = c_xc_energy_density( &exc[0], &density[0], &sigma[0], nrho, &func_id[0], nfunc )

    #return exc
