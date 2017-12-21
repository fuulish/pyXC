#!/usr/bin/env python

from pyxc import XC
import numpy as np
import unittest
import cube

class TestXC(unittest.TestCase):
    def test_water_dimer(self):
        c = cube.Cube('data/density.cube')
        xc = XC(c)
        exc = xc.get_exc()
        EXC = (exc * c.data.flatten()).sum() * c.dV

        self.assertAlmostEqual(EXC, -8.2939935007, places=5)

    def test_cp2k_hydrogen(self):
        c = cube.Cube('data/cp2k_rtp_0_0_1-ELECTRON_DENSITY-1.cube')
        xc = XC(c)
        exc = xc.get_exc()
        EXC = (exc * c.data.flatten()).sum() * c.dV

        self.assertAlmostEqual(EXC, -0.58913097576700, places=3)

    def test_simple_libxc(self):
        c = cube.Cube('data/simple.cube')
        xc = XC(c, func_id=[1,])

        exc = xc.get_exc(sgm=np.array([0.2, 0.3, 0.4, 0.5, 0.6]))

        ref = np.array([ -0.342809, -0.431912, -0.494416, -0.544175, -0.586194] )

        np.testing.assert_allclose(exc, ref, atol=1.e-5, rtol=0)

if __name__ == '__main__':
    unittest.main()
