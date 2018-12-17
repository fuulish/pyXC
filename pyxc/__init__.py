import numpy as np
from copy import deepcopy
from evalxc import calc_exc

class XC(object):

    def __init__(self, c=None, rho=None, sgm=None, func_id=[1, 10]):
        """
        """

        self.func_id = np.array(func_id, dtype='int')

        if c is not None:
            self.c = deepcopy(c)
            self.rho = c.data.flatten().astype('float64')
        else:
            if rho is not None:
                self.rho = deepcopy(rho).astype('float64')

        if sgm is not None:
            self.sgm = deepcopy(sgm).astype('float64')
        else:
            if c is not None:
                dx = self.c.box_dim / self.c.data.shape
                grd = np.gradient(self.c.data, dx[0], dx[1], dx[2], edge_order=2)

                sgm = grd[0]*grd[0] + grd[1]*grd[1] + grd[2]*grd[2]
                self.sgm = sgm.flatten().astype('float64')
            else:
                self.sgm = None

        self._exc = None

    def calculate_exc(self):

        exc = np.zeros_like(self.rho)
        calc_exc(self.rho, self.sgm, exc, self.func_id)

        return exc

    @property
    def exc(self):
        if self._exc is None:
            self._exc = self.calculate_exc()

        return self._exc

    @exc.setter
    def exc(self, value):
        raise RuntimeError('Cannot set "exc" property')
