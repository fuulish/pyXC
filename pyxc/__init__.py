import numpy as np
from copy import deepcopy
from xceval import calc_exc

class XC(object):

    def __init__(self, c, func_id=[0, 10]):
        """
        """

        self.func_id = np.array(func_id, dtype='int')
        self.c = deepcopy(c)

    def get_exc(self):
        dx = self.c.box_dim / self.c.data.shape
        grd = np.gradient(self.c.data, dx[0], dx[1], dx[2])
        sgm = np.linalg.norm(grd, axis=0)
        dns = deepcopy(self.c.data)

        grd = np.reshape(grd, (-1, 1))
        dns = np.reshape(dns, (-1, 1))
        sgm = np.reshape(sgm, (-1, 1))
        exc = np.zeros_like(dns)

        calc_exc(exc, dns, sgm, self.func_id)

        exc *= dns

        return exc.sum()
