#!/usr/bin/env python

import pyxc
from pyxc import XC
from cube import Cube

Exc_ref = -4.12419564898472
Eh_ref = 17.95589449201523

edens = Cube('LDA-ELECTRON_DENSITY-1_0.cube')
tdens = Cube('LDA-TOTAL_DENSITY-1_0.cube')
hpot = Cube('LDA-v_hartree-1_0.cube')

Eh = (hpot.data * tdens.data).sum() * tdens.dV/2.
xc = XC(edens)
exc = xc.exc
exc = exc.reshape(edens.data.shape)

Exc = (exc * edens.data).sum() * edens.dV

print Exc_ref, Exc
print Eh_ref, Eh
