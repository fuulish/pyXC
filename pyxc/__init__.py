import numpy as np
from copy import deepcopy
from evalxc import calc_exc

class XC(object):

    def __init__(self, c, func_id=[1, 10]):
        """
        """

        self.func_id = np.array(func_id, dtype='int')
        self.c = deepcopy(c)

    def get_exc(self, rho=None, sgm=None):

        if rho is None:
            dns = self.c.data.flatten().astype('float64')
        else:
            dns = rho

        if sgm is None: #and gga and higher...
            dx = self.c.box_dim / self.c.data.shape
            grd = np.gradient(self.c.data, dx[0], dx[1], dx[2])

            sgm = grd[0]*grd[0] + grd[1]*grd[1] + grd[2]*grd[2]
            sgm = sgm.flatten().astype('float64')

        exc = np.zeros_like(dns)
        calc_exc(dns, sgm, exc, self.func_id)

        return exc
