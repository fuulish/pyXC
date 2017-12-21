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

if __name__ == '__main__':
    unittest.main()
