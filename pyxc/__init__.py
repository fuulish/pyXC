import numpy as np
from copy import deepcopy
from evalxc import calc_exc

class XC(object):

    def __init__(self, c, func_id=[1, 10]):
        """
        """

        self.func_id = np.array(func_id, dtype='int')
        self.c = deepcopy(c)

    def get_exc(self):
        dx = self.c.box_dim / self.c.data.shape
        grd = np.gradient(self.c.data, dx[0], dx[1], dx[2])

        dns = deepcopy(self.c.data)
        dns = dns.flatten().astype('float64')

        sgm = np.linalg.norm(grd, axis=0)**2
        sgm = sgm.flatten().astype('float64')

        exc = np.zeros_like(dns)
        exc = calc_exc(exc, dns, sgm, self.func_id)

        return exc
